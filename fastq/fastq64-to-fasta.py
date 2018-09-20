#!/usr/bin/env python3
import sys
import gzip
import re

filename_fastq = sys.argv[1]

f_fastq = open(filename_fastq, 'r')
if filename_fastq.endswith('.gz'):
    f_fastq = gzip.open(filename_fastq, 'rt')

filename_base = re.sub(r'.(fq|fastq|fq.gz|fastq.gz)$', '', filename_fastq)

f_fa = open('%s.fa' % (filename_base), 'w')

for line in f_fastq:
    if line.startswith('@'):
        header = line.strip()
        nseq = next(f_fastq).strip()
        h2 = next(f_fastq).strip()
        qseq = next(f_fastq).strip()

        str_list = []
        tmp_i = 0
        for tmp_q in [ord(x)-64 for x in qseq]:
            if tmp_q < 20:
                str_list.append(nseq[tmp_i].lower())
            else:
                str_list.append(nseq[tmp_i].upper())
            tmp_i += 1

        f_fa.write(">%s\n%s\n" % (header.lstrip('@'), ''.join(str_list)))
f_fastq.close()
f_fa.close()
