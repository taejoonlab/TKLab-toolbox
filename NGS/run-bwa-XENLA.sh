#!/bin/bash
NUM_THREADS=8

SAMTOOLS="$HOME/miniconda3/bin/samtools"
BWA="$HOME/miniconda3/bin/bwa"

SAM_BEST="$HOME/git/HTseq-toolbox/sam/sam-to-sam_best.py"

DB="$HOME/public/db.bwa/XENLA_dna.GCA001663975v1+"
DBNAME=$(basename $DB)

for FQ1 in $(ls ../fastq/*.fastq.gz)
do
  #FQ2=${FQ1/_1/_2}

  SAM=$(basename $FQ1)
  SAM=${SAM/.fastq.gz/}"."$DBNAME".bwa_mem.sam"
  RMDUP_BAM=${SAM/.sam/}".best_rmdup.bam"

  if [ -e $RMDUP_BAM ]; then
    echo "Skip $FQ1"
    continue
  fi

  if [ ! -e $SAM ]; then
    echo "Make $SAM"
    $BWA mem -t $NUM_THREADS $DB $FQ1 > $SAM
  fi

  BEST_SAM=$SAM"_best"
  if [ -e $SAM ] && [ ! -e $BEST_SAM ]; then 
    echo "Make $BEST_SAM"
    $SAM_BEST $SAM
  fi
  
  BAM=${SAM/.sam/}".best.bam"
  if [ -e $BEST_SAM ] && [ ! -e $BAM ]; then
    echo "Make $BAM"
    $SAMTOOLS view -@ $NUM_THREADS -b -o $BAM $BEST_SAM
  fi

  SORTED_BAM=${SAM/.sam/}".best_sorted.bam"
  if [ -e $BAM ] && [ ! -e $SORTED_BAM ]; then
    echo "Make $SORTED_BAM"
    $SAMTOOLS sort -@ $NUM_THREADS -o $SORTED_BAM $BAM
  fi

  RMDUP_BAM=${SAM/.sam/}".best_rmdup.bam"
  if [ -e $SORTED_BAM ] && [ ! -e $RMDUP_BAM ]; then
    echo "Make $RMDUP_BAM"
    $SAMTOOLS rmdup -s --output-fmt BAM $SORTED_BAM $RMDUP_BAM
  fi
  
  BAM=${SAM/.sam/}".bam"
  if [ -e $SAM ] && [ ! -e $BAM ]; then
    echo "Make $BAM"
    $SAMTOOLS view -@ $NUM_THREADS -b -o $BAM $SAM
  fi

  SORTED_BAM=${SAM/.sam/}".sorted.bam"
  if [ -e $BAM ] && [ ! -e $SORTED_BAM ]; then
    echo "Make $SORTED_BAM"
    $SAMTOOLS sort -@ $NUM_THREADS -o $SORTED_BAM $BAM
  fi

  RMDUP_BAM=${SAM/.sam/}".rmdup.bam"
  if [ -e $SORTED_BAM ] && [ ! -e $RMDUP_BAM ]; then
    echo "Make $RMDUP"
    $SAMTOOLS rmdup -s --output-fmt BAM $SORTED_BAM $RMDUP_BAM
  fi
done
