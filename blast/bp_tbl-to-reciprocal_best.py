#!/usr/bin/env python3
import os
import sys
import gzip

## files from NCBI BLAST tabular format
filename_A = sys.argv[1]
filename_B = sys.argv[2]

def read_tbl(filename):
    rv = dict()
    f = open(filename,'r')
    if filename.endsiwth('.gz'):
        f = gzip.open(filename,'rt')
    for line in f:
        if line.startswith('#'):
            continue
        tokens = line.strip().split("\t")
        q_id = tokens[0]
        t_id = tokens[1]
        bits = float(tokens[-1])
        if not q_id in rv:
            rv[q_id] = {'t_id':t_id, 'bits':bits}
        elif rv[q_id]['bits'] < bits:
            rv[q_id] = {'t_id':t_id, 'bits':bits}
    f.close()
    return rv

best_A = read_tbl(filename_A)
best_B = read_tbl(filename_B)

for id_A in best_A.keys():
    id_B = best_A[id_A]['t_id']
    tmp_A = best_A[id_A]
    if id_B in best_B and best_B[id_B]['t_id'] == id_A:
        tmp_B = best_B[id_B]
        print("%s\t%s\t%.1f\t%.1f"%(id_A, id_B, tmp_A['bits'], tmp_B['bits']))
