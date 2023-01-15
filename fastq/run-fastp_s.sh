#!/bin/bash
NUM_THREADS=8

for IN_1 in $(ls *XENTR*.called.fastq.gz)
do
  OUT=${IN_1/.called.fastq/}
  OUT=${OUT/.gz/}
  OUT_HTML=$OUT".html"
  OUT_LOG=$OUT".log"

  OUT_1=$OUT".process.fastq"
  UN_1=$OUT".unpaired.fastq"

  echo "##########"
  echo $IN_1
  fastp --thread $NUM_THREADS --in1 $IN_1 --out1 $OUT_1 \
    -l 50 -h $OUT_HTML
    #--reads_to_process 1000000
done

