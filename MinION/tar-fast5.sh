#!/bin/bash

## Tar-Gzip MinION result after running Albacore for basecalling
## See run-ont-basecall.sh for more details
##
## Author: Taejoon Kwon (https://github.com/taejoon)

## Directory for the raw fast5 files.
DIR_NAME=$1
DIR_RAW="$DIR_NAME/fast5"

## Assume that basecall result is recorded under 'called/ directory
## (via run-ont-basecall.sh)

DIR_PASS="$DIR_NAME/called/workspace/pass"
DIR_FAIL="$DIR_NAME/called/workspace/fail"

## Archive FASTQ
echo "Merge FASTQ"
cat $DIR_PASS/*fastq > $DIR_NAME".pass.fastq"
cat $DIR_FAIL/*fastq > $DIR_NAME".fail.fastq"

## Archive logs
tar cvzpf $DIR_NAME.log.tgz  $DIR_NAME/called/*.*

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

## Archive passed fast5
SUBDIR_PASS=($(ls -d $DIR_PASS/*/))
SUBDIR_PASS_LEN=${#SUBDIR_PASS[@]}

for ((i=0; i<$SUBDIR_PASS_LEN;i+=10));
do
  IDX=$(( i / 10 ))
  TGZ_OUT=$DIR_NAME".fast5_pass_"$IDX"n.tgz"
  DIR_IN="$DIR_PASS/"$IDX"?/"
  if [ $i == 0 ]; then
    DIR_IN="$DIR_PASS/?/"
  fi
  echo $TGZ_OUT
  tar cvzpf $TGZ_OUT $DIR_IN
done

## Archive failed fast5
SUBDIR_FAIL=($(ls -d $DIR_FAIL/*/))
SUBDIR_FAIL_LEN=${#SUBDIR_FAIL[@]}

for ((i=0; i<$SUBDIR_FAIL_LEN;i+=10));
do
  IDX=$(( i / 10 ))
  TGZ_OUT=$DIR_NAME".fast5_fail_"$IDX"n.tgz"
  DIR_IN="$DIR_FAIL/"$IDX"?/"
  if [ $i == 0 ]; then
    DIR_IN="$DIR_FAIL/?/"
  fi
  echo $TGZ_OUT
  tar cvzpf $TGZ_OUT $DIR_IN
done
