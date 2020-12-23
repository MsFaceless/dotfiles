#!/bin/python
# -*- coding: utf-8 -*-
""" Get wallpapers from Design Milk website """

import os
import requests
from bs4 import BeautifulSoup


def get_soup_from_url(url):
    """ get_soup_from_url  """
    req = requests.get(url)
    return BeautifulSoup(req.content, "html.parser")


def get_linklist_from_url(url):
    """ get_linklist_from_url  """
    soup = get_soup_from_url(url)
    taglist = soup.findAll("a", {"class": "article-image"})
    return [tag["href"] for tag in taglist]


def write_links_file(starturl, filename):
    """ write_links_file  """
    totallist = []
    for i in range(10):
        url = starturl.format(i + 1)
        thislinklist = get_linklist_from_url(url)
        totallist.extend(thislinklist)
    with open(filename, "w") as fobj:
        for item in totallist:
            fobj.write("{0}\n".format(item))


def read_links_file(filename):
    """ read_links_file  """
    with open(filename, "r") as fobj:
        return fobj.readlines()


def do_next(filename, size="1900"):
    """ do_next """
    for url in read_links_file(filename):
        soup = get_soup_from_url(url)
        taglist = soup.find_all("a", href=True)
        taglist = [tag["href"] for tag in taglist if size in tag["href"].lower()]
        download_unique_files(taglist)


def download_unique_files(
    urllist, pictures_folderpath="/home/camilla/Pictures/wallpapers"
):
    """ download_unique_files """
    for url in urllist:
        filename = url.split("/")[-1]
        filepath = os.path.join(pictures_folderpath, filename)
        if not os.path.exists(filepath):
            print("Downloading: {0}".format(filename))
            req = requests.get(url, stream=True)
            with open(filepath, "wb") as fobj:
                for chunk in req.iter_content(1024):
                    fobj.write(chunk)
        else:
            print("Passing: {0}".format(filename))


if __name__ == "__main__":

    START = "https://design-milk.com/column/designer-desktops/page/{0}/"
    FNAME = "all_desktop_links.txt"
    # write_links_file(START, FNAME)

    do_next(FNAME)
