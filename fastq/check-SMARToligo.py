#!/usr/bin/env python3
import sys

# tmp_seq = 'AAGCAGTGGTATCAACGCAGAGT'
tmp_seq = 'AAGCAGTGGTATCAACGCAGAGT ACATGGG'.replace(' ', '')

# tmp_rc_seq = 'ACTCTGCGTTGATACCACTGCTT'
tmp_rc_seq = 'ACTCTGCGTTGATACCACTGCTT CCCATGT'.replace(' ', '')

filename_fq = sys.argv[1]

total_count = 0
good_count = 0
f_fq = open(filename_fq, 'r')
for tmp_h in f_fq:
    if tmp_h.startswith('@'):
        tmp_nseq = next(f_fq).strip()
        tmp_h2 = next(f_fq)
        tmp_qseq = next(f_fq).strip()

        total_count += 1
        tmp_count = tmp_nseq.count(tmp_seq) + tmp_nseq.count(tmp_rc_seq)
        if tmp_count < 2:
            good_count += 1
f_fq.close()

print("Total reads: %d" % total_count)
print("Reads without TSO oligo: %d (%.2f pct)" %
      (good_count, good_count/total_count*100))
