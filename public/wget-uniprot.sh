#!/bin/bash

wget ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/relnotes.txt
wget https://www.uniprot.org/docs/speclist

SRC_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REF_LIST=$SRC_DIR"/uniprot_references.txt"

if [ ! -e $REF_LIST ]; then
  echo "Not available: Uniprot Ref Proteome List"
  echo "Current setting: "$REF_LIST

else

  for UP_ID in $(awk '{print $2}' $REF_LIST)
  do
    echo $UP_ID
    wget ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/$UP_ID".fasta.gz"
    wget ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/$UP_ID"_DNA.fasta.gz"
    wget ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/$UP_ID".gene2acc.gz"
    wget ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/$UP_ID".idmapping.gz"
  done
fi

