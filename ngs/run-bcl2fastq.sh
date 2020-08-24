#!/bin/bash

# See http://sapac.support.illumina.com/downloads/bcl2fastq-conversion-software-v2-20.html

# Install bcl2fastq2 as below:

# Download bcl2fastq2 Linux RPM.
# $ wget http://sapac.support.illumina.com/content/dam/illumina-support/documents/downloads/software/bcl2fastq/bcl2fastq2-v2-20-0-linux-x86-64.zip

# Install the following packages: unzip & alien
# $ sudo apt-get install unzip alien

# Convert .rpm to .deb using alien, and install .deb with dpkg.
# $ unzip bcl2fastq2-v2-20-0-linux-x86-64.zip
# $ sudo alien bcl2fastq2-v2.20.0.422-Linux-x86_64.rpm
# $ sudo dpkg -i ./bcl2fastq2_0v2.20.0.422-2_amd64.deb

RUN_DIR="DIR_FROM_MACHINE"
OUT_DIR="DIR_OUTPUT"
SAMPLE_SHEET="SampleSheet.csv"

bcl2fastq --runfolder-dir $RUN_DIR --output-dir $OUT_DIR --sample-sheet $SAMPLE_SHEET --barcode-mismatch 1
