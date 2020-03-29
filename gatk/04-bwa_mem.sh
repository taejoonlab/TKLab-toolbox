#!/bin/bah

DB="~/db.bwa/Homo_sapiens_assembly38.fasta"
FQ_i="./fastq/DSMC202003_HUMANg_OvC-P01_Organoid.i_marked.fastq.gz"

OUT=$(basename $FQ_i)
OUT=${OUT/.i_marked.fastq.gz/}".HUMAN_hg38_broad.bwa_mem.sam"

bwa mem -M -t 10 -p -o $OUT $DB $FQ_i
