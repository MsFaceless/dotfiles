#!/usr/bin/bash

source target_config
scp bootstrap_ubuntu.sh $SSH_STRING:
scp create_environment.sh $SSH_STRING:
ssh $SSH_STRING 'bash bootstrap_ubuntu.sh'
