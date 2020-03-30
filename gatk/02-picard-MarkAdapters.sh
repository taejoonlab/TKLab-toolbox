#!/bin/bash

UBAM=$1

MARKED_BAM=${UBAM/.ubam/.marked_ubam}
MARKED_METRICS=${UBAM/.ubam/.marked_ubam}".matrics.txt"

picard MarkIlluminaAdapters TMP_DIR=$HOME/tmp \
  I=$UBAM O=$MARKED_BAM M=$MARKED_METRICS
