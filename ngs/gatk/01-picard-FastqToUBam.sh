#!/bin/bash

FQ1=$1
FQ2=${FQ1/_R1/_R2}
SAMPLE=${FQ1/_R1.raw.fastq.gz/}
OUT=$SAMPLE".ubam"

TMP_DIR="$HOME/tmp"

picard FastqToSam F1=$FQ1 F2=$FQ2 O=$OUT SM=$SAMPLE TMP_DIR=$TMP_DIR
