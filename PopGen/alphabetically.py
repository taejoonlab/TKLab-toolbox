import sys, os, re
folder = sys.argv[1]

def make_file_list(input_dir):
    file_list = []
    input_file_list = os.listdir(input_dir)
    for input_file in input_file_list:
        if input_file[:3] == 'mms':
            file_list.append(input_file)
    return file_list
#make file list
file_list = make_file_list(folder)

for each_file in file_list:
	with open(folder + each_file,'r') as f:
		print each_file +' is now processed ...'
		linecount = 0
		name = ''
		uniq_dict = {}
		for line in f:
			tmp = line.strip()
			if name == '': # tmp is name
				name = tmp
			else:          # tmp is sequence
				uniq_dict[name] = tmp
				name = ''
				linecount += 1
				if linecount % 100000 == 0:
					print linecount
        #order keys depend on sequence (alphabetically)
		sorted_key = sorted(uniq_dict, key=lambda k: uniq_dict[k])
		sel_file = open('abc_'+each_file,'w')
		check = 0
		for key in sorted_key:
			sel_file.write(key + '\n' + uniq_dict[key] + '\n')


