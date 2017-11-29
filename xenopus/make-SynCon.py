#!/usr/bin/env python
import os
import sys
import gzip

#Qid	QLen	Tid	TLen	AlignLen	Mismatches	GapOpens	BitScore	Evalue
#3.S|Xelaev18036905m	571	Xelaev18034619m|Xelaev18034619m	1308	573	31	1	1043.0	0.00e+00

best_list = dict()
f_best = open('XENLA_JGIv18pV4_prot.XENLA_JGIv18pV4_prot.bp+_tbl_best','r')
for line in f_best:
    if line.startswith('#'):
        continue
    tokens = line.strip().split("\t")
    q_id = tokens[0]
    t_id = tokens[2]
    best_list[q_id] = t_id
f_best.close()

gene_pos = dict()
chr_gene_list = dict()
#Scaffold100	XENLA_JGIv91_dna_final	gene	41820	54989	.	-	.	ID=unnamed|Xelaev18000001m.path1;Name=unnamed|Xelaev18000001m
f_gff = gzip.open('/home/taejoon/xenopus.annot/XENLA_JGIv18/XENLA_JGIv18pV4_cdna.XENLA_GCA001663975v1.gmap.gff3.gz','rt')
for line in f_gff:
    if line.startswith('#'):
        continue
    tokens = line.strip().split("\t")
    chr_id = tokens[0]
    tmp_type = tokens[2]
    tmp_pos = int(tokens[3])
    if tmp_type != 'gene':
        continue
    tmp_id = tokens[8].split(';')[0].split('.')[0].replace('ID=','')
    gene_pos[tmp_id] = {'chr':chr_id,'pos':tmp_pos}
    if not chr_id in chr_gene_list:
        chr_gene_list[chr_id] = dict()
    chr_gene_list[chr_id][tmp_id] = tmp_pos
f_gff.close()

sorted_gene_list = dict()
for tmp_chr_id in sorted(chr_gene_list.keys()):
    sorted_gene_list[tmp_chr_id] = sorted(chr_gene_list[tmp_chr_id].keys(), key=chr_gene_list[tmp_chr_id].get)

for tmp_chr_id in sorted(chr_gene_list.keys()):
    for tmp_gene in chr_gene_list
    print(tmp_chr_id)
