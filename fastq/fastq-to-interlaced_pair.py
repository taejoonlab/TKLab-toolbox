#!/usr/bin/env python3
import sys
import gzip

filename_fq1 = sys.argv[1]
filename_fq2 = sys.argv[2]
filename_out = sys.argv[3]

f_fq1 = open(filename_fq1, 'r')
if filename_fq1.endswith('.gz'):
    f_fq1 = gzip.open(filename_fq1, 'rb')

f_fq2 = open(filename_fq2, 'r')
if filename_fq2.endswith('.gz'):
    f_fq2 = gzip.open(filename_fq2, 'rb')

read1_len = 0
read2_len = 0

nfreq1_raw = dict()
nfreq2_raw = dict()
nfreq1_called = dict()
nfreq2_called = dict()

count_total = 0
count_nocall_1 = 0
count_nocall_2 = 0
count_nocall_12 = 0

f_out = open('%s.i_paired.fastq' % filename_out, 'w')
for line in f_fq1:
    h_nseq1 = line.strip()
    nseq1 = f_fq1.next().strip()
    h_qseq1 = f_fq1.next().strip()
    qseq1 = f_fq1.next().strip()

    read1_len = len(nseq1)
    if len(nfreq1_raw) < read1_len:
        for tmp_i in range(len(nfreq1_raw), read1_len):
            nfreq1_raw[tmp_i] = {'A': 0, 'T': 0, 'G': 0, 'C': 0, 'N': 0}
            nfreq1_called[tmp_i] = {'A': 0, 'T': 0, 'G': 0, 'C': 0, 'N': 0}

    h_nseq2 = f_fq2.next().strip()
    nseq2 = f_fq2.next().strip()
    h_qseq2 = f_fq2.next().strip()
    qseq2 = f_fq2.next().strip()

    read2_len = len(nseq2)
    if len(nfreq2_raw) < read2_len:
        for tmp_i in range(len(nfreq2_raw), read2_len):
            nfreq2_raw[tmp_i] = {'A': 0, 'T': 0, 'G': 0, 'C': 0, 'N': 0}
            nfreq2_called[tmp_i] = {'A': 0, 'T': 0, 'G': 0, 'C': 0, 'N': 0}

    count_total += 1

    count_N1 = nseq1.count('N') + nseq1.count('.')
    count_N2 = nseq2.count('N') + nseq2.count('.')

    count_A1 = nseq1.count('A')
    count_A2 = nseq2.count('A')
    count_T1 = nseq1.count('T')
    count_T2 = nseq2.count('T')
    count_G1 = nseq1.count('G')
    count_G2 = nseq2.count('G')
    count_C1 = nseq1.count('C')
    count_C2 = nseq2.count('C')

    if count_N1 > 0 and count_N2 > 0:
        count_nocall_12 += 1
        for tmp_i in range(0, read1_len):
            nfreq1_raw[tmp_i][nseq1[tmp_i]] += 1
        for tmp_i in range(0, read2_len):
            nfreq2_raw[tmp_i][nseq2[tmp_i]] += 1

    elif count_N1 > 0 or count_A1*count_T1*count_C1*count_G1 == 0:
        count_nocall_1 += 1
        for tmp_i in range(0, read1_len):
            nfreq1_raw[tmp_i][nseq1[tmp_i]] += 1

        for tmp_i in range(0, read2_len):
            nfreq2_raw[tmp_i][nseq2[tmp_i]] += 1
    elif count_N2 > 0 or count_A2*count_T2*count_C2*count_G2 == 0:
        count_nocall_2 += 1
        for tmp_i in range(0, read1_len):
            nfreq1_raw[tmp_i][nseq1[tmp_i]] += 1
        for tmp_i in range(0, read2_len):
            nfreq2_raw[tmp_i][nseq2[tmp_i]] += 1
    else:
        for tmp_i in range(0, read1_len):
            nfreq1_raw[tmp_i][nseq1[tmp_i]] += 1
            nfreq1_called[tmp_i][nseq1[tmp_i]] += 1

        for tmp_i in range(0, read2_len):
            nfreq2_raw[tmp_i][nseq2[tmp_i]] += 1
            nfreq2_called[tmp_i][nseq2[tmp_i]] += 1

#       h1_tokens = h_nseq1.split()
#       if( len(h1_tokens) > 1 ):
#           h_nseq1 = '@%s'%h1_tokens[0]
#       h2_tokens = h_nseq2.split()
#       if( len(h2_tokens) > 1 ):
#           h_nseq2 = '@%s'%h2_tokens[0]

        f_out.write('%s\n%s\n+\n%s\n' % (h_nseq1, nseq1, qseq1))
        f_out.write('%s\n%s\n+\n%s\n' % (h_nseq2, nseq2, qseq2))
f_fq1.close()
f_fq2.close()
f_out.close()

nucl_list = ['A', 'T', 'G', 'C', 'N']

f_raw = open('%s_R1.raw.i_pos_call' % filename_out, 'w')
f_called = open('%s_R1.called.i_pos_call' % filename_out, 'w')
f_raw.write('Position\tA\tT\tG\tC\tN\n')
f_called.write('Position\tA\tT\tG\tC\n')
for tmp_i in range(0, read1_len):
    tmp_ATGCN = '\t'.join(['%d' % nfreq1_raw[tmp_i][x] for x in nucl_list])
    f_raw.write('%d\t%s\n' % (tmp_i, tmp_ATGCN))
    tmp_ATGCN = '\t'.join(['%d' % nfreq1_called[tmp_i][x] for x in nucl_list])
    f_called.write('%d\t%s\n' % (tmp_i, tmp_ATGCN))
f_raw.close()
f_called.close()

f_raw = open('%s_R2.raw.i_pos_call' % filename_out, 'w')
f_called = open('%s_R2.called.i_pos_call' % filename_out, 'w')
f_raw.write('Position\tA\tT\tG\tC\tN\n')
f_called.write('Position\tA\tT\tG\tC\n')
for tmp_i in range(0, read2_len):
    tmp_ATGCN = '\t'.join(['%d' % nfreq2_raw[tmp_i][x] for x in nucl_list])
    f_raw.write('%d\t%s\n' % (tmp_i, tmp_ATGCN))
    tmp_ATGCN = '\t'.join(['%d' % nfreq2_called[tmp_i][x] for x in nucl_list])
    f_called.write('%d\t%s\n' % (tmp_i, tmp_ATGCN))
f_raw.close()
f_called.close()

f_log = open('%s.i_paired.log' % filename_out, 'w')
f_log.write('Total pairs: %d\n' % count_total)
count_fail = count_nocall_12 + count_nocall_1 + count_nocall_2
f_log.write('Failed: %d (_1:%d, _2:%d, both:%d)\n' %
            (count_fail, count_nocall_1, count_nocall_2, count_nocall_12))
count_good_pair = count_total - count_fail
pct_good_pair = (count_total - count_fail) * 100.0 / count_total
f_log.write('Good pairs: %d (%.2f pct)\n' % (count_good_pair, pct_good_pair))
