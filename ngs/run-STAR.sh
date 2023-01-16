#!/bin/bash

NUM_THREADS=8

# DROME
# GENOME_DIR="$HOME/DGRP/db.dm6/db.STAR/"
# DB_GTF="$HOME/DGRP/db.dm6/dmel-all-r6.46.gtf"

GENOME_DIR="<a directory for the genome index>"
DB_GTF="<a path for the GTF file>"

for FQ1 in $(ls ../fastq/*_R1.trim.fastq.gz)
do
  FQ2=${FQ1/_R1/_R2}
  OUT=$(basename $FQ1)
  OUT=${OUT/_R1.trim.fastq.gz/}"."
  LOG_FINAL=$OUT"Log.final.out"

  echo "OUT_LOG: "$LOG_FINAL
  if [ ! -e $LOG_FINAL ]; then
    STAR --genomeDir $GENOME_DIR --runThreadN $NUM_THREADS \
        --readFilesIn $FQ1 $FQ2 --readFilesCommand zcat \
        --outSAMtype BAM SortedByCoordinate  \
        --outFileNamePrefix $OUT \
        --limitBAMsortRAM 1000000000 \
        --sjdbGTFfile $DB_GTF \
        --sjdbOverhang 100
  fi
done
