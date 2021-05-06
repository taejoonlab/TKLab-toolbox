#!/bin/bash

# If bioconda is not added on your channel, run the following command first. 
# conda config --add channels bioconda


conda install -c bioconda blat ucsc-bedGraphToBigWig ucsc-bedSort ucsc-bedClip \
              ucsc-faSplit ucsc-liftUp ucsc-axtChain ucsc-twoBitInfo ucsc-faToTwoBit \
              ucsc-chainMergeSort ucsc-chainSplit ucsc-chainNet ucsc-netChainSubset 

conda install -c bioconda blast exonerate

# Not sure, but diamond is installed up-to-date version without channel setting.
# Make sure that conda-forge and bioconda channels are set.

conda install diamond

conda install -c bioconda fasttree mafft muscle
