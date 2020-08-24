#!/bin/bash
  
BAM_N="Normal.bam"
BAM_T="Tumor.bam"

REF_GC="hg38_masked.gc50bp.wig.gz"

OUT=$(basename $BAM_T)
OUT=${OUT/.bwa_mem.sorted.bam/}".seqz.gz"
echo $OUT

sequenza-utils bam2seqz -n $BAM_N -t $BAM_T --fasta REF.fa -gc $REF_GC -o $OUT

