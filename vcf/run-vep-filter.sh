#!/bin/bash

for IN in $(ls /opt/vep/.vep/output/*vep.vcf)
do
    OUT=${IN/output/output\/filter}
    OUT=${OUT/.vcf/}".HIGH+MODERATE.vcf"
    echo $IN $OUT
    ./filter_vep -i $IN -o $OUT \
    	     -filter "IMPACT is HIGH or IMPACT is MODERATE" --force_overwrite
done
