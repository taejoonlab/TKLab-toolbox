#!/bin/bash
NUM_THREADS=8

for FQ1 in $(ls *R1.raw.fastq.gz)
do
    FQ1_OUT=${FQ1/_R1.raw.fastq/_R1.trim.fastq}
    FQ2=${FQ1/_R1/_R2}
    FQ2_OUT=${FQ1_OUT/_R1/_R2}

    cutadapt --cores=$NUM_THREADS --max-n 1 --pair-filter=any \
        -a G{100} -A G{100} \
        -a CTGTCTCTTATACACATCT -A CTGTCTCTTATACACATCT \
        --minimum-length 50 \
        -o $FQ1_OUT -p $FQ2_OUT \
        $FQ1 $FQ2
done
