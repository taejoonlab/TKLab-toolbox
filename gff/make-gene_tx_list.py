#!/usr/bin/env python3
import os
import sys

## Prep code begins.
pre_py_name = 'extract-gff-by-mol_type.py'
usage_mesg = '\nUsage: %s <filename_gene_gff> <filename_mrna_gff>\n'%(sys.argv[0])
usage_mesg += '\t(Create <gene_gff> and <mrna_gff> with %s)\n\n'%(pre_py_name)

def print_usage_and_exit():
    sys.stderr.write(usage_mesg)
    sys.exit(1)

if len(sys.argv) != 3:
    print_usage_and_exit()

filename_gene_gff = sys.argv[1]
filename_mrna_gff = sys.argv[2]

for tmp_in_file in [filename_gene_gff, filename_mrna_gff]:
    if not os.access(tmp_in_file, os.R_OK):
        sys.stderr.write('%s is not available.\n'%tmp_in_file)
        print_usage_and_exit()
### Prep code ends.

gene_list = dict()
f_gene = open(filename_gene_gff, 'r')
for line in f_gene:
    if line. startswith('#'):
        continue
    tokens = line.strip().split("\t")

    tmp_id = ''
    tmp_name = 'NA'
    tmp_biotype = 'NA'
    tmp_attr = tokens[8]
    for tmp in tmp_attr.split(';'):
        (tmp_k, tmp_v) = tmp.split('=')
        if tmp_k == 'ID':
            tmp_id = tmp_v
        elif tmp_k == 'Name':
            tmp_name = tmp_v
        elif tmp_k == 'gene_biotype':
            tmp_biotype = tmp_v
    
    gene_list[tmp_id] = {'name':tmp_name, 'biotype':tmp_biotype, 'mrna_list':[]}
f_gene.close()

f_mrna = open(filename_mrna_gff,'r')
for line in f_mrna:
    if line. startswith('#'):
        continue
    tokens = line.strip().split("\t")

    tmp_id = ''
    tmp_parent = 'NA'
    tmp_attr = tokens[8]
    for tmp in tmp_attr.split(';'):
        (tmp_k, tmp_v) = tmp.split('=')
        if tmp_k == 'ID':
            tmp_id = tmp_v
        elif tmp_k == 'Parent':
            tmp_parent = tmp_v
    
    if not tmp_parent in gene_list:
        sys.stderr.write('No parent: %s\n'%tmp_parent)
        sys.exit(1)
    
    gene_list[tmp_parent]['mrna_list'].append(tmp_id)
f_mrna.close()

for tmp_g in sorted(gene_list.keys()):
    tmp = gene_list[tmp_g]
    print("%s\t%s\t%s\t%s"%(tmp_g, tmp['biotype'], tmp['name'], ';'.join(tmp['mrna_list'])))
