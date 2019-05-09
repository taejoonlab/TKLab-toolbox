import sys, os, re

folder = sys.argv[1]

def make_file_list(input_dir):
    file_list = []
    input_file_list = os.listdir(input_dir)
    for input_file in input_file_list:
        if input_file[:4] == 'abc_':
            file_list.append(input_file)
    return file_list

#make file list
file_list = make_file_list(folder)


for each_file in file_list:
    uniq_seq = open('uniq_'+each_file[4:],'w')
    with open(folder+each_file,'r') as f:
        species = each_file.split('.')[4:]
        linecount = 1
        tmp_seq = ''
        uniqcount = 0
        for line in f:
            if linecount == 1: #sequence name
                linecount+=1
                name = line.strip()
            else: #sequence
                linecount = 1
                seq = line.strip()
                if tmp_seq == seq: #only reads with exactly same sequence with previous read will recorded
                    uniq_seq.write(name+'\n'+seq+'\n')
                elif tmp_seq != seq:
                    uniqcount = 0 #new sequcence > do not record
                tmp_seq = seq
