#!/usr/bin/env python3
import os
import sys

filename_gff = sys.argv[1]
query_mol_type = sys.argv[2]

f_gff = open(filename_gff,'r')
for line in f_gff:
    if line.startswith('#'):
        print( line.strip() )
        continue

    tokens = line.strip().split("\t")
    mol_type = tokens[2]
    if mol_type == query_mol_type:
        print( line.strip() )
f_gff.close()
