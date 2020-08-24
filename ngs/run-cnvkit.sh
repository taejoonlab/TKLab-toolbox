#!/bin/bash
BAM_N="Normal.bam"
BAM_T="Tumor.bam"

REF="/home/taejoon/pub/ucsc/hg38/hg38_masked.fa"

# For WGS
# First run
cnvkit.py batch $BAM_T -n $BAM_N -m wgs -f $REF --annotate refFlat.txt -p 6

# Reuse the reference 
#cnvkit.py batch $BAM_T -m wgs -r reference.cnn -p 6
