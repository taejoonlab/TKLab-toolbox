#!/bin/bash
for DIR in $(ls -d */)
do
  echo $DIR
  CLOUPE_IN=$DIR"count/cloupe.cloupe"
  CLOUPE_OUT=$(basename $DIR)".cloupe"
  echo $CLOUPE_IN $CLOUPE_OUT
  cp $CLOUPE_IN $CLOUPE_OUT
done
#XtSCIday0/count/cloupe.cloupe
#XtSCIday1/count/cloupe.cloupe
#XtSCIday3/count/cloupe.cloupe
#XtSCIday5/count/cloupe.cloupe
