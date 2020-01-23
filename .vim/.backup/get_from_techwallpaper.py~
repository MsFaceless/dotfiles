#!/bin/python

import os
import requests
from bs4 import BeautifulSoup

START = "http://getwallpapers.com/collection/4k-tech-wallpaper"
PATH="/home/camilla/Pictures/wallpapers"

req = requests.get(START)
soup = BeautifulSoup(req.content, "html.parser")
taglist = soup.findAll("a", {"class": "download_button"})

for tag in taglist:

    dlink = tag['data-download']
    filename = f"{dlink.split('/')[-1]}.jpg"

    filepath = os.path.join(PATH, filename)
    if not os.path.exists(filepath):
        print("Downloading: {0}".format(filename))
        req = requests.get(dlink, stream=True)
        with open(filepath, "wb") as fobj:
            for chunk in req.iter_content(1024):
                fobj.write(chunk)
    else:
        print("Passing: {0}".format(filename))
