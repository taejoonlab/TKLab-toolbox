#!/usr/bin/env python3
import os
import sys
import gzip
from MODtree import *

dirname_aa_fa = sys.argv[1]

sp_info = get_sp_info()
HS_names = get_HS_prot2names()
names = get_prot2names()

tf_list = dict()
for filename_fa in os.listdir(dirname_aa_fa):
    tf_id = filename_fa.split('.')[0]
    tf_list[tf_id] = {'sp_list':[], 'prot_list':[]}
    f = open(os.path.join(dirname_aa_fa,filename_fa),'r')
    for line in f:
        if line.startswith('>'):
            tmp_prot_id = line.strip().lstrip('>')
            if tmp_prot_id in names:
                tmp_species = names[tmp_prot_id]['species']
                tmp_gene_name = names[tmp_prot_id]['name']
                if not tmp_species in sp_info:
                    continue
                new_prot_id = '%s.%s'%(sp_info[tmp_species]['tax_id'],tmp_prot_id)
                tf_list[tf_id]['sp_list'].append(sp_info[tmp_species]['sp_code'])
                tf_list[tf_id]['prot_list'].append(new_prot_id)
    f.close()

print( "#MODtreeID\tCountSpecies\tCountProt\tSpeciesList\tProtList")
for tmp_tf_id in sorted(tf_list.keys()):
    tmp_sp_list = sorted(list(set(tf_list[tmp_tf_id]['sp_list'])))
    tmp_prot_list = sorted(list(set(tf_list[tmp_tf_id]['prot_list'])))
    sp_count = len(tmp_sp_list)
    prot_count = len(tmp_prot_list)
    str_sp_list = ','.join(tmp_sp_list)
    str_prot_list = ','.join(tmp_prot_list)
    tmp_HS_name = 'NA'
    for tmp_prot_id in ['.'.join(x.split('.')[1:]) for x in tmp_prot_list]:
        if tmp_prot_id in HS_names:
            tmp_HS_name = HS_names[tmp_prot_id]
    
    if sp_count < 2 or prot_count < 2:
        continue

    print( "%s.%s\t%d\t%d\t%s\t%s"%(tmp_tf_id, tmp_HS_name, sp_count, prot_count,\
            str_sp_list, str_prot_list) )
