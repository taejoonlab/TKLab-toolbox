#!/bin/bash

## If the genome is fragmented (many scaffolds), you may need to increase
## the number of opened files by ulimit
ulimit -n 30000

CHAIN_MS="$HOME/miniconda3/bin/chainMergeSort"
CHAIN_S="$HOME/miniconda3/bin/chainSplit"

#DIR_CHAIN_IN="gmap.JGIv72_lt10k"
DIR_CHAIN_IN="gmap.JGIv91_lt10k"

DIR_CHAIN_OUT=${DIR_CHAIN_IN/gmap/chain}
if [ ! -d $DIR_CHAIN_OUT ]; then
  echo "Make $DIR_CHAIN_OUT"
  mkdir $DIR_CHAIN_OUT
fi

$CHAIN_MS $DIR_CHAIN_IN/*chain | $CHAIN_S $DIR_CHAIN_OUT stdin
