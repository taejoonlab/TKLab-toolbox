#!/usr/bin/env python3
import sys

filename_fa = sys.argv[1]

f_fa = open(filename_fa, 'r')
if filename_fa.endswith('.gz'):
    f_fa = gzip.open(filename_fa, 'rt')

f_out = open('%s_chr.fa' % (filename_fa.replace('.fa', '')), 'w')
for line in f_fa:
    if line.startswith('>'):
        tmp_h = line.strip().lstrip('>')
        if tmp_h.find('random') >= 0 or tmp_h.startswith('chrUn'):
            is_print = -1
        else:
            is_print = 1
            f_out.write('>%s\n' % tmp_h)
    elif is_print > 0:
        f_out.write("%s\n" % line.strip())
f_fa.close()
f_out.close()
