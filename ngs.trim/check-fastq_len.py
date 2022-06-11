#!/usr/bin/env python3
import gzip
import sys

filename_fq = sys.argv[1]

f_fq = open(filename_fq, 'r')
if filename_fq.endswith('.gz'):
    f_fq = gzip.open(filename_fq, 'rt')

for line in f_fq:
    if line.startswith('@'):
        h_nseq = line.strip()
        len_nseq = len(next(f_fq).strip())
        h_qseq = next(f_fq).strip()
        len_qseq = len(next(f_fq).strip())

        if len_nseq * len_qseq == 0:
            sys.stderr.write("ZERO length: %s\n" % h_nseq)
            break
        elif len_nseq != len_qseq:
            sys.stderr.write("DIFF length: %s\n" % h_nseq)
            break
f_fq.close()
