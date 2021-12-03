#!/bin/bash
# Install homer via CONDA
# $ conda install -c bioconda homer

# Change the following filenames
TAGS_T="tags.MyTf"
TAGS_I="tags.MyCtrl"

findPeaks $TAGS_T -style factor -o auto -i $TAGS_I

# If you want to call the peak without input control (not recommended), 
# use the following command.

#findPeaks $TAGS_T -style factor -o auto 
