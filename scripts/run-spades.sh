#!/bin/bash

BC="NGCTGAGT"
spades.py --phred-offset auto -o $BC -1 ../BC/5068-JG-0006_S1_L001_R1_001.$BC.fastq.gz -2 ../BC/5068-JG-0006_S1_L001_R2_001.$BC.fastq.gz
