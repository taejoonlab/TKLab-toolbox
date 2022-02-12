#!/usr/bin/env python3
import gzip
import sys

filename_peak_xls = sys.argv[1]
#filename_gff3 = '/home/taejoon/git/amphibase-xentro9/init/xenTro9_XB2021-04-16.ucsc.gff3.gz'
filename_gff3 = 'xenTro9_XB2021-04-16.ucsc.L123.gff3.gz'

#chr	start	end	length	abs_summit	pileup	-log10(pvalue)	fold_enrichment	-log10(qvalue)	name
#GL172637.1	1924	2271	348	2117	29	10.3239	3.85564	8.7589	Pelzer2021_XENTRstx.day0_peak_1

peak_list = dict()
f_xls = open(filename_peak_xls, 'r')
for line in f_xls:
    if line.startswith('#'):
        continue
    tokens = line.strip().split("\t")
    if tokens[0] == '' or tokens[0] == 'chr':
        continue
    seq_id = tokens[0]
    peak_start = int(tokens[1])
    peak_end = int(tokens[2])
    peak_summit = int(tokens[4])
    peak_pileup = int(tokens[5])
    peak_id = tokens[9]
    if seq_id not in peak_list:
        peak_list[seq_id] = dict()
    peak_list[seq_id][peak_id] = {'start': peak_start, 'end': peak_end, 'summit': peak_summit, 'pileup': peak_pileup}
f_xls.close()

gene_list = dict()
f_gff3 = gzip.open(filename_gff3, 'rt')
for line in f_gff3:
    if line.startswith('#'):
        continue
    tokens = line.strip().split("\t")
    seq_id = tokens[0]
    seq_type = tokens[2]
    if seq_type == 'gene':
        pos_start = int(tokens[3])
        pos_end = int(tokens[4])
        strand = tokens[6]
        gene_id = 'NA'
        gene_name = 'NA'
        for tmp in tokens[8].split(';'):   
            if tmp.startswith('ID='):
                gene_id = tmp.split('=')[1]
            #if tmp.startswith('Name='):
            if tmp.startswith('gene_name='):
                gene_name = tmp.split('=')[1]

        if seq_id not in gene_list:
            gene_list[seq_id] = dict()
        gene_list[seq_id]['%s|%s' % (gene_name, gene_id)] = {'start':pos_start, 'end': pos_end, 'strand': strand}
f_gff3.close()

for seq_id, seq_peaks in peak_list.items():
    if seq_id == 'chrM' or seq_id.startswith('chrUn'):
        continue

    for tmp_id, tmp_peak in seq_peaks.items():
        tmp_peak_summit = tmp_peak['summit']
        tmp_peak_pileup = tmp_peak['pileup']

        is_genic = 0
        nearest_gene = 'NA'
        nearest_gene_dist = 0
        for tmp_gene_id, tmp_gene in gene_list[seq_id].items():
            tmp_gene_start = tmp_gene['start']
            tmp_gene_end = tmp_gene['end']
            tmp_gene_strand = tmp_gene['strand']
            if tmp_gene_start < tmp_peak_summit and tmp_gene_end > tmp_peak_summit:
                is_genic = 1
            
            tmp_dist_start = abs(tmp_peak_summit - tmp_gene_start)
            tmp_dist_end = abs(tmp_peak_summit - tmp_gene_end)
            tmp_dist = min(tmp_dist_start, tmp_dist_end)
            if nearest_gene_dist == 0 or nearest_gene_dist > tmp_dist:
                nearest_gene_dist = tmp_dist
                nearest_gene = tmp_gene_id
        
        nearest_gene_start = gene_list[seq_id][nearest_gene]['start']
        nearest_gene_end = gene_list[seq_id][nearest_gene]['end']
        print(seq_id, tmp_id, tmp_peak_summit, tmp_peak_pileup, is_genic, nearest_gene, nearest_gene_start, nearest_gene_end, nearest_gene_dist)

