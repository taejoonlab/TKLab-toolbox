import sys, os, re

folder = sys.argv[1]

def make_file_list(input_dir):
    file_list = []
    input_file_list = os.listdir(input_dir)
    for input_file in input_file_list:
        if input_file[:5] == 'uniq_':
            file_list.append(input_file)
    return file_list
#make file list
file_list = make_file_list(folder)

for each_file in file_list:
    tag_file = open('TAG'+each_file.replace('uniq',''),'w')
    gatc_file = open('GATC'+each_file.replace('uniq',''),'w')
    with open(folder + each_file,'r') as f:
        for line in f:
            if line.startswith('>'):
                name = line.strip()
            elif line.startswith('TAG'): #depend on enzyme cutsite, divide samples into different files (not clustered together)
                seq = line.strip()
                if len(seq) <101:
                    continue
                tag_file.write('>'+each_file[5:-6]+'.'+name[1:]+'\n'+seq+'\n')
            elif line.startswith('GATC'):
                seq = line.strip()
                if len(seq) <101:
                    continue
                gatc_file.write('>'+each_file[5:-6]+'.'+name[1:]+'\n'+seq+'\n')
    
