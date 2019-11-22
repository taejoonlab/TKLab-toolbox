#!/bin/bash

# Make a symbolic link to reference genome
REF="REF.fa"

# Setup the Strelka2
# https://github.com/Illumina/strelka/blob/v2.9.x/docs/userGuide/quickStart.md
DIR_STRELKA="$HOME/src/strelka2/"

BAM_TUMOR="name of tumor BAM file"
BAM_NORMAL="name of normal BAM file"

OUT=${TUMOR_BAM/.bwa_mem.sorted.bam/}
OUT=$(basename $OUT)
echo $OUT

# add '--exome' for Exome sequencing
$DIR_STRELKA/bin/configureStrelkaSomaticWorkflow.py --referenceFasta=$REF --runDir=$OUT \
       --normalBam=$BAM_NORMAL --tumorBam=$TUMOR_BAM

