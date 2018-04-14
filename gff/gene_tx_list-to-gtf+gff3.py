#!/usr/bin/env python3
import os
import sys

## Prep code begins.
pre_py_code = 'make-gene_tx_list.py'
usage_mesg = '\nUsage: %s <filename_raw_gff> <gene_tx_list>\n'%(sys.argv[0])
usage_mesg += '\t(you can create <gene_tx_list> with %s)\n\n'%(pre_py_code)

def print_usage_and_exit():
    sys.stderr.write(usage_mesg)
    sys.exit(1)

if len(sys.argv) != 3:
    print_usage_and_exit()

filename_raw_gff = sys.argv[1]
filename_gene_tx_list = sys.argv[2]

for tmp_in_file in [filename_raw_gff, filename_gene_tx_list]:
    if not os.access(tmp_in_file, os.R_OK):
        sys.stderr.write('%s is not available.\n'%tmp_in_file)
        print_usage_and_exit()
### Prep code ends.

gene_info = dict()
mrna_info = dict()
exon_info = dict()
f_list = open(filename_gene_tx_list,'r')
for line in f_list:
    tokens = line.strip().split("\t")
    if len(tokens) < 4:
        continue

    gene_id = tokens[0]
    biotype = tokens[1]
    if biotype != 'protein_coding':
        continue

    gene_name = tokens[2]
    gene_id_name = '%s|%s'%(gene_id, gene_name)

    gene_info[ gene_id ] = 'ID=%s;Name=%s'%(gene_id_name, gene_name)

    for mrna_id in tokens[3].split(';'):
        mrna_id_name = '%s|%s'%(mrna_id, gene_name)
        mrna_info[ mrna_id ] = 'ID=%s;Parent=%s;Name=%s'%\
                                (mrna_id_name, gene_id_name, gene_name)
        exon_info[ mrna_id ] = 'Parent=%s;gene_id=%s;transcript_id=%s'%\
                                (mrna_id_name, gene_id_name, mrna_id_name)
f_list.close()

f_gff = open(filename_raw_gff,'r')
if filename_raw_gff.endswith('.gz'):
    import gzip
    f_gff = gzip.open(filename_raw_gff,'rt')

for line in f_gff:
    if line.startswith('#'):
        print(line.strip())
        continue

    tokens = line.strip().split("\t")
    tmp_biotype = tokens[2]
    tmp_record = '\t'.join(tokens[:8])

    tmp_id = ''
    tmp_parent = ''
    for tmp in tokens[8].split(';'):
        (tmp_k, tmp_v) = tmp.split('=')
        if tmp_k == 'ID':
            tmp_id = tmp_v
        if tmp_k == 'Parent':
            tmp_parent = tmp_v

    if tmp_biotype == 'gene':
        if tmp_id in gene_info:
            print('%s\t%s'%(tmp_record, gene_info[tmp_id]))
    if tmp_biotype == 'mRNA':
        if tmp_id in mrna_info:
            print('%s\t%s'%(tmp_record, mrna_info[tmp_id]))
    if tmp_biotype == 'exon':
        if tmp_parent in mrna_info:
            print('%s\tID=%s;%s'%(tmp_record, tmp_id, exon_info[tmp_parent]))
        #else:
        #    sys.stderr.write('Error: %s\n'%line.strip())
f_gff.close()
