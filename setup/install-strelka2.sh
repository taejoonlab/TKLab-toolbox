#!/bin/bash

# https://github.com/Illumina/strelka/blob/v2.9.x/docs/userGuide/quickStart.md
# https://github.com/Illumina/strelka/releases

# From the github
# wget https://github.com/Illumina/strelka/releases/download/v2.9.2/strelka-2.9.2.centos6_x86_64.tar.bz2

# From bioconda. It requires python2.7
conda create py2 python=2.7
conda install -c bioconda strelka

