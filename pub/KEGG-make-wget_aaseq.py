#!/usr/bin/env python
import os
import sys

## A file containing all genes in a species
## using http://rest.kegg.jp/list/hsa

filename_genes = sys.argv[1]

gene_list = []
f_genes = open(filename_genes,'r')
for line in f_genes:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    species_code = tokens[0][:3]
    for tmp in tokens[2].split(';;'):
        gene_list.append( '%s:%s'%(species_code,tmp) )
f_genes.close()

for tmp in sorted(list(set(gene_list))):
    print "wget http://rest.kegg.jp/get/%s/aaseq"%(tmp)
