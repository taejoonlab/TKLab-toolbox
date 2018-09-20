#!/bin/bash

NUM_THREADS=6

## Config file
## You can see the list of available configs at:
## http://porecamp.github.io/2017/basecalling.html
## or run 'read_fast5_basecaller.py -l'
##
## For example, if you use FLO-MIN106 flow cell, and
## SQK-LSK108 kit for library construction, 
## set 'r94_450bps_linear.cfg' as below.
##
#flowcell    kit         barcoding  config file
#FLO-MIN106  SQK-LSK108             r94_450bps_linear.cfg

CONFIG="r94_450bps_linear.cfg"

INPUT_DIR="fast5"
OUTPUT_DIR="called"

if [ ! -e $OUTPUT_DIR ]; then
  mkdir $OUTPUT_DIR
fi

read_fast5_basecaller.py -i $INPUT_DIR -r -t $NUM_THREADS \
				-s $OUTPUT_DIR -o fastq,fast5 -c $CONFIG
