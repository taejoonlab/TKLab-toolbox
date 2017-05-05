#!/bin/bash

## Split target genome

FA_SPLIT="$HOME/miniconda3/bin/faSplit"

for FA in $(ls ../*.fa)
do
  NAME=$(basename $FA)
  NAME=$(echo $NAME | awk -F"." '{print $2}')

  if [ ! -d lift ]; then
    mkdir lift
  fi
  
  if [ ! -d split ]; then
    mkdir lift
  fi

  echo "$FA --> $NAME"
  $FA_SPLIT -lift=lift/$NAME.lft size $FA -oneFile 3000 split/$NAME
done
