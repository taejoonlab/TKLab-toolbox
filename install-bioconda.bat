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
