#!/bin/bash

## Index info
#/RunParameters.xml:  <CustomIndexPrimer>BP14</CustomIndexPrimer>

#ID="scCapSt27"
#INPUT_DIR="./181121_NB501779_0090_AHWYLVBGX7"

# If you don't know the barcode index, run 'cellranger mkfastq' with arbitrary barcode index first.
# Then, look at the any of following files under <sampleID>/outs/fastq_path/Stats directory.
#  - ConversionStats.xml
#  - DemuxSummaryFIL?.txt
#  - Stats.json
# You can find the most abundant "undetermined" barcode sequence. 
# Search the 10x/*csv file with that undetermiend barcode sequence, 
# then you will see what your barcode index is.

ID="LP202112_multi2"
CSV="LP202112_multi2.CMO.csv"

$HOME/src/10X/cellranger-6.1.2/cellranger multi --id=$ID --csv=$CSV
