#!/usr/bin/env python3
import sys
import gzip
import math

filename_vcf = sys.argv[1]

f_vcf = open(filename_vcf, 'r')
if filename_vcf.endswith('gz'):
    f_vcf = gzip.open(filename_vcf, 'rt')

f_out = open('%s.EAS' % filename_vcf, 'w')
for line in f_vcf:
    if line.startswith('#'):
        continue

    tokens = line.strip().split("\t")
    tmp_flag = tokens[6]
    if tmp_flag.find('PASS') < 0:
        continue

    info_list = {'AC':0, 'AN':0, 'AC_eas':0, 'AN_eas':0}
    for tmp_info in tokens[7].split(';'):
        if tmp_info.find('=') < 0:
            continue

        (tmp_k, tmp_v) = tmp_info.split('=')
        if tmp_k in info_list.keys():
            info_list[tmp_k] = int(tmp_v)
    
    if info_list['AC_eas'] <= 1:
        continue
    
    info_list['AF'] = math.log10(float(info_list['AC'])/float(info_list['AN']))
    info_list['AF_eas'] = math.log10(float(info_list['AC_eas'])/float(info_list['AN_eas']))
    info_list['AF_odds'] = (info_list['AF_eas'] - info_list['AF']) / math.log10(2)
    if info_list['AF_odds'] > 1:
        sys.stderr.write('%s\t%.2f\n' % ('\t'.join(tokens[:5]), info_list['AF_odds']))
        f_out.write('%s\n' % line.strip())
        #print(info_list)
f_vcf.close()
f_out.close()
