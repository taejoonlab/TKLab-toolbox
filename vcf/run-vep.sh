#!/bin/bash

for IN in $(ls /opt/vep/.vep/input/*vcf)
do
    OUT=${IN/input/output}
    OUT=$(echo $OUT | awk -F'_' '{print $1"_"$2"_"$3}')".germline_overlap.vcf"
    echo $IN 
    echo "-->" $OUT

./vep --cache --offline --format vcf --vcf --force_overwrite \
	--dir_cache /opt/vep/.vep/ \
	--dir_plugins /opt/vep/.vep/Plugins/ \
	--input_file $IN \
	--output_file $OUT
	#--input_file /opt/vep/.vep/input/my_input.vcf \
	#--output_file /opt/vep/.vep/output/my_output.vcf \
	#--custom /opt/vep/.vep/custom/my_extra_data.bed,BED_DATA,bed,exact,1 \
	#--plugin dbNSFP,/opt/vep/.vep/Plugins/dbNSFP.gz,ALL
done
