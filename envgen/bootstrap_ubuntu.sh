#!/bin/bash

apt --yes dist-upgrade
apt build-dep --yes python3 python3-dev linux-headers-$(uname -r) build-essential mercurial tldr
apt install --yes python3 python3-dev linux-headers-$(uname -r) build-essential mercurial openssh-server openssh-client tldr
apt install --yes mariadb-server mariadb-client libmariadbclient18
systemctl enable mariadb
systemctl enable ssh
