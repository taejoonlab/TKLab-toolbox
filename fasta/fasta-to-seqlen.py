#!/usr/bin/env python3
import sys
import gzip

filename_fa = sys.argv[1]

h_fa = ''
seqlen = dict()
f_fa = open(filename_fa, 'r')
if filename_fa.endswith('.gz'):
    f_fa = gzip.open(filename_fa, 'rt')

for line in f_fa:
    if line.startswith('>'):
        h_fa = line.strip().lstrip('>').split()[0]
        seqlen[h_fa] = 0
    else:
        seqlen[h_fa] += len(line.strip())
f_fa.close()

for h_fa in sorted(seqlen.keys(), key=seqlen.get, reverse=True):
    print("%s\t%d" % (h_fa, seqlen[h_fa]))
