#!/bin/bash
for SEQZ in $(ls *.seqz.gz)
do
  OUT=${SEQZ/.seqz.gz/}".w50seqz.gz"
  if [ ! -e $OUT ]; then
    echo $OUT
    sequenza-utils seqz_binning --seqz $SEQZ -w 50 -o $OUT
  fi
done
