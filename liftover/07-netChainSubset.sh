#!/bin/bash
NET_CHAIN_SUBSET="$HOME/miniconda3/bin/netChainSubset"

OLD_NAME="JGIv91_lt10k"
NEW_NAME="XENLA_GCA001663975v1"
OVER_OUT="XENLA_dna."$OLD_NAME"-"$NEW_NAME".chain"

DIR_CHAIN_IN="chain."$OLD_NAME
DIR_NET_IN="net."$OLD_NAME
DIR_CHAIN_OUT="liftOver."$OLD_NAME"-"$NEW_NAME

if [ ! -d $DIR_CHAIN_OUT ]; then
  echo "Make $DIR_CHAIN_OUT"
  mkdir $DIR_CHAIN_OUT
fi

for NET_IN in $(ls $DIR_NET_IN/*.net)
do
  BASE_NAME=$(basename $NET_IN)
  BASE_NAME=${BASE_NAME/.net/}

  CHAIN_IN=$DIR_CHAIN_IN/$BASE_NAME".chain"
  CHAIN_OUT=$DIR_CHAIN_OUT/$BASE_NAME".chain"
  $NET_CHAIN_SUBSET $NET_IN $CHAIN_IN $CHAIN_OUT
done

cat $DIR_CHAIN_OUT/*chain > $OVER_OUT
