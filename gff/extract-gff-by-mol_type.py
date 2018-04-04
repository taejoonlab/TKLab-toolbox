#!/usr/bin/env python3
import os
import sys

usage_mesg = '\nUsage: %s <gff file> <mol_type>\n\n'%(sys.argv[0])

def print_usage_and_exit():
    sys.stderr.write(usage_mesg)
    sys.exit(1)

if len(sys.argv) != 3:
    print_usage_and_exit()

filename_gff = sys.argv[1]
query_mol_type = sys.argv[2]

if not os.access(filename_gff, os.R_OK):
    sys.stderr.write('%s is not available.\n'%filename_gff)
    print_usage_and_exit()

count_out_line = 0
f_gff = open(filename_gff,'r')
if filename_gff.endswith('.gz'):
    import gzip
    f_gff = gzip.open(filename_gff, 'rt')

for line in f_gff:
    if line.startswith('#'):
        print( line.strip() )
        continue

    tokens = line.strip().split("\t")
    mol_type = tokens[2]
    if mol_type == query_mol_type:
        count_out_line += 1
        print( line.strip() )
f_gff.close()

sys.stderr.write('Total number of extracted lines: %d\n'%count_out_line)
