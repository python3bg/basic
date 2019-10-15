#!/bin/bash

# git config --global user.name "$(getent passwd $USER | cut -d ':' -f 5 | cut -d ',' -f 1)"
# git config --global user.email "benny.gu@sap.com"
if [ $# -eq 0 ];then
git commit -am "empty_commit_message"
else
git commit -am "$*"
fi
git push