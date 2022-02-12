#!/bin/bash
NUM_THREADS=8

for IN_1 in $(ls *XENTR*.untie_1.fastq.gz)
do
  IN_2=${IN_1/untie_1/untie_2}
  OUT=${IN_1/.untie_1.fastq/}
  OUT=${OUT/.gz/}
  OUT_HTML=$OUT".html"
  OUT_LOG=$OUT".log"

  OUT_1=$OUT"_R1.process.fastq"
  OUT_2=$OUT"_R2.process.fastq"
  UN_1=$OUT"_R1.unpaired.fastq"
  UN_2=$OUT"_R2.unpaired.fastq"

  echo "##########"
  echo $IN_1 $IN_2
  fastp --thread $NUM_THREADS --in1 $IN_1 --in2 $IN_2 --out1 $OUT_1 --out2 $OUT_2 \
    --unpaired1 $UN_1 --unpaired2 $UN_2 -l 50 -h $OUT_HTML
    #--reads_to_process 1000000
done

