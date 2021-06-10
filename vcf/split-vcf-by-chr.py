#!/usr/bin/env python3
import sys

filename_vcf = sys.argv[1]

f_list = dict()
f_vcf = open(filename_vcf, 'r')
for line in f_vcf:
    if line.startswith('#'):
        continue
    tokens = line.strip().split("\t")
    t_id = tokens[0]
    if len(t_id) > 5:
        t_id = 'chrUn'

    if t_id not in f_list:
        f_list[t_id] = open('%s.%s' % (filename_vcf, t_id), 'w')
    f_list[t_id].write("%s\n" % line.strip())
f_vcf.close()
