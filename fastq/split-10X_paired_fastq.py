#!/usr/bin/env python3
import os
import sys
import gzip

filename_R1 = sys.argv[1]
#filename_R1 = "5068-JG-0006_S1_L001_R1_001.fastq.gz"
filename_R2 = filename_R1.replace('_R1_','_R2_')

filename_R1_out_base = filename_R1.replace('.fastq.gz','')
filename_R2_out_base = filename_R2.replace('.fastq.gz','')

f_out_R1 = dict()
f_out_R2 = dict()

f_R1 = gzip.open(filename_R1,'rt')
f_R2 = gzip.open(filename_R2,'rt')

for h_R1 in f_R1:
    h_R2 =f_R2.readline()
    list_R1 = [f_R1.readline().strip() for i in range(0,3)]
    list_R2 = [f_R2.readline().strip() for i in range(0,3)]

    r_R1 = h_R1.strip().split()[0]
    r_R2 = h_R2.strip().split()[0]
    bc_R1 = h_R1.strip().split(':')[-1]
    bc_R2 = h_R2.strip().split(':')[-1]

    if r_R1 == r_R2 and bc_R1 == bc_R2:
        if not bc_R1 in f_out_R1:
            f_out_R1[bc_R1] = open('%s.%s.fastq'%(filename_R1_out_base,bc_R1),'a')
            f_out_R2[bc_R2] = open('%s.%s.fastq'%(filename_R2_out_base,bc_R2),'a')

        f_out_R1[bc_R1].write('\n'.join(list_R1)+"\n")
        f_out_R2[bc_R2].write('\n'.join(list_R2)+"\n")

    for i in range(0,4):
        next(f_R1)
        next(f_R2)

for tmp_bc in f_out_R1.keys():
    f_out_R1[tmp_bc].close()
    f_out_R2[tmp_bc].close()

#@E00247:495:HCWMLCCXY:1:1101:3569:1309 1:N:0:NTAGTTAC
#NAGCTACAGCTCCTCTATTGTGGTTACTATTATTCTGGGGTGTTACTATTATTTATGGGGTGTTACTATTATTTATGGGTTGTTACTATTATTTATGGGTTGTTACTATTATTTATGGGGTGTTACCATTATTCTTGGGTTGTTATTTTTT
