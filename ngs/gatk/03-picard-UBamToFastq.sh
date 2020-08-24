#!/bin/bash

MARKED_UBAM=$1

FQ=${UBAM/.marked_ubam/}".i_marked.fastq"

echo $UBAM $FQ
picard SamToFastq -Xmx8g I=$UBAM FASTQ=$FQ CLIPPING_ATTRIBUTE=XT CLIPPING_ACTION=2 INTERLEAVE=true NON_PF=true TMP_DIR=$HOME/tmp
