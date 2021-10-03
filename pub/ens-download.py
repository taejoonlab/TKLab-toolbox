#!/usr/bin/env python3

from ftplib import FTP
import sys
import os

usage_mesg = 'ens-download.py <three-digits ensembl version)>'

if len(sys.argv) < 2:
    sys.stderr.write('Usage: %s\n' % usage_mesg)
    sys.exit(1)

release_ver = sys.argv[1]

species_list = []
dirname_base = os.path.dirname(os.path.realpath(__file__))

f_list = open(os.path.join(dirname_base, 'ens_species.txt'), 'r')

for line in f_list:
    if line.startswith('#'):
        continue
    species_list.append(line.strip().split()[1].lower())
f_list.close()

ftp = FTP('ftp.ensembl.org')
ftp.login()


def download_suffix(ftp, tmp_suffix):
    for tmp_filename in ftp.nlst():
        if tmp_filename.endswith(tmp_suffix):
            if os.access(tmp_filename, os.R_OK):
                sys.stderr.write('%s is already downloaded. Skip.\n'
                                 % tmp_filename)
                continue

            sys.stderr.write('Download %s\n' % tmp_filename)
            ftp.retrbinary('RETR %s' % tmp_filename,
                           open(tmp_filename, 'wb').write)


for tmp_sp in species_list:
    if not tmp_sp.startswith('pet'):
        continue

    tmp_dir_gtf = '/pub/release-%03d/gtf/%s/' % (int(release_ver), tmp_sp)
    ftp.cwd(tmp_dir_gtf)
    download_suffix(ftp, '%03d.gtf.gz' % (int(release_ver)))

    tmp_dir_fasta = '/pub/release-%03d/fasta/%s/' % (int(release_ver), tmp_sp)
    ftp.cwd(tmp_dir_fasta)

    ftp.cwd('./cdna')
    download_suffix(ftp, '.cdna.all.fa.gz')

    ftp.cwd('../pep')
    download_suffix(ftp, '.pep.all.fa.gz')

    ftp.cwd('../cds')
    download_suffix(ftp, '.cds.all.fa.gz')

    ftp.cwd('../ncrna')
    download_suffix(ftp, '.ncrna.fa.gz')

# ../79/Anolis_carolinensis.AnoCar2.0.79.gtf.gz
# ../79/Danio_rerio.Zv9.79.gtf.gz
# ../79/Gallus_gallus.Galgal4.79.gtf.gz
# ../79/Homo_sapiens.GRCh38.79.gtf.gz
# ../79/Mus_musculus.GRCm38.79.gtf.gz
# ../79/Oryzias_latipes.MEDAKA1.79.gtf.gz
# ../79/Xenopus_tropicalis.JGI_4.2.79.gtf.gz
