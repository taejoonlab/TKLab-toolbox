#!/usr/bin/env python
import os
import sys

## A name of directory containing 'path:...' file
## You can download them using 'make-wget_pathway.sh' script

dir_name = sys.argv[1]

f_summary = open('%s.summary'%dir_name,'w')
f_genes = open('%s.genes'%dir_name,'w')
f_compounds = open('%s.compounds'%dir_name,'w')

gene_total = []
for filename in os.listdir( dir_name ):
    if( not filename.startswith('path:') ):
        continue
    #sys.stderr.write('Read %s ... '%filename)

    path_id = ''
    path_name = ''
    gene_list = []
    comp_list = []

    prev_tag = ''
    f = open(os.path.join(dir_name,filename),'r')
    for line in f:
        tmp_tag = line[:11].strip()
        if( tmp_tag == 'ENTRY' ):
            path_id = line.strip().split()[1]
        if( tmp_tag == 'NAME' ):
            path_name = line[11:].split(' - ')[0].strip()

        if( tmp_tag == 'COMPOUND' ):
            comp_list.append( line[11:].strip().split()[0] )
            f_compounds.write('path:%s\t%s\n'%(path_id,line[11:].strip()))
        elif( tmp_tag == '' and prev_tag == 'COMPOUND' ):
            comp_list.append( line[11:].strip().split()[0] )
            f_compounds.write('path:%s\t%s\n'%(path_id,line[11:].strip()))
        elif( tmp_tag == 'GENE' ):
            gene_list.append( line[11:].strip().split()[0] )
            f_genes.write('path:%s\t%s\n'%(path_id,line[11:].strip()))
            #print line[11:].strip()
        elif( tmp_tag == '' and prev_tag == 'GENE' ):
            gene_list.append( line[11:].strip().split()[0] )
            f_genes.write('path:%s\t%s\n'%(path_id,line[11:].strip()))
            #print line[11:].strip()

        if( tmp_tag != '' ):
            prev_tag = tmp_tag
    f.close()       

    if( len(gene_list) == 0 ):
        sys.stderr.write('//SKIP// %s(%d) %s\n'%(path_id, len(gene_list), path_name))
        continue
    f_summary.write('path:%s\t%s\t%d\t%d\n'%(path_id, path_name, len(gene_list), len(comp_list)))

f_summary.close()
f_genes.close()
f_compounds.close()

