import sys, os, re

folder = sys.argv[1]

def selected_file_list(input_dir):
    file_list = []
    input_file_list = os.listdir(input_dir)
    for input_file in input_file_list:
        if input_file[:5] == 'TKLab':
            file_list.append(input_file)
    return file_list
    
# create fastq file list in selected folder
file_list = selected_file_list(folder)
for afile in file_list:
    with open(folder + afile,'r') as f:
        line_count = 0
        target = 100000
        selectcount = 1
        header_seq = {}
        writing = open('arrange_'+afile.replace('TKLab201808_HYLSUgbs_',''), 'w')
        print afile + ' Now running...'
        for line in f:
            #header
            if selectcount == 1:
                line_count += 1
                if line_count == target:
                    print line_count 
                    target += 100000
                header = re.split('@|:|_|/| |\n',line)
                name = header[8]+'U_'+header[4]+'_'+header[5]+'_'+header[6]+'_'+header[7]
                selectcount += 1
                

            #sequence
            elif selectcount == 2:
                selectcount +=1
                l = line.strip()
                if l[0:4] == 'GATC' or l[0:3] == 'TAG':
                    writing.write(name + '\n>' + l + '\n')

            #qual
            elif selectcount == 3:
                selectcount +=1
                
            elif selectcount == 4:
                selectcount = 1
                
            
