#!/bin/bash

#UBAM="DSMC202003_HUMANg_OvC-P01_Blood.ubam"
UBAM="DSMC202003_HUMANg_OvC-P01_Organoid.ubam"

MARKED_BAM=${UBAM/.ubam/.marked_ubam}
MARKED_METRICS=${UBAM/.ubam/.marked_ubam}".matrics.txt"

picard MarkIlluminaAdapters TMP_DIR=/work/taejoon/tmp \
  I=$UBAM O=$MARKED_BAM M=$MARKED_METRICS
