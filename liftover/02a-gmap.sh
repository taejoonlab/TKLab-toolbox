#!/bin/bash

#GMAP="$HOME/miniconda3/bin/gmap"
GMAP="$HOME/local/bin/gmap"

GMAPDB="/work/public/db.gmap/"
DB="XENLA_dna.JGIv7b_lt10k"
#DB="XENLA_dna.JGIv91_lt10k"

DB_NAME=$(basename $DB)
DB_VER=$(echo $DB_NAME | awk -F"." '{print $2}')

NUM_THREADS=32

for FA in $(ls split/*fa)
do
  OUT=$(basename $FA)
  OUT=${OUT/.fa/}
  OUT_DIR="gmap."$DB_VER
  if [ ! -d $OUT_DIR ]; then
    mkdir $OUT_DIR
  fi

  OUT="$OUT_DIR/"$OUT"."$DB_NAME".gmap.psl"
  LOG=$OUT".log"

  $GMAP -f psl -t $NUM_THREADS -D $GMAPDB -d $DB $FA > $OUT
done
