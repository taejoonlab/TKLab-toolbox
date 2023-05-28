#!/bin/bash

FQ1_IN="Ueno201210_XENLA_liver_R1.raw.fastq.gz"
#FQ1_IN="Taira201203_XENLA_liver_R1.raw.fastq.gz"
#FQ1_IN="Ueno201210_XENLA_egg_R1.raw.fastq.gz"
#FQ1_IN="PRJNA318484_XENBOtx_SRR3383209_R1.raw.fastq.gz"

FQ2_IN=${FQ1_IN/_R1.raw.fastq.gz/}"_R2.raw.fastq.gz"

FQ1_OUT=${FQ1_IN/.raw.fastq.gz/}".trim.fastq.gz"
FQ2_OUT=${FQ2_IN/.raw.fastq.gz/}".trim.fastq.gz"

fastp -i $FQ1_IN -I $FQ2_IN -o $FQ1_OUT -O $FQ2_OUT

LOG_JSON=${FQ1_IN/_R1.raw.fastq.gz/}".fastp.json"
mv fastp.json  $LOG_JSON

LOG_HTML=${FQ1_IN/_R1.raw.fastq.gz/}".fastp.html"
mv fastp.html $LOG_HTML
