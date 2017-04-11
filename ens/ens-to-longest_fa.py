#!/usr/bin/env python
import os
import sys
import gzip

query_prefix = sys.argv[1]

is_clean = 0
if( len(sys.argv) > 2 and sys.argv[2] == 'clean' ):
    is_clean = 1

## GTF snip
#>ENST00000415118 havana_ig_gene:known chromosome:GRCh38:14:22438547:22438554:1 gene:ENSG00000223997 gene_biotype:TR_D_gene transcript_biotype:TR_D_gene

sp_code = dict()
dirname_base = os.path.dirname( os.path.realpath(__file__) )
f_list = open(os.path.join(dirname_base,'ens_species.txt'),'r')
for line in f_list:
    if( line.startswith('#') ):
        continue
    tmp_tokens = line.strip().split()
    sp_code[ tmp_tokens[1].capitalize() ] = tmp_tokens[0]
f_list.close()

def read_fa(filename):
    seq_h = ''
    seq_list = dict()
    f = open(filename,'r')
    if( filename.endswith('.gz') ):
        f = gzip.open(filename,'rb')
    for line in f:
        if( line.startswith('>') ):
            seq_h = line.strip().split()[0].lstrip('>')
            seq_list[seq_h] = []
        else:
            seq_list[seq_h].append(line.strip())
    f.close()
    return seq_list

def read_gtf(filename):
    rv = {'gene':dict(), 'tx':dict(), 'prot':dict(), 'gene_count':dict()}
    genome_version = 'Unknown'
    f = open(filename,'r')
    if( filename.endswith('.gz') ):
        f = gzip.open(filename,'rb')
    for line in f:
        if( line.startswith('#!genome-version') ):
            genome_version = line.strip().split()[1]
            continue
        elif( line.startswith('#!') ):
            continue

        tokens = line.strip().split("\t")
        chr_id = tokens[0]
        chr_pos = '%s:%s:%s:%s:%d'%(genome_version,chr_id,tokens[3],tokens[4],int('%s1'%tokens[6]))
        if( not rv['gene_count'].has_key(chr_id) ):
            rv['gene_count'][chr_id] = 0

        if( tokens[2] == 'CDS' or tokens[2] == 'transcript' or tokens[2] == 'gene' ):
            gene_id = 'NA'
            transcript_id = 'NA'
            protein_id = 'NA'
            gene_name = 'NA'

            for tmp in tokens[8].split(';'):
                tmp = tmp.strip()
                if( tmp.startswith('gene_id') ):
                    gene_id = tmp.split()[1].replace('"','')
                if( tmp.startswith('transcript_id') ):
                    transcript_id = tmp.split()[1].replace('"','')
                if( tmp.startswith('gene_name') ):
                    #gene_name = tmp.split()[1].replace('"','')
                    gene_name = tmp.replace('gene_name ','').replace('"','').replace(' ','').replace('(','_').replace(')','').replace(':','_')
                if( tmp.startswith('protein_id') ):
                    protein_id = tmp.split()[1].replace('"','')

            if( tokens[2] == 'gene' ):
                rv['gene_count'][chr_id] += 1
                if( not rv['gene'].has_key(gene_id) ):
                    rv['gene'][gene_id] = {'chr_pos':chr_pos, 'gene_name':gene_name, 'tx_list':[], 'prot_list':[]}
                else:
                    rv['gene'][gene_id]['chr_pos'] = chr_pos

            if( tokens[2] == 'transcript' ):
                rv['tx'][transcript_id] = {'chr_pos':chr_pos, 'gene_name':gene_name, 'gene_id':gene_id, 'prot_list':[]}
                if( not rv['gene'].has_key(gene_id) ):
                    rv['gene'][gene_id] = {'chr_pos':chr_pos, 'gene_name':gene_name, 'tx_list':[], 'prot_list':[]}
                rv['gene'][gene_id]['tx_list'].append(transcript_id)
            
            if( tokens[2] == 'CDS' ):
                rv['prot'][protein_id] = {'chr_pos':chr_pos, 'gene_name':gene_name, 'gene_id':gene_id, 'tx_id':transcript_id}
                if( not rv['gene'].has_key(gene_id) ):
                    rv['gene'][gene_id] = {'chr_pos':chr_pos, 'gene_name':gene_name, 'tx_list':[], 'prot_list':[]}
                rv['gene'][gene_id]['prot_list'].append(protein_id)
                if( not rv['tx'].has_key(transcript_id) ):
                    rv['tx'][transcript_id] = {'chr_pos':chr_pos, 'gene_name':gene_name, 'gene_id':gene_id, 'prot_list':[]}
                rv['tx'][transcript_id]['prot_list'].append(protein_id)
    return rv

