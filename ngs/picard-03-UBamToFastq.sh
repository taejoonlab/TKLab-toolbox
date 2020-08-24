#!/bin/bash

#UBAM="DSMC202003_HUMANg_OvC-P01_Blood.marked_ubam"
UBAM="DSMC202003_HUMANg_OvC-P01_Organoid.marked_ubam"

FQ=${UBAM/.marked_ubam/}".i_marked.fastq"

echo $UBAM $FQ
picard SamToFastq -Xmx8g I=$UBAM FASTQ=$FQ CLIPPING_ATTRIBUTE=XT CLIPPING_ACTION=2 INTERLEAVE=true NON_PF=true TMP_DIR="/work/taejoon/tmp"
