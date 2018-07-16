#!/usr/bin/env python3
import sys

filename_fa = sys.argv[1]
filename_list = sys.argv[2]

seq_h = ''
seq_list = dict()
f_fa = open(filename_fa, 'r')
for line in f_fa:
    if line.startswith('>'):
        seq_h = line.strip().lstrip('>')
        seq_list[seq_h] = []
    else:
        seq_list[seq_h].append(line.strip())
f_fa.close()

f_list = open(filename_list, 'r')
for line in f_list:
    tokens = line.strip().split()
    if tokens[0] in seq_list:
        print(">%s\n%s" % (tokens[0], ''.join(seq_list[tokens[0]])))
f_list.close()
