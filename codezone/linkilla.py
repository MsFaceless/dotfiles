#!/bin/python
import os

for i in os.listdir(os.path.abspath(os.path.curdir)):
    try: print(f"Im good: {os.stat(i)}")
    except: os.remove(i)
