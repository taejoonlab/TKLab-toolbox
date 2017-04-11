#!/usr/bin/env python3
import os
import sys
import gzip
from MODtree import *

#filename_tsv = '/work/project/pub/eggNOG/v45/euNOG.members.tsv'
#filename_tsv = '/work/project/pub/eggNOG/v45/biNOG.members.tsv'
#filename_tsv = '/work/project/pub/eggNOG/v45/veNOG.members.tsv'

filename_tsv = sys.argv[1]

tax2sp = get_tax2sp()
HS_names = get_HS_prot2names()

#==> /work/project/pub/eggNOG/v45/biNOG.members.tsv <==
#biNOG	ENOG410A4PM	4	4	G	31033.ENSTRUP00000020495,8083.ENSXMAP00000002012,69293.ENSGACP00000002809,99883.ENSTNIP00000006575
print( "#MODtreeID\tCountSpecies\tCountProt\tSpeciesList\tProtList")
f_tsv = open(filename_tsv,'r')
for line in f_tsv:
    tokens = line.strip().split("\t")
    family_id = '%s.%s'%(tokens[0],tokens[1])

    tmp_HS_name = 'NA'
    member_list = []
    sp_code_list = []
    for tmp_id in tokens[5].split(','):
        tmp_tax_id = tmp_id.split('.')[0]
        tmp_prot_id = '.'.join(tmp_id.split('.')[1:])
        if tmp_prot_id in HS_names:
            tmp_HS_name = HS_names[tmp_prot_id]
        if tmp_tax_id in tax2sp:
            member_list.append(tmp_id)
            sp_code_list.append(tax2sp[tmp_tax_id])

    len_member_list = len(member_list)
    sp_code_list = sorted(list(set(sp_code_list)))
    len_sp_code_list = len(sp_code_list)
    if len_member_list < 2 or len_sp_code_list < 2:
        continue

    str_member_list = ','.join(sorted(member_list))
    str_sp_code_list = ','.join(sp_code_list)

    print( "%s.%s\t%d\t%d\t%s\t%s"%(family_id, tmp_HS_name,\
            len_sp_code_list, len_member_list,\
            str_sp_code_list, str_member_list) )
f_tsv.close()
