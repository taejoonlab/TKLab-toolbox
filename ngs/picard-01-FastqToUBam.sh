#!/bin/bash

FQ1="DSMC202003_HUMANg_OvC-P01_Organoid_R1.raw.fastq.gz"
FQ2=${FQ1/_R1/_R2}
OUT=${FQ1/_R1.raw.fastq.gz/}".ubam"

SAMPLE="DSMC202003_OvC-P01_Organoid"

TMP_DIR="/work/taejoon/tmp"

picard FastqToSam F1=$FQ1 F2=$FQ2 O=$OUT SM=$SAMPLE TMP_DIR=$TMP_DIR
