#!/usr/bin/env python3
import sys
from scipy.stats import hypergeom

filename_annot_freq = sys.argv[1]
#filename_annot_freq = '~/git/TKLab-toolbox/hyperG/odb9/vertebrata_7742_OrthoDB9_orthogroup_info.IPR_freq'
filename_query_list = sys.argv[2]

gene_list = []
term_dict = dict()

#GO:0000012	4	EOG090B01WZ;EOG090B0301;EOG090B042S;EOG090B08Q5
f_annot = open(filename_annot_freq, 'r')
for line in f_annot:
    tokens = line.strip().split("\t")
    term_id = tokens[0]
    
    if term_id not in term_dict:
        term_dict[term_id] = []

    for tmp_gene_id in tokens[2].split(';'):
        gene_list.append(tmp_gene_id)
        term_dict[term_id].append(tmp_gene_id)
f_annot.close()

query_list = []
f_query = open(filename_query_list, 'r')
for line in f_query:
    query_list.append(line.strip())
f_query.close()

count_total = len(set(gene_list))
query_set = set(query_list)
count_query = len(query_set)

sys.stderr.write('Total DB genes: %d\n' % count_total)
sys.stderr.write('Total query genes: %d\n' % count_query)

for term_id in sorted(term_dict.keys()):
    term_set = set(term_dict[term_id])
    overlap_set = query_set.intersection(term_set)
    count_term = len(term_set) 
    count_overlap = len(overlap_set)

    if count_overlap == 0:
        continue

    rv_hg = hypergeom(count_total, count_term, count_query)
    pmf_hg = rv_hg.pmf(count_overlap)
    print(term_id, count_total, count_term, count_query, count_overlap, pmf_hg)
