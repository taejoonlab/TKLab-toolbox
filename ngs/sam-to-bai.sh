#!/bin/bash
## Install samtools using Bioconda
##
## $ conda install -c bioconda samtools
##
## This script is based on samtools version 1.7

SAM_SUFFIX=".sam_hit"
NUM_THREADS=4

for SAM in $(ls *$SAM_SUFFIX)
do
  echo "Processing $SAM ..."

  BAM=${SAM/$SAM_SUFFIX/}".bam"
  if [ ! -e $BAM ]; then
    samtools view -@ $NUM_THREADS -bS -o $BAM $SAM
  else
    echo "$BAM is already available. Skip."
  fi

  SORTED_BAM=${SAM/$SAM_SUFFIX/}".sorted.bam"
  if [ ! -e $SORTED_BAM ]; then
    samtools sort -@ $NUM_THREADS -o $SORTED_BAM $BAM
  else
    echo "$SORTED_BAM is already available. Skip."
  fi

  BAM_INDEX=${SAM/$SAM_SUFFIX/}".sorted.bam.bai"
  if [ ! -e $BAM_INDEX ]; then
    samtools index -@ $NUM_THREADS $SORTED_BAM
  else
    echo "$BAM_INDEX is already available. Skip."
  fi
done
