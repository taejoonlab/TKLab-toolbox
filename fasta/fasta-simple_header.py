#!/usr/bin/env python3
import sys

filename_fa = sys.argv[1]

f_fa = open(filename_fa, 'r')
if filename_fa.endswith('.gz'):
    import gzip
    f_fa = gzip.open(filename_fa, 'rt')

for line in f_fa:
    if line.startswith('>'):
        print(line.strip().split()[0])
    else:
        print(line.strip())
f_fa.close()
