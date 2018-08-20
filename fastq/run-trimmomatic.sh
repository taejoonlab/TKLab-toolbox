#!/bin/bash

## Assume that you install trimmomatic with conda

## Directory for conda
DIR_CONDA=$HOME/miniconda3

FA_ADAPTER=$( find $DIR_CONDA | grep -m1 TruSeq3-PE-2.fa )
echo "Adapter: "$FA_ADAPTER

for FQ1 in $(ls *R1.*fastq)
do
  FQ2=${FQ1/_R1/_R2}
  OUT=${FQ1/_R1.raw.fastq}"_trim"

  trimmomatic PE -validatePairs -summary $OUT".summary" $FQ1 $FQ2 -baseout $OUT \
    $FA_ADAPTER:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:50
done

