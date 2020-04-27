#!/usr/bin/env python3
import sys
import gzip

filename_fa = sys.argv[1]

f_fa = open(filename_fa, 'r')
if filename_fa.endswith('.gz'):
    f_fa = gzip.open(filename_fa, 'rt')

for line in f_fa:
    if line.startswith('>'):
        tmp_tokens = line.strip().lstrip('>').split('|')
        print(">%s|%s|%s" % (tmp_tokens[-2], tmp_tokens[0], tmp_tokens[2]))
    else:
        print(line.strip())
f_fa.close()
