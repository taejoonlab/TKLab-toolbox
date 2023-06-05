#!/bin/bash

for FQ_IN in $(ls *.raw.fastq.gz)
do
  FQ_OUT=${FQ_IN/.raw.fastq.gz/}".trim.fastq.gz"

  fastp -i $FQ_IN -o $FQ_OUT

  LOG_JSON=${FQ_IN/.raw.fastq.gz/}".fastp.json"
  mv fastp.json  $LOG_JSON

  LOG_HTML=${LOG_JSON/.json/}".html"
  mv fastp.html $LOG_HTML
done
