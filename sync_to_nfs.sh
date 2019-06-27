#!/bin/bash

sudo mount -a
rsync -varuzP /home/camilla/enviros /home/camilla/NFS/drive_2/Staff\ Folders/camilla
notify-send -u critical "Enviros backed up to NFS"
