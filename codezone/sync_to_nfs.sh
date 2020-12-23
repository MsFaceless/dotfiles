#!/bin/bash
function dlswp {
    find . -iname "*.pyc" -print0 -exec rm -r {} \;
}

sudo mount -a

#cd /home/camilla/enviros && dlswp
#rsync -varuzzP /home/camilla/enviros /home/camilla/NFS/drive_1/staff_folders/camilla
#notify-send -u critical "Enviros backed up to NFS"

cd /home/camilla/Documents && dlswp
rsync -varuzzP /home/camilla/Documents /home/camilla/NFS/drive_1/staff_folders/camilla
notify-send -u critical "Documents backed up to NFS"
