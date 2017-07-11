#!/bin/bash

## Install conda
if [ -x "$(command -v conda)" ]; then
  echo "conda is avilalbe. Skip installation."
else
  echo "Install the latest Miniconda3"
  MINICONDA_INSTALLER="Miniconda3-latest-Linux-x86_64.sh"
  wget https://repo.continuum.io/miniconda/$MINICONDA_INSTALLER
  chmod 755 $MINICONDA_INSTALLER
  ./$MINICONDA_INSTALLER
  rm $MINICONDA_INSTALLER
fi

export PATH=$PATH:~/miniconda3/bin/

## Setup Bioconda
conda config --add channels conda-forge
conda config --add channels defaults
conda config --add channels r
conda config --add channels bioconda

## Install packages
conda install bowtie bowtie2 star bwa gmap \
              samtools bedtools \
              bioconductor-deseq2 bioconductor-deseq bioconductor-edger \
              homer \
              blat ucsc-bedGraphToBigWig ucsc-bedSort ucsc-bedClip \
              ucsc-faSplit ucsc-liftUp ucsc-axtChain ucsc-twoBitInfo ucsc-faToTwoBit \
              ucsc-chainMergeSort ucsc-chainSplit ucsc-chainNet ucsc-netChainSubset \
              blast exonerate

## Install Python2
PYTHON2_AVAILABLE=0
for CONDA_ENV in $(conda env list)
do
  if [ $CONDA_ENV == 'py2' ]; then
    PYTHON2_AVAILABLE=1
    echo "Python2 is available. Skip installation."
  fi
done

if [ ! $PYTHON2_AVAILABLE ]; then
  echo "Install Python2"
  conda create -n py2 python=2.7
fi

## Packages with Python2
source activate py2
conda install macs2
source deactivate py2
