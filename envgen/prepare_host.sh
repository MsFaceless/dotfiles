#!/usr/bin/bash

source target_config
ssh-copy-id $SSH_STRING 
scp pyact $SSH_STRING:
bash deploy_$(python check_host_os.py '-host='$HOST '-user='$USER).sh
