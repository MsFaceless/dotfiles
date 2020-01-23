#!/bin/bash
echo "INPUT ROOT PASS"
read rootpass
mysql -uroot -p$rootpass < sql_cmd.txt
