#dominant
import os

folder = sys.argv[1]

def make_file_list(input_dir):
    file_list = []
    input_file_list = os.listdir(input_dir)
    for input_file in input_file_list:
        if input_file[-8:] == '.cluster':
            file_list.append(input_file)
    return file_list

file_list = make_file_list(folder)

for each_file in file_list:
    with open(folder + each_file,'r') as f:
        print each_file
        clustername = each_file.replace('.cluster','')
        sample = each_file.split('_')[1]
        sample_name = each_file.split('.')[0]
        uniq = open('dom_{}'.format(clustername),'w')
        tmp_name = []
        seq_dic = []
        for line in f: #indel is not considered (hard to compare further)
            if len(line.strip()) <171:
                continue
            name,seq = line.split()
            if name.startswith('cluster'):
                tmp_record = ''
                if len(seq_dic)>1:
                    for i in range(len(seq_dic[1])):
                        tmp_seq = ''
                        for j in range(len(seq_dic)): #tmp_seq containt every nucleotide from same position of reads in one cluster
                            tmp_seq += seq_dic[j][i]
                        #record most frequently shown nucleotide as fasta format
                        max_base = max(tmp_seq.count('A'),tmp_seq.count('T'),tmp_seq.count('G'),tmp_seq.count('C'),tmp_seq.count('-'))
                        max_a = tmp_seq.count('A')
                        max_g = tmp_seq.count('G')
                        max_t = tmp_seq.count('T')
                        max_c = tmp_seq.count('C')
                        if max_base == max_a:
                            tmp_record += 'A'
                        elif max_base == max_g:
                            tmp_record += 'G'
                        elif max_base == max_t:
                            tmp_record += 'T'    
                        elif max_base == max_c:
                            tmp_record += 'C'
                    if len(tmp_record) == 101:
                        uniq.write('>{}\n{}\n'.format(tmp_name[0].split('*')[0],tmp_record))
                tmp_name = []
                seq_dic = []
            else:
                tmp_name.append(name)
                seq_dic.append(seq)

