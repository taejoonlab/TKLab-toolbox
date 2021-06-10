#!/bin/bash

VERSION=38
URL_DIR="ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_"$VERSION"/"
GENCODE_PREFIX="gencode.v"$VERSION

wget $URL_DIR/$GENCODE_PREFIX".annotation.gff3.gz"
wget $URL_DIR/$GENCODE_PREFIX".primary_assembly.annotation.gff3.gz"
wget $URL_DIR/$GENCODE_PREFIX".primary_assembly.annotation.gtf.gz"

wget $URL_DIR/$GENCODE_PREFIX".transcripts.fa.gz"
wget $URL_DIR/$GENCODE_PREFIX".pc_translations.fa.gz"
