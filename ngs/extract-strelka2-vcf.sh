#!/bin/bash

SAMPLE=$1

for VCF in $(ls *$SAMPLE*/results/variants/variants.vcf.gz)
do
  DIR_NAME=$(echo $VCF | awk -F"/" '{print $1}')
  NEW=$DIR_NAME".variants.vcf.gz"
  echo "$VCF -> $NEW"
  cp $VCF $NEW
  zip -r $DIR_NAME".zip" $DIR_NAME
done
