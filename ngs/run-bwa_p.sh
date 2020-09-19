#!/bin/bash
NUM_THREADS=8

DB="$HOME/db.bwa/hg38_ref"
DBNAME=$(basename $DB)

for FQ1 in $(ls ../fastq/*_1P)
do
  FQ2=${FQ1/_1P/_2P}

  SAM=$(basename $FQ1)
  SAM=${SAM/_1P/}"."$DBNAME".bwa_mem.sam"
  BAM=${SAM/.sam/}".bam"
  SORT_N=${SAM/.sam/}".sortN.bam"
  FIXMATE=${SAM/.sam/}".fixmate.bam"
  SORT_C=${SAM/.sam/}".sortC.bam"
  MARKDUP=${SAM/.sam/}".markdup.bam"

  if [ -e $MARKDUP ]; then
    echo "Skip $FQ1"
    continue
  fi

  if [ ! -e $SAM ]; then
    echo "Make $SAM"
    bwa mem -M -t $NUM_THREADS $DB $FQ1 $FQ2 > $SAM
  fi
    

  if [ ! -e $BAM ]; then
    echo "Make $BAM"
    samtools view -h -@ $NUM_THREADS -o $BAM $SAM
  fi

  if [ -e $BAM ] && [ ! -e $SORT_N ]; then
    echo "Make $SORT_N"
    samtools sort -n -@ $NUM_THREADS --output-fmt BAM -o $SORT_N $BAM
    samtools fixmate -m -@ $NUM_THREADS --output-fmt BAM $SORT_N $FIXMATE
  fi

  if [ -e $FIXMATE ] && [ ! -e $SORT_C ]; then
    echo "Make $SORT_C"
    samtools sort -@ $NUM_THREADS --output-fmt BAM -o $SORT_C $FIXMATE
    samtools index -@ $NUM_THREADS $SORT_C
  fi

  if [ -e $MARKDUP ]; then
    echo "Make $MARKDUP"
    samtools markdup -@ $NUM_THREADS -s -r $SORT_C $MARKDUP
    samtools index -@ $NUM_THREADS $MARKDUP
  fi
done
