#!/bin/bash
  
DB="/home/tklab_202003/db.bwa/Homo_sapiens_assembly38.fasta"
SAM="DSMC202003_HUMANg_OvC-P01_Organoid.HUMAN_hg38_broad.bwa_mem.sam"
UBAM="DSMC202003_HUMANg_OvC-P01_Organoid.ubam"
OUT=${SAM/.sam/}".merge.bam"

picard -Xmx32G MergeBamAlignment R=$DB UNMAPPED_BAM=$UBAM \
ALIGNED_BAM=$SAM O=$OUT \
CREATE_INDEX=true ADD_MATE_CIGAR=true \
CLIP_ADAPTERS=false \
CLIP_OVERLAPPING_READS=true \
INCLUDE_SECONDARY_ALIGNMENTS=true \
MAX_INSERTIONS_OR_DELETIONS=-1 \
PRIMARY_ALIGNMENT_STRATEGY=MostDistant \
ATTRIBUTES_TO_RETAIN=XS \
TMP_DIR=$HOME/work/tmp
