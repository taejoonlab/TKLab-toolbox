#!/bin/bash

BG2BW="$HOME/miniconda3/bin/bedGraphToBigWig"
BEDSORT="$HOME/miniconda3/bin/bedSort"
BEDCLIP="$HOME/miniconda3/bin/bedClip"
BEDTOOLS="$HOME/miniconda3/bin/bedtools"

SEQLEN="$HOME/xenopus.genome/XENLA_GCA001663975v1/XENLA_dna.GCA001663975v1+.seqlen"
BLOCK_SIZE=10

for BAM in $(ls *bam)
do
  BW=${BAM/.bam/}".bw"
  if [ -e $BW ]; then
    echo "Skip $BAM"
    continue
  fi

  BG_IN=${BAM/.bam/}".bg_in"
  if [ ! -e $BG_IN ] && [ -e $BAM ]; then
    echo "Make $BG_IN"
    $BEDTOOLS genomecov -ibam $BAM -bg > $BG_IN
  fi
  
  BG_CLIP=${BAM/.bam/}".bg_clip"
  if [ ! -e $BG_CLIP ] && [ -e $BG_IN ]; then
    echo "Make $BG_CLIP"
    $BEDCLIP $BG_IN $SEQLEN $BG_CLIP
  fi

  BG=${BAM/.bam/}".bg"
  if [ ! -e $BG ] && [ -e $BG_CLIP ]; then
    echo "Make $BG"
    $BEDSORT $BG_CLIP $BG
  fi
  
  BW=${BAM/.bam/}".bw"
  if [ ! -e $BW ] && [ -e $BG ]; then
    echo "Make $BW"
    $BG2BW $BG $SEQLEN -blockSize=$BLOCK_SIZE $BW
  fi
done
