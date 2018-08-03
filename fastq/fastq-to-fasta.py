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
        nseq = f_fastq.next().strip()
        h2 = f_fastq.next().strip()
        qseq = f_fastq.next().strip()
        f_fa.write(">%s\n%s\n" % (header.lstrip('@'), nseq))
f_fastq.close()
f_fa.close()
