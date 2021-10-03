#!/bin/bash

# install kallisto first via conda
# $ conda install -c bioconda kallisto

IDX="RAT_ens100_tx_all.kallisto_idx"
IDX_NAME=${IDX/.kallisto_idx/}

NUM_THREADS=8
DIR_FQ="../fastq/"

for FQ1 in $(ls $DIR_FQ/*_trim_1P)
do
  FQ2=${FQ1/_1P/_2P}
  OUT=$(basename $FQ1)
  OUT=${OUT/_trim_1P/}"."$IDX_NAME".kallisto_quant"

  echo "FASTQ:" $FQ1 

  if [ -d $OUT ]; then
    echo "$OUT exists. Skip."
  else
    echo "Run $OUT"
    kallisto quant -t $NUM_THREADS -i $IDX -o $OUT $FQ1 $FQ2
  fi
done
