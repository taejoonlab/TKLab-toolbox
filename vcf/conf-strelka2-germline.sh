#!/bin/bash

# Make a symbolic link to reference genome
REF="$HOME/REF.fa"

# Setup the Strelka2
# https://github.com/Illumina/strelka/blob/v2.9.x/docs/userGuide/quickStart.md
DIR_STRELKA="$HOME/git/NGS-pipeline/strelka2/2.9.10/"

for BAM in $(ls ../bwa/*.bwa_mem.markdup.bam)
do
  OUT=${BAM/.bwa_mem.markdup.bam/}
  OUT=$(basename $OUT)
  echo $OUT
  $DIR_STRELKA/bin/configureStrelkaGermlineWorkflow.py --referenceFasta=$REF --runDir=$OUT --bam=$BAM
done
