import sys,re,os

tmp_read = {}
risk = 0
mms6883 = ''
mms1 = ''
mms2 = ''
mms3 = ''

testlist = ['mms0621-1','mms0725-2','mms0725-3','mms6883']

with open('uniq_tag_frog.txt','r') as f:
    for line in f:
        if line.startswith('cluster'):
            if risk == 0:
                #if len(tmp_read.keys()) == 4:
                if len(tmp_read.keys()) < 4 and len(tmp_read.keys()) != 0:
                    for mms in testlist:
                        if mms not in tmp_read:
                            tmp_read[mms] = '-'*len(tmp_read['mms6883'])
                    for ab in tmp_read.keys():
                        if ab == 'mms0621-1':
                            mms1 += tmp_read[ab]
                        elif ab == 'mms0725-2':
                            mms2 += tmp_read[ab]
                        elif ab == 'mms0725-3':
                            mms3 += tmp_read[ab]
                        elif ab == 'mms6883':
                            mms6883 += tmp_read[ab]
            risk = 0
            tmp_read = {}
        else:
            name,seq = line.split()
            indiv = name.split('.')[0]
            if indiv in tmp_read:
                risk =1
            tmp_read[indiv] = seq

print len(mms6883),len(mms1),len(mms2),len(mms3)
snp1 = open('tagSNP_0621-1.txt','w')
snp2 = open('tagSNP_0725-2.txt','w')
snp3 = open('tagSNP_0725-3.txt','w')
snp6883 = open('tagSNP_6883.txt','w')

snp1.write('>mms0621-1\n'+mms1+'\n')
snp2.write('>mms0725-2\n'+mms2+'\n')
snp3.write('>mms0725-3\n'+mms3+'\n')
snp6883.write('>mms6883\n'+mms6883+'\n')

