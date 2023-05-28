#!/bin/bash

## A script to concatenate paired-end reads with flash. 

## Installation via conda
# $ conda install -c bioconda flash

NUM_THREADS=4
MAX_OVERLAP=140  # ReadLength - 10 bp

#for R1 in $(ls *_R1.raw.fastq.gz)
for R1 in $(ls *_R1.trim.fastq.gz)
do
  R2=${R1/_R1/_R2}

  #OUT_NAME=${R1/.raw.fastq.gz/}
  OUT_NAME=${R1/.trim.fastq/}
  OUT_NAME=$(echo $OUT_NAME | sed 's/.gz$//')
  OUT_NAME=$(echo $OUT_NAME | sed 's/_R1$//')

  echo $R1 $R2 $OUT_NAME

  #flash $R1 $R2 -o $OUT_NAME -t $NUM_THREADS -M $MAX_OVERLAP --interleaved-output
done

