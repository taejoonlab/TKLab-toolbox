#!/bin/bash

BED_ANTITARGET="./refFlat.no_alt_fix.antitarget.bed"
BED_TARGET="./refFlat.no_alt_fix.target.bed"

for BAM in $(ls ../dragen.bam/*.bam)
do
    echo $BAM
    OUT_BASE=$(basename $BAM)
    OUT_BASE=${OUT_BASE/.bam/}
    COV_TARGET=$OUT_BASE".targetcoverage.cnn"
    COV_ANTITARGET=$OUT_BASE".antitargetcoverage.cnn"
    cnvkit coverage $BAM $BED_TARGET -o $COV_TARGET -p 4
    cnvkit coverage $BAM $BED_ANTITARGET -o $COV_ANTITARGET -p 4
done
