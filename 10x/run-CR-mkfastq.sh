#!/bin/bash

## Index info
#/RunParameters.xml:  <CustomIndexPrimer>BP14</CustomIndexPrimer>

## St13
#INPUT_DIR="./181115_NB501779_0086_AHWYH7BGX7"
## St18
#ID="scCapSt18"
#INPUT_DIR="./181119_NB501779_0088_AHWYJ5BGX7"
## St24
#ID="scCapSt24"
#INPUT_DIR="./181120_NB501779_0089_AHWYJGBGX7"

## St27
ID="scCapSt27"
INPUT_DIR="./181121_NB501779_0090_AHWYLVBGX7"


~/src/10X/cellranger-2.1.1/cellranger mkfastq --id=$ID --run=$INPUT_DIR --csv="samplesheet-"$ID".csv"
