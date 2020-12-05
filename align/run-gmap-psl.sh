#!/bin/bash

# Install GMAP using conda
# $ conda install -c bioconda gmap

GMAPDB="path/to/db.gmap/"
NUM_THREADS=1

FA="<my fasta file>"
DB="<db index name>""

OUT=${FA/.fa/}"."$DB".gmap_psl"
time gmap -f psl -t $NUM_THREADS -D $GMAPDB -d $DB $FA > $OUT
