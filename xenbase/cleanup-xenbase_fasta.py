#!/usr/bin/env python3
import sys
import gzip

filename_fa = sys.argv[1]

f_fa = open(filename_fa, 'r')
if filename_fa.endswith('.gz'):
    f_fa = gzip.open(filename_fa, 'rt')

seq_list = dict()
for line in f_fa:
    if line.startswith('>'):
        tokens = line.strip().lstrip('>').split('|')
        tmp_gene_id = tokens[1]
        tmp_tx_id = tokens[3]

        tmp_level = 1
        tmp_name = tokens[4].strip()
        if tmp_name.find('provisional:') >= 0:
            tmp_name = tmp_name.split('provisional:')[1].replace(']', '')
            tmp_level = 2
        elif tmp_name.find('[provisional]') >= 0:
            tmp_name = tmp_name.split()[0]
            tmp_level = 2

        if tmp_name.upper().startswith('XETRO'):
            tmp_level = 3
        if tmp_name.upper().startswith('LOC'):
            tmp_level = 3
        if tmp_name.upper().startswith('MGC'):
            tmp_level = 3

        if tmp_name.upper().endswith('RIK'):
            tmp_level = 3
        if tmp_name.upper().startswith('XB') and len(tmp_name) >= 8:
            tmp_level = 3

        # Manual fix for XENTR 2021-04-15 version
        if tmp_name == 'homeobox100496651-provisional':
            tmp_name = 'homeobox100496651'
            tmp_level = 3
        if tmp_name == 'opnpl [provisonal]':
            tmp_name = 'opnpl'
            tmp_level = 2
        if tmp_name == 'XB22166507 [provisonal]':
            tmp_name = 'XB22166507'
            tmp_level = 3
        if tmp_name == 'XB5802730 [provisional rab10l]':
            tmp_name = 'rab10l'
            tmp_level = 2
        if tmp_name == 'XB940515 (prov. tnfsf8)':
            tmp_name = 'tnfsf8'
            tmp_level = 2
        if tmp_name == 'car1_predicted':
            tmp_name = 'carl'
            tmp_level = 2

        tmp_h = '%s|%s|%s|Level=%d' % \
                (tmp_name, tmp_tx_id, tmp_gene_id, tmp_level)
        seq_list[tmp_h] = []
    else:
        seq_list[tmp_h].append(line.strip())
f_fa.close()

# 2021-04-15 version
# >gnl|gene5703|XT-9_1-gene5703|rna18481| lamp5
# >gnl|gene29194|XT-9_1-gene29194|rna56249| LOC108646171 [provisional:hcn4]

for tmp_h in sorted(seq_list.keys()):
    print(">%s\n%s" % (tmp_h, ''.join(seq_list[tmp_h])))
