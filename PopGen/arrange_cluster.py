import sys,re,os

criteria = sys.argv[1]
criteria = int(criteria)
folder = sys.argv[2]

def make_file_list(input_dir):
    file_list = []
    input_file_list = os.listdir(input_dir)
    for input_file in input_file_list:
        if input_file[-3:] == '.uc':
            file_list.append(input_file)
    return file_list

file_list = make_file_list(folder)

for each_file in file_list:
    print each_file
    fasta_file = folder+each_file.split('.')[0]+'.fasta'
    index_seq = {}
    #load sequence information from fasta file
    with open(fasta_file,'r') as f:
        for line in f:
            if line.startswith('>'):
                index = line.strip()[1:]
            else:
                seq = line.strip()
                index_seq[index]=seq

    arrange = {}
    #from arrange clustering output
    with open(folder+each_file,'r') as f2:
        for line in f2:
            if line.startswith('H'):
                items = line.split()
                cluster = items[1]
                length = items[2]
                identitiy = items[3]
                matching = items[7]
                name = items[8]
                std = items[9]
                if matching == '=':
                    matching = length+'M'
                if cluster in arrange:
                    name_c = name+'*'+identitiy+'*'+matching
                    arrange[cluster].append(name_c)
                else:
                    std_len = str(len(index_seq[std]))
                    std_c = std+'*101.0*'+std_len+'M' #to distinguish standard sequence, we use 101 rather than 100
                    name_c = name+'*'+identitiy+'*'+matching
                    arrange[cluster] = [std_c,name_c]


    w = open(each_file.split('.')[0]+'.cluster', 'w')
    #k : cluster number
    #v : each sequence name with information in cluster
    for k,v in arrange.items():
        if len(v) > criteria-1:
            value = v
            score = []
            match = []
            tmp_list = []

            #to get cluster with more than 5 samples, we check filename of each sequence
            for read in value:
                fileindex = read.split('.')[0]
                tmp_list.append(fileindex)
            tmp_list = sorted(set(tmp_list))
            if len(tmp_list) < criteria:
                continue
            for select in value:
                scr = select.split('*')[2] # match_score
                test = re.findall(r'[0-9]*M|[0-9]*I|[0-9]*D',select)
                if test[0][:-1] == '':
                    test = 0
                else:
                    test = int(test[0][:-1])
                match.append(select.split('*')[2]) # how to match
                score.append(test)
            #depend on score, re-arrange seq-name and matching information
            # this will give std matching information first, so that we can compare other sequence with standard
            value = [x for _,x in sorted(zip(score,value),reverse=True)]
            match = [x for _,x in sorted(zip(score,match),reverse=True)]
            tmp_pt = ''
            #to set cluster with best comparing condition, we note how all of the sequence in cluster match together
            std_count = 1
            for point in match:
                test =re.findall(r'[0-9]*M|[0-9]*I|[0-9]*D',point)
                #if there is no inset-delete comparing
                if std_count == 1:
                    if len(tmp_pt) < int(point.split('M')[0]):
                        tmp_pt = '*'* int(point.split('M')[0])
                    std_count = 0
                else:
                    i = 0
                    replace = []
                    for tt in test:
                        # M,I >> will be shown as *
                        if tt[-1] == 'M' or tt[-1] == 'I':
                            MI = re.split('I|M', tt)[0]
                            if MI == '':
                                MI = '1'
                            MI = int(MI)
                            i += MI # how many match will shown
                        # D >> will be shown as -
                        elif tt[-1] == 'D':
                            D = tt.split('D')[0]
                            if D =='':
                                D = '1'
                            D = int(D)
                            c = 0
                            p =''

                            if i == 0: #when deletion exist at front of sequence
                                qqq = D
                                for z in range(qqq):
                                    #if there is already noted deletion in template, skip rewriting to escape re-writing
                                    if tmp_pt[z] == '-':
                                        D -=1
                                tmp_pt = '-'*D+tmp_pt
                                continue

                            for a in range(len(tmp_pt)):
                                q = tmp_pt[a]
                                #q : current base state,  p : next base state
                                if a+2 <= len(tmp_pt):
                                    p = tmp_pt[a+1]
                                else: #when there is no next state
                                    p = ''
                                if q == '*':
                                    c+=1
                                if c == i: #after finish writing all M,I information
                                    #if there is already noted deletion in template, skip rewriting to escape re-writing
                                    if p == '-':
                                        D -=1
                                    else:#insert deletion information
                                        fin_pt = tmp_pt[:a+1]+'-'*D+tmp_pt[a+1:]
                            #note and update the template status by other sequence in cluster
                            tmp_pt =fin_pt
            new_value = []
            for read in value:
                seq_sel = read.split('*')[0]
                point = read.split('*')[2]
                seq = index_seq[seq_sel]
                test = re.findall(r'[0-9]*M|[0-9]*I|[0-9]*D',point)
                seq_result = ''
                length = 0
                qwe = 0
                seq_tmp = ''

                #write sequence information based on matching information
                # ex) IIIIIIMMMMMMDMMMM for 6I6MD4M
                for tt in test:
                    if tt[-1] == 'I':
                        I = re.split('I', tt)[0]
                        if I == '':
                            I = 1
                        I = int(I)
                        seq_tmp += 'I'*I

                    elif tt[-1] == 'M':
                        M = re.split('M', tt)[0]
                        if M == '':
                            M = 1
                        M = int(M)
                        seq_tmp += 'M'*M

                    elif tt[-1] == 'D':
                        D = re.split('D', tt)[0]
                        if D == '':
                            D = 1
                        D = int(D)
                        seq_tmp += 'D'*D
                seq_count = 0
                tmp_count = 0

                #write sequence on template
                for test_letter in tmp_pt:
                    if tmp_count == len(seq_tmp):
                        continue
                    if seq_tmp[tmp_count] == 'D':
                        seq_result += seq[seq_count]
                        tmp_count +=1
                        seq_count +=1
                    elif test_letter == '*' and seq_tmp[tmp_count] == 'M':
                        seq_result += seq[seq_count]
                        tmp_count +=1
                        seq_count +=1
                    elif test_letter == '*' and seq_tmp[tmp_count] == 'I':
                        seq_result += '-'
                        tmp_count +=1
                    else:
                        seq_result += '-'

                seq_result = seq_result.ljust(len(tmp_pt),'-')
                name = read.split('*')[0] + '*' + read.split('*')[1] + '*' + read.split('*')[2]
                name = name.ljust(70)
                new_value.append(name+seq_result)
            w.write('cluster#'+k.ljust(62) + tmp_pt + '\n')
            new_value.sort()
            for nv in new_value:
                w.write(nv + '\n')
    w.write('cluster end')

