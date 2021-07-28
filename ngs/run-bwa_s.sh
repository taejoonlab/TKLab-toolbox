#!/bin/bash
NUM_THREADS=8

DB="$HOME/pub/ucsc/mm39/db.bwa/mm39_chr"
DBNAME=$(basename $DB)

for FQ1 in $(ls ../fastq/*_trim.fq)
do
  SAM=$(basename $FQ1)
  SAM=${SAM/_trim.fq/}"."$DBNAME".bwa_mem.sam"
  BAM=${SAM/.sam/}".bam"
  SORT_C=${SAM/.sam/}".sortC.bam"
  MARKDUP=${SAM/.sam/}".markdup.bam"

  if [ -e $MARKDUP ]; then
    echo "Skip $FQ1"
    continue
  fi

  if [ ! -e $SAM ]; then
    echo "Make $SAM"
    bwa mem -M -t $NUM_THREADS $DB $FQ1 > $SAM
  fi

  if [ ! -e $BAM ]; then
    echo "Make $BAM"
    samtools view -h -@ $NUM_THREADS -o $BAM $SAM
    rm $SAM
  fi

  if [ -e $BAM ] && [ ! -e $SORT_C ]; then
    echo "Make $SORT_C"
    samtools sort -@ $NUM_THREADS --output-fmt BAM -o $SORT_C $BAM
    samtools index -@ $NUM_THREADS $SORT_C
  fi

  if [ ! -e $MARKDUP ]; then
    echo "Make $MARKDUP"
    samtools markdup -@ $NUM_THREADS -s -r $SORT_C $MARKDUP
    samtools index -@ $NUM_THREADS $MARKDUP
  fi
done
