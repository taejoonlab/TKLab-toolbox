#!/bin/bash

# Install homer via CONDA
# $ conda install -c bioconda homer

# Change the following BAM (or other supported format)
BAM_CHIP="../bam/MyTF.bam"

OUT_DIR="tags.MyTF"

# Use '-single' for the genome with many scaffolds 
# (make a single output file instead of each file per chromosome/scaffold)

makeTagDirectory $OUT_DIR -format SAM -single $BAM_CHIP
