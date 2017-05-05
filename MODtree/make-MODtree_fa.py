#!/usr/bin/env python3
import os
import sys
import gzip
from MODtree import *

filename_MODtree_list = sys.argv[1]

dirname_ens = '/work/project/pub/ens/70/'
filename_names = 'ens70.prot2name'

prot_names = get_prot2names()
tax2sp = get_tax2sp()

seq_list = dict()
for filename in os.listdir(dirname_ens):
    if not filename.endswith('.pep.all.fa.gz'):
        continue
    sys.stderr.write('Read %s\n'%filename)
    f_fa = gzip.open(os.path.join(dirname_ens,filename),'rt')
    for line in f_fa:
        if line.startswith('>'):
            seq_h = line.strip().split()[0].lstrip('>')
            seq_list[seq_h] = []
        else:
            seq_list[seq_h].append(line.strip())
    f_fa.close()

#MODtreeID	CountSpecies	CountProt	SpeciesList	ProtList
#biNOG.ENOG410A4PF.PRDX5	6	6	ANOCA,DANRE,DROME,HUMAN,MOUSE,XENTR	10090.ENSMUSP00000025904,28377.ENSACAP00000006272,7227.FBpp0100079,7955.ENSDARP00000109990,8364.ENSXETP00000013225,9606.ENSP00000265462
f_list = open(filename_MODtree_list,'r')
for line in f_list:
    if line.startswith('#'):
        continue
    tokens = line.strip().split("\t")
    sp_list = tokens[3].split(',')

    #if not 'HUMAN' in sp_list:
    #    continue
    #if not 'XENTR' in sp_list:
    #    continue
    #if not 'CAEEL' in sp_list and not 'DROME' in sp_list:
    #    continue
    
    f_out = open('%s.fa'%tokens[0],'w')
    for tmp_id in tokens[4].split(','):
        tmp_tokens = tmp_id.split('.')
        tmp_tax_id = tmp_tokens[0]
        tmp_prot_id = '.'.join(tmp_tokens[1:])
        tmp_name = tmp_prot_id
        if tmp_prot_id in prot_names:
            tmp_name = prot_names[tmp_prot_id]['name']

        tmp_h = '>%s|%s|%s'%(tax2sp[tmp_tax_id],tmp_name, tmp_prot_id)
        f_out.write('>%s\n%s\n'%(tmp_h, ''.join(seq_list[tmp_prot_id])))
    f_out.close()
f_list.close()
