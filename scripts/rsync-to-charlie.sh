#!/bin/bash

SOURCE_HOST="<username>@<remote host>"
LOG="rsync-to-remote_host.log"

SOURCE_DIR=$(pwd -P)
if [ -e DIR.remote ]; then
  SOURCE_DIR=$(cat DIR.remote)
fi
echo $SOURCE_DIR

#SOURCE_DIR=$PWD
TARGET_DIR=$SOURCE_DIR

CMD='rsync -avz -e "ssh -p 3030 "' 
CMD+=" ./ $SOURCE_HOST:$SOURCE_DIR/"

echo >> $LOG
date >> $LOG
echo $CMD >> $LOG
rsync -avz -e "ssh -p 3030 " ./ $SOURCE_HOST:$SOURCE_DIR/ | tee -a $LOG
