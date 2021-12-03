#!/bin/bash

## FASTA of genome sequences
#GENOME="MyGenome.fa"

#TAGS_T="tags.MyTF"

MOTIFS_T=${TAGS_T/tags./motifs.}
PEAKS=$TAGS_T"/peaks.txt"

if [ ! -e $MOTIFS_T ]; then
  mkdir $MOTIFS_T
fi

POS=$MOTIFS_T".motif_pos.txt"
cp $PEAKS $MOTIFS_T
findMotifsGenome.pl $PEAKS $GENOME $MOTIFS_T > $POS
