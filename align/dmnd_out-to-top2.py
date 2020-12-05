#!/usr/bin/env python3
import sys

filename_dmnd_out = sys.argv[1]

f_out = open(filename_dmnd_out, 'r')
if filename_dmnd_out.endswith('.gz'):
    import gzip
    f_out = gzip.open(filename_dmnd_out, 'r')

hits_list = dict()
for line in f_out:
    tokens = line.strip().split("\t")
    q_id = tokens[0]
    t_id = tokens[1]
    tmp_bits = float(tokens[-1])

    if q_id not in hits_list:
        hits_list[q_id] = {'self_bits': 0,
                           'nonself_id': 'NA',  'nonself_bits': 0}

    if q_id == t_id:
        hits_list[q_id]['self_bits'] = tmp_bits
    elif hits_list[q_id]['nonself_bits'] < tmp_bits:
        hits_list[q_id]['nonself_id'] = t_id
        hits_list[q_id]['nonself_bits'] = tmp_bits
f_out.close()

for tmp_id, tmp in hits_list.items():
    print("%s\t%.1f\t%s\t%.1f" %
          (tmp_id, tmp['self_bits'], tmp['nonself_id'], tmp['nonself_bits']))
