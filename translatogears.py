import time
import requests
from flask import Flask
from bs4 import BeautifulSoup as NewSoup
from bs4 import Tag
BeautifulSoup = lambda x: NewSoup(x, 'html.parser')

class Translate():

    def __init__(self, *args, **kwargs):
        self.base_url = kwargs.get('base_url')
        self.auth_data = kwargs.get('auth_data')
        self.session = requests.Session()
        self.site_dict = {}
        if self.base_url and self.auth_data: self.generate_site()

    def get_target_link(self, link):
        cleaned_link = link.replace("/", "%2F")
        thislink = f"{self.base_url}{self.login_handler_url}?came_from={cleaned_link}"
        return thislink

    def try_rocket_auth(self):
        print()
        return

    def try_zordon_auth(self):
        print()
        return

    def authenticate_session(self):
        auth_r = self.session.get(f'{self.base_url}')
        auth_soup = BeautifulSoup(auth_r.text)
        if auth_r.url != self.base_url:
            auth_url = auth_r.url[len(self.base_url):].split("?")[0]
            #self.site_dict[auth_url] = auth_soup.renderContents()
            self.site_dict[auth_url] = auth_r.text
            self.login_dict = {
                    'login':self.auth_data.get('username'), 
                    'password':self.auth_data.get('password')
                    }
        form_action_url = "/login_handler?"
        if not self.login_dict == {}:
            if form_action_url:
                self.login_handler_url = form_action_url.split("?")[0]
                auth_url = f'{self.base_url}{form_action_url}'
                auth_url = f'{self.base_url}{self.login_handler_url}'
                auth_r = self.session.post(auth_url, data=self.login_dict)
                authed_soup = BeautifulSoup(auth_r.text)
                #self.site_dict['/'] = authed_soup.renderContents()
                #self.site_dict['/'] = auth_r.text
                if auth_r: return True
        return False

    def unpack_item(self, item):
        if not len(item) == 2: return False, False
        return item[0], item[1]

    def process_images(self, item, tempdict):
        link, html = self.unpack_item(item)
        itemsoup = BeautifulSoup(html)
        for img in itemsoup.find_all('img'):
            img_url = img.get('src')
            if img_url:
                img_r = self.session.post(self.get_target_link(img_url), data=self.login_dict)
                if img_r: 
                    img_link = img_url.lstrip('.')
                    if not tempdict.get(img_url): tempdict[img_link] = img_r.text
        return True

    def process_scripts(self, item, tempdict):
        link, html = self.unpack_item(item)
        print(f"Processing scripts for {link}")
        itemsoup = BeautifulSoup(html)
        for script in itemsoup.find_all('script'):
            script_url = script.get('src')
            if script_url:
                if not self.site_dict.get(script_url): 
                    script_r = self.session.post(self.get_target_link(script_url), data=self.login_dict)
                    if script_r: tempdict[script_url] = script_r.text
            elif not script_url: self.process_complex_script(script, tempdict)
        return True

    def process_complex_script(self, script_tag, tempdict):
        print("Processing Complex Script")
        target_link = None
        for line in script_tag.prettify().split("\n"):
            target_link = None
            if '.get(' in line:
                print("Get Found")
                target_link = line.split('.get')[1]
                check_spaces = target_link.split(" ")
                if len(check_spaces) > 1: target_link = check_spaces[0]
                target_link = target_link.replace('"', '').replace("'", "").replace(',', '').lstrip("(")
            elif '.load(' in line:
                print("Load Found")
                target_link = line.split('load')[1].split(',')[0].lstrip('(')
                if "?" in line: question_split = target_link.split("?")
                else: question_split = [target_link]
                if len(question_split) > 1: target_link = question_split[0]
                target_link = target_link.replace('"', '').replace("'", "")
            elif '.redirect(' in line:
                print("Redirect Found")
                target_link = line.split('$.redirect(')[1].split(')')[0]
                check_spaces = target_link.split(" ")
                if len(check_spaces) > 1: target_link = check_spaces[0]

            if target_link:
                if not self.site_dict.get(target_link):
                    clean_target_link = self.get_target_link(target_link)
                    this_r = self.session.post(clean_target_link, data=self.login_dict)
                    if this_r: tempdict[target_link] = this_r.text
        return True

    def process_links(self, item, tempdict):
        link, html = self.unpack_item(item)
        print(f"Processing links for {link}")
        item_soup = BeautifulSoup(html)
        tag_list = item_soup.find_all('link')
        for tag in tag_list:
            this_link = tag.get('href')
            if this_link: 
                already_gotted = tempdict.get(this_link)
                if not already_gotted:
                    clean_target_link = self.get_target_link(this_link)
                    this_link_request = self.session.post(clean_target_link, data=self.login_dict)
                    if this_link_request: 
                        tempdict[this_link] = this_link_request.text
                    elif not this_link_request:
                        del this_link
                        del this_link_request
                else:
                    #print(tempdict[this_link])
                    print("I am be gotted")
            elif not thislink:
                print("I would have been missed")
        return True

    def process_atags(self, item, tempdict):
        link, html = self.unpack_item(item)
        item_soup = BeautifulSoup(html)
        tag_list = item_soup.find_all('a')
        for tag in tag_list:
            this_link = tag.get('href')
            if this_link:
                #if 'http' in this_link: continue
                if not tempdict.get(this_link):
                    this_link_request = self.session.post(self.get_target_link(this_link), data=self.login_dict)
                    if this_link_request: tempdict[this_link] = BeautifulSoup(this_link_request.text).renderContents()
        return True

    def build_pages(self, tempdict={}):
        print("-"*80)
        print()
        if tempdict != {}: self.site_dict.update(tempdict)
        site_dict_copy = self.site_dict.copy()
        tempdict = self.site_dict.copy()
        already_processed = []
        for item in site_dict_copy.items():
            link, html = self.unpack_item(item)
            if link in already_processed: continue
            #if link.startswith('#'): continue
            if len(link.split("?")) > 1: 
                link = link.split("?")[0]
            self.process_links(item, tempdict)
            self.process_images(item, tempdict)
            self.process_atags(item, tempdict)
            self.process_scripts(item, tempdict)
            #self.process_fonts(item, tempdict)
            self.process_self(item, tempdict)
            already_processed.append(link)
            #if not link.startswith('http'):
        print()
        print("-"*80)
        tempdict = {k:v for k, v in tempdict.items() if 'http' not in k}
        self.site_dict = {k:v for k, v in self.site_dict.items() if 'http' not in k}
        if tempdict.keys() != self.site_dict.keys(): 
            self.build_pages(tempdict)
        else: return True

    def process_fonts(self, item, tempdict):
        print("Processing Fonts")
        link, html = self.unpack_item(item)
        item_soup = BeautifulSoup(html)
        for link in item_soup.find_all('link'):
            link_url = link.get('href')
            if 'font' in link_url:
                if link_url.startswith('http'):
                    link_request = self.session.get(link_url)
                    if link_request: 
                        replace_tag = BeautifulSoup(f"<style>{link_request.text}</style>")
                        to_replace = item_soup.find('link', attrs={'href':link_url})
                        to_replace.replace_with(replace_tag)
                        new_html = item_soup.renderContents()
                        print(new_html)
                        tempdict[link_url] = new_html
                else:
                    link_request = self.session.post(self.get_target_link(link_url), data=self.login_dict)
                    if link_request:
                        for item in link_request.text.split('url'):
                            if '/fonts' in item:
                                font_link = item.lstrip('("..').split('"')[0]
                                font_link = font_link.split("?")[0]
                                font_request = self.session.post(self.get_target_link(font_link), data=self.login_dict)
                                if font_request: tempdict[font_link] = font_request.text
        return True

    def process_self(self, item, tempdict):
        print("Processing Self")
        link, html = self.unpack_item(item)
        item_soup = BeautifulSoup(html)
        link_list = [link for link in item_soup.find_all('link')]
        if len(link_list) == 0: return True
        other_link = link_list[0]
        other_link_url = other_link.get('href')
        other_link_html = tempdict.get(other_link_url)
        if other_link_html:
            replace_tag = BeautifulSoup(f"<style>{other_link_html}</style>")
            to_replace = item_soup.find('link', attrs={'href':other_link_url})
            to_replace.replace_with(replace_tag)
            new_html = item_soup.renderContents()
            tempdict[link] = new_html
        self.process_self((link, new_html), tempdict)

    def generate_site(self):
        print("Generating Site")
        host = '0.0.0.0'
        port = 25000
        app = Flask(__name__, static_url_path='')
        is_authable = self.authenticate_session()
        if is_authable: self.build_pages()
        for k, v in self.site_dict.items(): 
            if k == '/': self.wrap_server(app, '', v)
            else: self.wrap_server(app, k, v)
        print(app.url_map)
        app.run(host, port)
        return True

    def wrap_server(self, app, name, html):
        actual_name = name.split("/")[-1]
        print(actual_name)
        def wrapped(): return html
        setattr(wrapped, "__qualname__", name)
        setattr(wrapped, "__name__", name)
        if not name.startswith('/'): name = f'/{name}'
        app.route(name, methods=['GET'])(wrapped)
        return wrapped

if __name__ == "__main__":
    auth_dict = {'username':'developer', 'password':'developpass'}
    """
    kwargs = {
            'base_url':'http://192.168.0.3:8088',
            'auth_data':auth_dict,
            }
    t = Translate(**kwargs)
    """
    kwargs = {
            'base_url':'http://localhost:1234',
            'auth_data':auth_dict,
            }
    t = Translate(**kwargs)