with_gtf = 0
for filename_gtf in os.listdir('.'):
    if( not filename_gtf.startswith(query_prefix) ):
        continue
    
    if( not filename_gtf.endswith('.gtf.gz') ):
        continue
    
    with_gtf = 1
    filename_tokens = filename_gtf.split('.')
    filename_base = '.'.join(filename_tokens[:-3])
    filename_cdna = '%s.cdna.all.fa.gz'%(filename_base)
    filename_ncrna = '%s.ncrna.fa.gz'%(filename_base)
    filename_prot = '%s.pep.all.fa.gz'%(filename_base)

    out_sp_code = filename_tokens[0]
    if( sp_code.has_key(out_sp_code) ):
        out_sp_code = sp_code[out_sp_code]
    out_version = filename_tokens[-3]

    f_log = open('%s_ens%s.log'%(out_sp_code,out_version),'w')
    f_cdna = open('%s_ens%s_cdna_longest.fa'%(out_sp_code,out_version),'w')
    f_ncdna = open('%s_ens%s_ncdna_longest.fa'%(out_sp_code,out_version),'w')
    f_tx = open('%s_ens%s_tx_longest.fa'%(out_sp_code,out_version),'w')
    f_prot = open('%s_ens%s_prot_longest.fa'%(out_sp_code,out_version),'w')

    sys.stderr.write('Read %s ...'%filename_gtf)
    f_log.write('#Read %s ...'%filename_gtf)
    rv_gtf = read_gtf(filename_gtf)
    gene_list = sorted(rv_gtf['gene'].keys())
    sys.stderr.write('Done (%d genes; %d transcripts; %d proteins)\n'%(len(gene_list), len(rv_gtf['tx'].keys()), len(rv_gtf['prot'].keys())))
    f_log.write('Done (%d genes; %d transcripts; %d proteins)\n'%(len(gene_list), len(rv_gtf['tx'].keys()), len(rv_gtf['prot'].keys())))

    sys.stderr.write('Read %s ... '%filename_cdna)
    f_log.write('#Read %s ... '%filename_cdna)
    seq_cdna = read_fa(filename_cdna)
    sys.stderr.write('Done (%d sequences)\n'%len(seq_cdna))
    f_log.write('Done (%d sequences)\n'%len(seq_cdna))

    sys.stderr.write('Read %s ... '%filename_ncrna)
    f_log.write('#Read %s ... '%filename_ncrna)
    seq_ncrna = read_fa(filename_ncrna)
    sys.stderr.write('Done (%d sequences)\n'%len(seq_ncrna))
    f_log.write('Done (%d sequences)\n'%len(seq_ncrna))

    sys.stderr.write('Read %s ... '%filename_prot)
    f_log.write('#Read %s ... '%filename_prot)
    seq_prot = read_fa(filename_prot)
    sys.stderr.write('Done (%d sequences)\n'%len(seq_prot))
    f_log.write('Done (%d sequences)\n'%len(seq_prot))

    pos2gene = dict()
    for gene_id in gene_list:
        tmp_pos = rv_gtf['gene'][gene_id]['chr_pos']
        tmp_chr = tmp_pos.split(':')[1]
        if( is_clean > 0 ):
            if( not rv_gtf['gene_count'].has_key(tmp_chr) ):
                sys.stderr.write('[clean] No gene count: %s\n'%tmp_chr)
                f_log.write('ChrNoGene\tchr:%s\n'%tmp_chr)
                continue
            else:
                tmp_count = rv_gtf['gene_count'][tmp_chr]
                if( tmp_chr != 'MT' and tmp_count < 500 ):
                    #sys.stderr.write('[clean] gene on a patched chromosome: %s\n'%gene_id)
                    f_log.write('ChrClean\tchr:%s\tgene:%s\n'%(tmp_chr,gene_id))
                    continue
                    
        if( not pos2gene.has_key(tmp_pos) ):
            pos2gene[tmp_pos] = []
        pos2gene[tmp_pos].append(gene_id)

    count_noTx = 0
    count_cdna = 0
    count_ncdna = 0
    for tmp_pos in sorted(pos2gene.keys()):
        if( len(pos2gene[tmp_pos]) > 1 ):
            f_log.write('GeneMulti\t%s\t%s\n'%(tmp_pos, ';'.join(sorted(pos2gene[tmp_pos]))))
        
        tmp_tx2gene = dict()
        tmp_tx_seq = dict()
        tmp_tx_len = dict()
        tmp_prot_seq = dict()
        tmp_prot_len = dict()
        for gene_id in pos2gene[tmp_pos]:
            gene_name = rv_gtf['gene'][gene_id]['gene_name']

            for tx_id in rv_gtf['gene'][gene_id]['tx_list']:
                tmp_tx2gene[tx_id] = {'gene_id':gene_id, 'gene_name':gene_name}
                tmp_nseq = ''
                if( seq_cdna.has_key(tx_id) ):
                    tmp_nseq = ''.join(seq_cdna[tx_id])
                elif( seq_ncrna.has_key(tx_id) ):
                    tmp_nseq = ''.join(seq_ncrna[tx_id])
                
                if( tmp_nseq == '' ):
                    count_noTx += 1
                    f_log.write('TxNoSeq\ttx:%s\tgene:%s\tname:%s\n'%(tx_id,gene_id,gene_name))
                else:
                    tmp_tx_seq[tx_id] = tmp_nseq
                    tmp_tx_len[tx_id] = len(tmp_nseq)
                
                if( rv_gtf['tx'].has_key(tx_id) ):
                    for prot_id in rv_gtf['tx'][tx_id]['prot_list']:
                        tmp_pseq = ''
                        if( seq_prot.has_key(prot_id) ):
                            tmp_pseq = ''.join(seq_prot[prot_id])
                        if( tmp_pseq == '' ):
                            count_noPep += 1
                            f_log.write('ProtNoSeq\tprot:%s\ttx:%s\tgene:%s\tname:%s\n'%(prot_id,tx_id,gene_id,gene_name))
                        else:
                            tmp_prot_seq[prot_id] = tmp_pseq
                            tmp_prot_len[prot_id] = len(tmp_pseq)

        if( len(tmp_tx_seq) == 0 ):
            tmp_gene_id = ';'.join(sorted(pos2gene[tmp_pos]))
            f_log.write('GeneNoTx\tgene:%s\n'%(tmp_gene_id))
            continue

        if( len(tmp_prot_len) > 0 ):
            prot_sorted = sorted(tmp_prot_len.keys(), key=tmp_prot_len.get, reverse=True)
            longest_prot_len = tmp_prot_len[prot_sorted[0]]
            longest_tx_len = 0
            longest_tx_id = 0
            longest_prot_id = 0
            for tmp_prot_id in [x for x in prot_sorted if tmp_prot_len[x] == longest_prot_len]:
                tmp_tx_id = rv_gtf['prot'][tmp_prot_id]['tx_id']
                if( tmp_tx_len[tmp_tx_id] > longest_tx_len ):
                    longest_tx_len = tmp_tx_len[tmp_tx_id]
                    longest_tx_id = tmp_tx_id
                    longest_prot_id = tmp_prot_id
            
            #if( longest_tx_id == rv_gtf['prot'][longest_prot_id]['tx_id'] ):
            gene_id = tmp_tx2gene[longest_tx_id]['gene_id']
            gene_name = tmp_tx2gene[longest_tx_id]['gene_name']
            f_tx.write('>%s|%s gene:%s prot:%s\n%s\n'%(gene_name,longest_tx_id,gene_id,longest_prot_id,tmp_tx_seq[longest_tx_id]))
            f_cdna.write('>%s|%s gene:%s prot:%s\n%s\n'%(gene_name,longest_tx_id,gene_id,longest_prot_id,tmp_tx_seq[longest_tx_id]))
            f_prot.write('>%s|%s gene:%s tx:%s\n%s\n'%(gene_name,longest_prot_id,gene_id,longest_tx_id,tmp_prot_seq[longest_prot_id]))
            count_cdna += 1
        else:
            tx_sorted = sorted(tmp_tx_len.keys(), key=tmp_tx_len.get, reverse=True)
            longest_tx_id = tx_sorted[0]
            gene_id = tmp_tx2gene[longest_tx_id]['gene_id']
            gene_name = tmp_tx2gene[longest_tx_id]['gene_name']
            f_tx.write('>%s|%s gene:%s\n%s\n'%(gene_name,longest_tx_id,gene_id,tmp_tx_seq[longest_tx_id]))
            f_ncdna.write('>%s|%s gene:%s\n%s\n'%(gene_name,longest_tx_id,gene_id,tmp_tx_seq[longest_tx_id]))
            count_ncdna += 1

    f_tx.close()
    f_cdna.close()
    f_ncdna.close()
    f_prot.close()

if( with_gtf > 0 ):
    sys.stderr.write('TxNoSeq: %d\n'%count_noTx)
    sys.stderr.write('cDNA/prot: %d\n'%count_cdna)
    sys.stderr.write('ncDNA: %d\n'%count_ncdna)
    f_log.write('#TxNoSeq: %d\n'%count_noTx)
    f_log.write('#cDNA/prot: %d\n'%count_cdna)
    f_log.write('#ncDNA: %d\n'%count_ncdna)

