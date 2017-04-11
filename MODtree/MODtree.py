filename_sp_list = 'MODtree.species_list.txt'
filename_names = 'ens70.prot2name.gz'

import gzip
import os

dirname_curr = os.path.dirname(os.path.realpath(__file__))

def get_tax2sp():
    tax2sp = dict()
    f_list =  open(os.path.join(dirname_curr,filename_sp_list),'r')
    for line in f_list:
        tokens = line.strip().split("\t")
        sp_code = tokens[0]
        tax_id = tokens[2]
        tax2sp[tax_id] = sp_code
    f_list.close()
    return tax2sp

def get_sp_info():
    rv = dict()
    f_list =  open(os.path.join(dirname_curr,filename_sp_list),'r')
    for line in f_list:
        tokens = line.strip().split("\t")
        sp_code = tokens[0]
        sp_name = tokens[1]
        tax_id = tokens[2]
        rv[sp_name] = {'sp_code':sp_code, 'tax_id':tax_id}
    f_list.close()
    return rv

def get_HS_prot2names():
    HS_names = dict()
    f_names =  gzip.open(os.path.join(dirname_curr,filename_names),'rt')
    for line in f_names:
        tokens = line.replace('"','').split()
        if len(tokens) != 5:
            continue
        if tokens[4] == 'Homo_sapiens':
            HS_names[tokens[3]] = tokens[1]
    f_names.close()
    return HS_names

def get_prot2names():
    prot_names = dict()
    f_names =  gzip.open(os.path.join(dirname_curr,filename_names),'rt')
    for line in f_names:
        tokens = line.replace('"','').split()
        if len(tokens) != 5:
            continue
        prot_names[tokens[3]] = {'species':tokens[4], 'name':tokens[1]}
    f_names.close()
    return prot_names
