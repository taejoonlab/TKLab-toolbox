#!/bin/bash
NUM_THREADS=8

SAMTOOLS="$HOME/miniconda3/bin/samtools"

SAM_BEST="$HOME/git/HTseq-toolbox/sam/sam-to-sam_best.py"

GENOME_DIR="$HOME/public/db.star/"
DB_NAME="XENLA_dna.GCA001663975v1+"
#HUMAN_ens85_dna_sm
#XENTR_dna.GCA000004195v3+
DB=$GENOME_DIR$DB_NAME

for FQ1 in $(ls ../fastq/*.fastq.gz)
do
  #FQ2=${FQ1/untie_1/untie_2}
  BASENAME=$(basename $FQ1)
  BASENAME=${BASENAME/.fastq.gz/}
  SAM=$BASENAME".Aligned.out.sam"
  
  RMDUP_BAM=$BASENAME"."$DB_NAME".STAR.best_rmdup.bam"
  if [ -e $RMDUP_BAM ]; then
    echo "Skip $FQ1"
    continue
  fi

  if [ ! -e $SAM ]; then
    echo "Make $SAM"
    STAR --genomeDir $DB --runThreadN $NUM_THREADS --readFilesIn $FQ1 \
      --readFilesCommand zcat --outSAMtype SAM \
      --outFileNamePrefix $BASENAME"." --limitBAMsortRAM 32000000000
  fi
  
  BAM=$BASENAME"."$DB_NAME".STAR.bam"
  if [ -e $BEST_SAM ] && [ ! -e $BAM ]; then
    $SAMTOOLS view -@ $NUM_THREADS -b -o $BAM $SAM
  fi

  SORTED_BAM=$BASENAME"."$DB_NAME".STAR.sorted.bam"
  if [ -e $BAM ] && [ ! -e $SORTED_BAM ]; then
    $SAMTOOLS sort -@ $NUM_THREADS -o $SORTED_BAM $BAM
  fi
  
  RMDUP_BAM=$BASENAME"."$DB_NAME".STAR.rmdup.bam"
  if [ -e $SORTED_BAM ] && [ ! -e $RMDUP_BAM ]; then
    $SAMTOOLS rmdup -s --output-fmt BAM $SORTED_BAM $RMDUP_BAM
  fi

  BEST_SAM=$SAM"_best"
  if [ -e $SAM ] && [ ! -e $BEST_SAM ]; then
    $SAM_BEST $SAM
  fi
  
  BAM=$BASENAME"."$DB_NAME".STAR.best.bam"
  if [ -e $BEST_SAM ] && [ ! -e $BAM ]; then
    $SAMTOOLS view -@ $NUM_THREADS -b -o $BAM $BEST_SAM
  fi

  SORTED_BAM=$BASENAME"."$DB_NAME".STAR.best_sorted.bam"
  if [ -e $BAM ] && [ ! -e $SORTED_BAM ]; then
    $SAMTOOLS sort -@ $NUM_THREADS -o $SORTED_BAM $BAM
  fi

  RMDUP_BAM=$BASENAME"."$DB_NAME".STAR.best_rmdup.bam"
  if [ -e $SORTED_BAM ] && [ ! -e $RMDUP_BAM ]; then
    $SAMTOOLS rmdup -s --output-fmt BAM $SORTED_BAM $RMDUP_BAM
  fi
done
