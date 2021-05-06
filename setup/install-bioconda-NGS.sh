#!/bin/bash

# If bioconda is not added on your channel, run the following command first. 
# conda config --add channels bioconda

## Install packages
# FASTQ-related: trimmomatic, fastqc
# Mappers: bowtie bowtie2 star bwa gmap
# NGS utils: samools bedtools
# Variant analysis: strelka

conda install -c bioconda trimmomatic fastqc flash
conda install -c bioconda  bowtie bowtie2 star bwa gmap
conda install -c bioconda  samtools bedtools

#bioconductor-deseq2 bioconductor-deseq bioconductor-edger \
#homer \
#blat ucsc-bedGraphToBigWig ucsc-bedSort ucsc-bedClip \
#ucsc-faSplit ucsc-liftUp ucsc-axtChain ucsc-twoBitInfo ucsc-faToTwoBit \
#ucsc-chainMergeSort ucsc-chainSplit ucsc-chainNet ucsc-netChainSubset \
#blast exonerate flash
