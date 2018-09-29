#!/bin/bash

## Tar-Gzip MinION result after running Albacore for basecalling
## See run-ont-basecall.sh for more details
##
## Author: Taejoon Kwon (https://github.com/taejoon)

## Directory for the raw fast5 files.
DIR_NAME=$1
DIR_RAW="$DIR_NAME/fast5"

## Archive raw fast5
SUBDIR_RAW=($(ls -d $DIR_RAW/*/))
SUBDIR_RAW_LEN=${#SUBDIR_RAW[@]}

for ((i=0; i<$SUBDIR_RAW_LEN;i+=10));
do
  IDX=$(( i / 10 ))
  TGZ_OUT=$DIR_NAME".fast5_raw_"$IDX"n.tgz"
  DIR_IN="$DIR_RAW/"$IDX"?/"
  if [ $i == 0 ]; then
    DIR_IN="$DIR_RAW/?/"
  fi
  echo $TGZ_OUT
  tar cvzpf $TGZ_OUT $DIR_IN
done
