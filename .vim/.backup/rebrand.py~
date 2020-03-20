import os
import sys
import subprocess

def create_args_dict():
    args_dict = {item.split('=')[0]:item.split('=')[1] for item in sys.argv if '=' in item}
    return args_dict

def rename_things(target_dir, target_string, substitute):
    for root, dirlist, filelist in os.walk(target_dir):
        for thedir in dirlist:
            if target_string in thedir:
                before = os.path.join(root, thedir)
                after = os.path.join(root, thedir.replace(target_string, substitute))
                os.rename(before, after)
                return False

        for thefile in filelist:
            if target_string in thefile:
                before = os.path.join(root, thefile)
                after = os.path.join(root, thefile.replace(target_string, substitute))
                os.rename(before, after)
                return False 

    return True

def rename():
    args_dict = create_args_dict()
    target_string = args_dict.get('target', None)
    if not target_string: print("No target_string found")
    substitute = args_dict.get('sub', None)
    if not substitute: print("No substitute found")
    target_dir = args_dict.get('target_dir', '.')

    casings = [None, 'upper', 'lower', 'capitalize', 'title']
    end = False
    for casing in casings:
        if casing == None:
            the_string = target_string
            the_substitute = substitute
        else:
            the_string = getattr(target_string, casing)()
            the_substitute = getattr(substitute, casing)()

        while not end: end = rename_things(target_dir, the_string, the_substitute)

        sub_files_process = subprocess.Popen([f"grep -rl {the_string} {target_dir}/ | xargs sed -i 's/{the_string}/{the_substitute}/g'"], shell=True)
        sub_files_process.wait()
        print(f"Replaced '{the_string}' in folder '{target_dir}/' with '{the_substitute}'")

if __name__ == "__main__":
    rename()
