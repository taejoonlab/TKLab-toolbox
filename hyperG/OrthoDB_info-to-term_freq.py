#!/usr/bin/env python3
import sys
import gzip

filename_info = sys.argv[1]
filename_info = 'vertebrata_7742_OrthoDB9_orthogroup_info.txt.gz'

f_info = open(filename_info, 'r')
filename_base = filename_info.replace('_info.txt', '_info')
if filename_info.endswith('.gz'):
    f_info = gzip.open(filename_info, 'rt')
    filename_base = filename_info.replace('_info.txt.gz', '_info')

freq_GO = dict()
freq_IPR = dict()
h_info = f_info.readline().strip().split("\t")
idx_GO = h_info.index('BiologicalProcesses')
idx_IPR = h_info.index('InterProDomains')
for line in f_info:
    tokens = line.strip().split("\t")
    og_id = tokens[0]
    for tmp_GO in tokens[idx_GO].split(';'):
        if tmp_GO not in freq_GO:
            freq_GO[tmp_GO] = []
        freq_GO[tmp_GO].append(og_id)
    
    for tmp_IPR in tokens[idx_IPR].split(';'):
        if tmp_IPR not in freq_IPR:
            freq_IPR[tmp_IPR] = []
        freq_IPR[tmp_IPR].append(og_id)
f_info.close()
#OrthoGroupID	Description	#Species	#Single-Copy	#Multi-Copy	ProtMedianLength	EvoRate	BiologicalProcesses	InterProDomains
#EOG090B000N	"baculoviral IAP repeat containing 6"	163	159	4	4781	0.8562	GO:0001890;GO:0006464;GO:0008219;GO:0008284;GO:0016567;GO:0042127;GO:0060711;GO:0060712;GO:2001237	IPR000608;IPR001370;IPR015943;IPR016135;IPR022103

min_count = 3
f_GO_out = open('%s.GO_freq' % filename_base, 'w')
for tmp_GO in sorted(freq_GO.keys()):
    if tmp_GO == 'NA':
        continue
    tmp_count = len(freq_GO[tmp_GO])
    if tmp_count <= min_count:
        continue
    tmp_og_list = ';'.join(sorted(freq_GO[tmp_GO]))
    f_GO_out.write('%s\t%s\t%s\n' % (tmp_GO, tmp_count, tmp_og_list))
f_GO_out.close()

f_IPR_out = open('%s.IPR_freq' % filename_base, 'w')
for tmp_IPR in sorted(freq_IPR.keys()):
    if tmp_IPR == 'NA':
        continue
    tmp_count = len(freq_IPR[tmp_IPR])
    if tmp_count <= min_count:
        continue
    tmp_og_list = ';'.join(sorted(freq_IPR[tmp_IPR]))
    f_IPR_out.write('%s\t%s\t%s\n' % (tmp_IPR, tmp_count, tmp_og_list))
f_IPR_out.close()

