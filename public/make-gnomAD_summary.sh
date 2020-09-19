#!/bin/bash

# FILTER flags for gnomADv3
# AC0: The allele count is zero after filtering out low-confidence genotypes (GQ < 20; DP < 10; and AB < 0.2 for het calls)
# AS-VQSR (gnomAD v3 only): Failed GATK Allele-Specific Variant Quality Recalibration (AS-VQSR)
# InbreedingCoeff: The Inbreeding Coefficient is < -0.3

for VCF_BGZ in $(ls *vcf.bgz)
do
  OUT=${VCF_BGZ/.vcf.bgz/}".vcf_summary"
  echo $OUT
  zcat $VCF_BGZ | grep -v ^# | awk -F"\t" '{ if( $7 == "PASS" ) print $1"\t"$2"\t"$3"\t"$4"\t"$5"\t"$6"\t"$7}' > $OUT
done
