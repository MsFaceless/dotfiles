#!/bin/bash

sudo mount -a
rsync -varuzP /home/camilla/enviros /home/camilla/NFS/drive_1/staff_folders/camilla
notify-send -u critical "Enviros backed up to NFS"
rsync -varuzP /home/camilla/Documents /home/camilla/NFS/drive_1/staff_folders/camilla
notify-send -u critical "Documents backed up to NFS"
