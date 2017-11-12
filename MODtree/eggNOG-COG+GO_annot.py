#!/usr/bin/env python3
import os
import sys
import re
import json
import gzip

q_OG_type = 'veNOG'

filename_tsv_gz = 'all_OG_annotations.tsv.gz'
#filename_tsv_gz = 'veNOG.annot2.tsv.gz'

sys.stderr.write('Query: %s, Source: %s\n'%(q_OG_type, filename_tsv_gz))

GO_short_category = {'Molecular Function':'GO_MF', 'Biological Process':'GO_BP',\
                     'Cellular Component':'GO_CC'}

re_u = re.compile(r"u'([A-Z])'")

GO_desc = dict()

f_COG = open('%s.COG_annot.txt'%q_OG_type,'w')
f_GO = open('%s.GO_annot.txt'%q_OG_type,'w')

count_COG = 0
count_GO = 0
f_tsv = gzip.open(filename_tsv_gz,'rt')
for line in f_tsv:
    tokens = line.strip().split("\t")

    OG_id = tokens[0]
    OG_id_full = 'ENOG41%s'%OG_id
    OG_name = tokens[3]

    OG_type = tokens[1]
    if OG_type != q_OG_type:
        continue

    for tmp in re.findall(re_u, tokens[4]):
        f_COG.write("%s\tCOG\t%s\n"%(OG_id_full,tmp))
        count_COG += 1
    
    GO_items = json.loads(tokens[5])
    for tmp_category in GO_items.keys():
        tmp_cname = GO_short_category[tmp_category]
        for tmp_item in GO_items[tmp_category]:
            tmp_GO_id = tmp_item[0]
            tmp_GO_desc = tmp_item[1]
            if not tmp_GO_id in GO_desc:
                GO_desc[tmp_GO_id] = '%s\t%s'%(tmp_cname, tmp_GO_desc)
            tmp_GO_evidence = tmp_item[2]
            tmp_GO_str = '%s\t%s'%(tmp_GO_id, tmp_GO_evidence)
            f_GO.write("%s\t%s\t%s\n"%(OG_id_full, tmp_cname, tmp_GO_str))
            count_GO += 1
f_tsv.close()

f_COG.close()
f_GO.close()

sys.stderr.write('COG: %d, GO: %d\n'%(count_COG, count_GO))
f_GO_desc = open('%s.GO_desc.txt'%q_OG_type,'w')
for tmp_GO_id in sorted(GO_desc.keys()):
    f_GO_desc.write('%s\t%s\n'%(tmp_GO_id, GO_desc[tmp_GO_id]))
f_GO_desc.close()
    
