#!/bin/bash

SEED=12345
R_COUNT=10000000

for FQ1 in $(ls *_R1.trim.fastq.gz)
do
  FQ2=${FQ1/_R1/_R2}
  OUT1=${FQ1/_R1.trim.fastq.gz/}"_10m_R1.trim.fastq.gz"
  OUT2=${FQ1/_R1.trim.fastq.gz/}"_10m_R2.trim.fastq.gz"

  echo $OUT1 $OUT2
  seqtk sample -s $SEED $FQ1 $R_COUNT > $OUT1
  seqtk sample -s $SEED $FQ2 $R_COUNT > $OUT2
done
