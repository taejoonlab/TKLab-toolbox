#!/bin/bash

## FASTA of genome sequences

GENOME="$HOME/pub/ucsc/hg38/hg38_ref.fa"

MOTIF_DIR="motifs.<my data>"

MOTIF_LIB=$MOTIF_DIR".known1-6.motif"
PEAKS=$MOTIF_DIR"/peaks.txt"

MOTIF_POS=$MOTIF_DIR".motif_pos.txt"

findMotifsGenome.pl $PEAKS $GENOME $MOTIF_DIR -find $MOTIF_LIB > $MOTIF_POS

#MOTIF_ANNOT=$MOTIFS".motif_annot.txt"
#annotatePeaks.pl $PEAKS $GENOME -m $MOTIF_LIB > $MOTIF_ANNOT
