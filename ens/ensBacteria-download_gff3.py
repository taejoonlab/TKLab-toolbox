#!/usr/bin/env python3
import os
import sys
from ftplib import FTP

ens_version = 37

ftp_url = 'ftp.ensemblgenomes.org'
filename_txt = 'species_EnsemblBacteria.txt'

root_dir_local = '/home/taejoon/pub/ens.bacteria/%d'%ens_version
root_dir_fasta = '/pub/bacteria/release-%d/fasta'%ens_version
root_dir_gff3 = '/pub/bacteria/release-%d/gff3'%ens_version

#name	species	division	taxonomy_id	assembly	assembly_accession	genebuild	variation	pan_compara	peptide_compara	genome_alignments	other_alignments	core_db	species_id

ftp = FTP(ftp_url)
ftp.login()

count_taxa = 0
count_dubious_taxa = 0
f_txt = open(filename_txt,'r') 
for line in f_txt:
    tokens = line.strip().split("\t")
    count_taxa += 1

    species_name = tokens[0]

    if species_name.startswith("'") or species_name.startswith("["):
        count_dubious_taxa += 1
        continue
    if species_name[0].isupper() == False:
        count_dubious_taxa += 1
        continue
    
    genus_name = species_name.split()[0]
    species_code = tokens[1]

    tmp_dir_local = '%s/%s'%(root_dir_local, genus_name)
    if not os.access(tmp_dir_local, os.R_OK):
        os.mkdir(tmp_dir_local)

    tax_id = tokens[3]
    assembly_id = tokens[4]
    assembly_acc = tokens[5]
    core_db = tokens[-2]
    #print(species_name, species_div, tax_id, assembly_id, assembly_acc, core_db)
    dirname_gff3 = '%s/%s/%s/'%(root_dir_gff3,core_db.split('_core_')[0],species_code)
    filename_gff3 = '%s.%s.%d.gff3.gz'%(species_code.capitalize(),assembly_id,ens_version)

    filename_gff3 = filename_gff3.replace(' ','_').replace('#','_')
    if filename_gff3.find('_of_') >= 0:
        sys.stderr.write('Premature info. - %s\n'%assembly_id)
        continue

    filename_gff3_local = os.path.join(tmp_dir_local, filename_gff3)

    if os.access(filename_gff3_local, os.R_OK):
        sys.stderr.write('Already downloaded. %s\n'%filename_gff3_local)
    else:
        ftp.cwd(dirname_gff3)
        sys.stderr.write('Access %s/%s\n'%(dirname_gff3, filename_gff3))
        try:
            ftp.retrbinary('RETR %s'%filename_gff3, open(os.path.join(tmp_dir_local,filename_gff3),'wb').write)
            sys.stderr.write('Download %s to %s\n'%(filename_gff3, tmp_dir_local))
        except:
            sys.stderr.write("Not available. %s\n"%filename_gff3)
f_txt.close()
ftp.quit()

sys.stderr.write("Total taxa: %d, Dubious taxa (skipped): %d\n"%(count_taxa, count_dubious_taxa))
