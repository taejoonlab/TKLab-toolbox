#!/bin/bash
BLAT="$HOME/src/ucsc/blat/blat"
#DB="../xenTro2.fa"
DB="../xenTro3.fa"

DB_NAME=$(basename $DB)
DB_NAME=${DB_NAME/.fa/}
for FA in $(ls split/*fa)
do
  OUT=$(basename $FA)
  OUT=${OUT/.fa/}
  OUT="blat.xenTro3/"$OUT"."$DB_NAME".blat_psl"
  LOG=$OUT".log"
  nohup $BLAT $DB $FA $OUT -tileSize=12 -minScore=100 -minIdentity=98 -fastMap &>$LOG &
done
