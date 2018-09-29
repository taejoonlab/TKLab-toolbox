#SNP call
import sys

fname = sys.argv[1]

uniq = open('uniq_{}.txt'.format(fname.split('.')[0]),'w')
f = open(fname,'r')
tmp1 = []
tmp2 = []
for line in f:
    if len(line.strip())<170:
        continue
    name,seq = line.split()
    if name.startswith('cluster'):
        tmp3 = [''] *(len(tmp2))
        if len(tmp2) != 0 and len(tmp2)<18: # how many reads can be allowed in one cluster
            for i in range(len(tmp2[1])):
                tmp_seq = ''
                for j in range(len(tmp2)):
                    tmp_seq += tmp2[j][i]
                if max(tmp_seq.count('A'),tmp_seq.count('T'),tmp_seq.count('G'),tmp_seq.count('C'),tmp_seq.count('-')) < j+1:
                    for k in range(len(tmp_seq)):
                        tmp3[k] += tmp_seq[k]
            if len(tmp3) != 0 and len(tmp3[0])!=0:
                uniq.write(tmp1[0]+'\n')
                for l in range(len(tmp3)):         
                    uniq.write(tmp1[l+1].ljust(70)+tmp3[l]+'\n')
        tmp1 = [name] #tmp1[0] is always cluster name
        tmp2 = []
    else:
        tmp1.append(name)
        tmp2.append(seq)

