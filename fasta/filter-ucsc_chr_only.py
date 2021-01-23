#!/usr/bin/env python3
import sys

filename_fa = sys.argv[1]

seq_list = dict()
seq_len = dict()

f_fa = open(filename_fa, 'r')
if filename_fa.endswith('.gz'):
    import gzip
    f_fa = gzip.open(filename_fa, 'rt')

for line in f_fa:
    if line.startswith('>'):
        tmp_h = line.strip().lstrip('>').split()[0]
        seq_list[tmp_h] = []
        seq_len[tmp_h] = 0
    else:
        seq_list[tmp_h].append(line.strip())
        seq_len[tmp_h] += len(line.strip())
f_fa.close()

f_out = open(filename_fa+'.chr_only', 'w')
f_seqlen = open(filename_fa+'.chr_only_seqlen', 'w')
for tmp_h in sorted(seq_len.keys(), key=seq_len.get, reverse=True):
    if tmp_h.startswith('chrUn') or tmp_h.find('random') >= 0:
        continue

    f_out.write('>%s\n%s\n' % (tmp_h, ''.join(seq_list[tmp_h])))
    f_seqlen.write('%s\t%d\n' % (tmp_h, seq_len[tmp_h]))
f_out.close()
f_seqlen.close()
