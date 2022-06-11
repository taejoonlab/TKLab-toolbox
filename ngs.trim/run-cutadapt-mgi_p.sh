#!/bin/bash
# ref: https://www.seqanswers.com/forum/general/74820-trimming-bgi-adapters?t=87647
for FQ1 in $(ls *R1.raw.fastq.gz)
do
  FQ1_OUT=${FQ1/_R1.raw.fastq/_R1.trim.fastq}
  
	FQ2=${FQ1/_R1/_R2}
  FQ2_OUT=${FQ1_OUT/_R1/_R2}

  cutadapt --cores=16 --max-n 1 --pair-filter=any \
    -a AAGTCGGAGGCCAAGCGGTCTTAGGAAGACAA -A AAGTCGGATCGTAGCCATGTCGTTCTGTGAGCCAAGGAGTTG \
    --minimum-length 50 \
    -o $FQ1_OUT -p $FQ2_OUT \
    $FQ1 $FQ2
done
