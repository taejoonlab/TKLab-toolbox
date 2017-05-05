#!/bin/bash
CHAIN_NET="$HOME/miniconda3/bin/chainNet"

SIZE_NEW="../XENLA_dna.GCA001663975v1+.seqlen"
SIZE_OLD="../../XENLA_JGIv91/XENLA_dna.JGIv91_lt10k.seqlen"

DIR_CHAIN_IN="chain.JGIv91_lt10k"
DIR_NET_OUT="net.JGIv91_lt10k"

if [ ! -d $DIR_NET_OUT ]; then
  echo "Make $DIR_NET_OUT"
  mkdir $DIR_NET_OUT
fi

for CHAIN_IN in $(ls $DIR_CHAIN_IN/*chain)
do
  echo $CHAIN_IN
  NET_OUT=$(basename $CHAIN_IN)
  NET_OUT=${NET_OUT/.chain/}".net"
  #echo $NET_OUT
  $CHAIN_NET $CHAIN_IN $SIZE_OLD $SIZE_NEW $DIR_NET_OUT/$NET_OUT /dev/null
done
