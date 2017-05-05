#!/bin/bash
LIFTUP="$HOME/miniconda3/bin/liftUp"

DIR_LIFT="lift"

SUFFIX=".gmap.psl"
OUT_SUFFIX=".gmap.liftUp.psl"

for DIR_PSL in $(ls -d gmap.*)
do
  if [ ! -d $DIR_PSL ]; then
    continue
  fi
  
  for PSL in $(ls $DIR_PSL/*$SUFFIX)
  do
    LIFT=$DIR_LIFT"/"$(basename $PSL| awk -F"." '{print $1}')".lft"
    OUT_PSL=${PSL/$SUFFIX/}$OUT_SUFFIX
    echo "$LIFT -> $OUT_PSL"
    $LIFTUP -pslQ $OUT_PSL $LIFT warn $PSL
  done
done
