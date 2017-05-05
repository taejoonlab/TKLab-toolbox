#!/bin/bash
AXT_CHAIN="$HOME/miniconda3/bin/axtChain"

## Make 2bit file by faToTwoBit
NEW_2BIT="../XENLA_dna.GCA001663975v1+.2bit"

OLD_2BIT="$HOME/xenopus.genome/XENLA_JGIv72/XENLA_dna.JGIv7b_lt10k.2bit"
DIR_PSL="gmap.JGIv7b_lt10k"

#OLD_2BIT="../../XENLA_JGIv91/XENLA_dna.JGIv91_lt10k.2bit"
#DIR_PSL="gmap.JGIv91_lt10k"

IN_SUFFIX=".gmap.liftUp.psl"
OUT_SUFFIX=".gmap.chain"

for PSL in $(ls $DIR_PSL/*$IN_SUFFIX)
do
  OUT_CHAIN=${PSL/$IN_SUFFIX/}$OUT_SUFFIX
  echo $OUT_CHAIN
  $AXT_CHAIN -linearGap=medium -psl $PSL $OLD_2BIT $NEW_2BIT $OUT_CHAIN
done
