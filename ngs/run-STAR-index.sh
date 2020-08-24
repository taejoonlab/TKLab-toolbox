!/bin/bash

NUM_THREADS=16

# Install STAR using conda
# $ conda install -c bioconda STAR

DB_FASTA="XENLA_dna.GCA001663975v1+.fa"

$STAR --runThreadN $NUM_THREADS --runMode genomeGenerate --genomeDir db.star \
  --genomeFastaFiles $DB_FASTA
