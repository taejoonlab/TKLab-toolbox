#!/bin/bash

# curl -O ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/relnotes.txt
# curl -O https://www.uniprot.org/docs/speclist

SRC_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REF_LIST=$SRC_DIR"/uniprot_references.txt"

if [ ! -e $REF_LIST ]; then
  echo "Not available: UNIPROT Ref Proteome List"
  echo "Current setting: "$REF_LIST

else
  for UP_TAX_ID in $(awk '{print $1"_"$2}' $REF_LIST | grep -v ^#)
  do
    UP_ID=$(echo $UP_TAX_ID | awk -F"_" '{print $1}')
    UP_DIR="ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/"$UP_ID
    
    #echo $UP_ID $UP_TAX_ID
    echo $UP_DIR
    curl -O $UP_DIR/$UP_TAX_ID".fasta.gz"
    curl -O $UP_DIR/$UP_TAX_ID"_DNA.fasta.gz"
    curl -O $UP_DIR/$UP_TAX_ID".gene2acc.gz"
    curl -O $UP_DIR/$UP_TAX_ID".idmapping.gz"
  done
fi
