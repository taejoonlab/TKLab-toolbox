#!/usr/bin/env python3
import gzip
import sys

filename_fq = sys.argv[1]

# This is a hard-coded info. Check your recovered FQ file (from gzrecover)
# and revise it.

h_prefix = '@NB501'

read_set = []
f_fq = open(filename_fq, 'rb')
if filename_fq.endswith('.gz'):
    f_fq = gzip.open(filename_fq, 'rb')

f_err = open('%s.error' % filename_fq, 'w')
f_out = open('%s.out' % filename_fq, 'w')
for tmp in f_fq:
    try:
        tmp_h = tmp.decode().strip()
        if tmp_h.startswith(h_prefix):
            if len(read_set) >= 4:
                read_h = read_set[0]
                read_seq = read_set[1]
                read_qh = read_set[2]
                read_qseq = read_set[3]

                is_corrupt = 0
                for tmp_line in [read_seq, read_qh, read_qseq]:
                    if tmp_line.startswith(h_prefix):
                        is_corrupt += 1
                
                if is_corrupt > 0:
                    f_err.write("[Dump]"+"\n".join(read_set) + "\n")
                else:
                    f_out.write("%s\n%s\n%s\n%s\n" %
                                (read_h, read_seq, read_qh, read_qseq))
                    if len(read_set) > 4:
                        f_err.write("[Dump]"+"\n".join(read_set[4:]) + "\n")
            elif len(read_set) > 0:
                f_err.write("[Dump]"+"\n".join(read_set) + "\n")

            read_set = []
        
        read_set.append(tmp_h)
    except:
        f_err.write("[ERROR]%s\n" % tmp)

f_fq.close()
f_out.close()
f_err.close()
