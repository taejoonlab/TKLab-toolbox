#!/usr/bin/env python3
import os
import sys
import gzip

filename_MODtree_list = sys.argv[1]

dirname_ens = '/work/project/pub/ens/70/'

prot2gene = dict()
for filename in os.listdir(dirname_ens):
    if not filename.endswith('.pep.all.fa.gz'):
        continue
    sys.stderr.write('Read %s\n'%filename)
    f_fa = gzip.open(os.path.join(dirname_ens,filename),'rt')
    for line in f_fa:
        if line.startswith('>'):
            tmp_tokens = line.strip().lstrip('>').split()
            prot_id = tmp_tokens[0]
            gene_id = tmp_tokens[3].split(':')[1]
            prot2gene[prot_id] = gene_id
    f_fa.close()

tax2sp = dict()
f_tax = open('/home/taejoon/git/HTseq-toolbox/annot/MODtree.species_list.txt','r')
for line in f_tax:
    tokens = line.strip().split("\t")
    tax2sp[ tokens[2] ] = tokens[0]
f_tax.close()

#GO_list: GO:0000400,GO:0000975,GO:0000976,GO:0000977,GO:0000978,GO:0000981,GO:0000986,GO:0000987,GO:0001046,GO:0001164,GO:0001165,GO:0003677,GO:0003684,GO:0003690,GO:0003696,GO:0003697,GO:0003700,GO:0004879,GO:0008301,GO:0010385,GO:0019237,GO:0030983,GO:0031492,GO:0042162,GO:0043047,GO:0043565,GO:0044212,GO:0051090,GO:0070336
#ZZZ3	Q8IYH5	ENSG00000036549	1	GO:0003677
q_gene_list = dict()
f_list=  open('../GOA_HUMAN_DBP.list','r')
for line in f_list:
    if line.startswith('#'):
        continue
    tokens = line.strip().split("\t")
    tmp_gene_id = tokens[2]
    tmp_gene_name = tokens[0]
    q_gene_list[tmp_gene_id] = tmp_gene_name
f_list.close()

#==> MODtree.biNOG.list <==
#MODtreeID	CountSpecies	CountProt	SpeciesList	ProtList
#biNOG.ENOG410A4PF.PRDX5	6	6	ANOCA,DANRE,DROME,HUMAN,MOUSE,XENTR	10090.ENSMUSP00000025904,28377.ENSACAP00000006272,7227.FBpp0100079,7955.ENSDARP00000109990,8364.ENSXETP00000013225,9606.ENSP00000265462
f_list = open(filename_MODtree_list,'r')
for line in f_list:
    if line.startswith('#'):
        continue
    tokens = line.strip().split("\t")
    tmp_id = tokens[0]
    tmp_count_species = int(tokens[1])
    tmp_count_prot = int(tokens[2])
    tmp_species_list = tokens[3].split(',')
    tmp_prot_list = tokens[4].split(',')

    tmp_gene_list = []
    for tmp_prot_id in tmp_prot_list:
        tmp_prot_id = '.'.join( tmp_prot_id.split('.')[1:] )
        if tmp_prot_id in prot2gene and prot2gene[tmp_prot_id] in q_gene_list:
            tmp_gene_name = q_gene_list[ prot2gene[tmp_prot_id] ]
            tmp_gene_list.append(tmp_gene_name)

    if len(tmp_gene_list) == 0:
        continue
    
    tmp_gene_list = sorted(tmp_gene_list)
    #if not 'DROME' in tmp_species_list and not 'CAEEL' in tmp_species_list:
    if 'DROME' in tmp_species_list or 'CAEEL' in tmp_species_list:
        per_sp_count = dict()
        for tmp_prot_id in tmp_prot_list:
            tmp_tax_id = tmp_prot_id.split('.')[0]
            tmp_sp_id = tax2sp[tmp_tax_id]
            if not tmp_sp_id in per_sp_count:
                per_sp_count[tmp_sp_id] = 0
            per_sp_count[tmp_sp_id] += 1
        
        print( tmp_gene_list, per_sp_count )
f_list.close()

