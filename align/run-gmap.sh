#!/bin/bash

# Install GMAP using conda
# $ conda install -c bioconda gmap

# Make GMAP database with gmap_build
# $ gmap_build -d $DBNAME -D $GMAPDB $DB_FASTA

GMAPDB="path/to/db.gmap/"
NUM_THREADS=1

FA="<my fasta file>"
DBNAME="<db index name>"

OUT=${FA/.fa/}"."$DB".gmap_psl"
time gmap -f psl -t $NUM_THREADS -D $GMAPDB -d $DB $FA > $OUT

# for GFF output
# time gmap -f gff3_gene -t $NUM_THREADS -D $GMAPDB -d $DB $FA > $OUT
