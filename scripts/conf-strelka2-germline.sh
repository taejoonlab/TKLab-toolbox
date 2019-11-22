#!/bin/bash

# Make a symbolic link to reference genome
REF="REF.fa"

# Setup the Strelka2
# https://github.com/Illumina/strelka/blob/v2.9.x/docs/userGuide/quickStart.md
DIR_STRELKA="$HOME/src/strelka2/"

for BAM in $(ls ../bwa/*.bwa_mem.sorted.bam)
do
  OUT=${BAM/.bwa_mem.sorted.bam/}
  OUT=$(basename $OUT)
  echo $OUT
  $DIR_STRELKA/bin/configureStrelkaGermlineWorkflow.py --referenceFasta=$REF --runDir=$OUT --bam=$BAM
done
