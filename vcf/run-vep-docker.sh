#!/bin/bash

# Docker installation
# docker pull ensemblorg/ensembl-vep

# Install cache
# docker run -t -i -v /work/docker/vep_data:/opt/vep/.vep ensemblorg/ensembl-vep perl INSTALL.pl -a cfp -s homo_sapiens -y GRCh38 -g all

# Launch the VEP docker by default
# docker run -t -i ensemblorg/ensembl-vep ./vep

# Launch the VEP docker with user data at /work/docker/vep_data
docker run -t -i -v /work/docker/vep_data:/opt/vep/.vep ensemblorg/ensembl-vep

