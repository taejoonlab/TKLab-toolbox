#!/bin/bash
NUM_THREADS=16

#DIR_IN="MODtree.treefam"
DIR_IN=$1

for IN in $(ls $DIR_IN/*.fa)
do
  echo $IN
  OUT=${IN/.fa/.mafft_out}
  mafft --maxiterate 1000 --reorder --thread $NUM_THREADS --quiet --localpair $IN > $OUT
done
