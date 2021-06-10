#!/bin/bash
for VCF in $(ls *chr?.vcf.bgz)
do
  EAS=$VCF".EAS"
  if [ -e $EAS ]; then 
    echo "Skip "$EAS
  else
    echo "Make "$EAS
    ./filter-gnomAD_EAS.py $VCF
  fi
done
