#!/bin/bash

# install kallisto first via conda
# $ conda install -c bioconda kallisto

IDX="$HOME/pub/GENCODE/MOUSEm26/gencode.vM26.transcripts.concise.kallisto_idx"
IDX_NAME=$(basename $IDX)
IDX_NAME=${IDX_NAME/.kallisto_idx/}

NUM_THREADS=8
DIR_FQ="../fastq/"

for FQ1 in $(ls $DIR_FQ/*fq)
do
  OUT=$(basename $FQ1)
  OUT=${OUT/_trim.fq/}"."$IDX_NAME".kallisto_quant"

  echo "FASTQ:" $FQ1 

  if [ -d $OUT ]; then
    echo "$OUT exists. Skip."
  else
    echo "Run $OUT"
    FRAGMENT_LEN=200
    FRAGMENT_LEN_SD=0.1

    kallisto quant --single -l $FRAGMENT_LEN -s $FRAGMENT_LEN_SD \
                   -t $NUM_THREADS -i $IDX -o $OUT $FQ1
  fi
done
