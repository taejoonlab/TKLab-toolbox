#!/bin/bash

BAM_C="<input control bam>"

BAM_T="<ChIP bam>"

NAME="<output name>"

# With input control
macs2 callpeak -f BAM -g hs -n $NAME -t $BAM_T -c $BAM_C -q 0.05

# Without input control
#macs2 callpeak -f BAM -g hs -n $NAME -t $BAM_T -q 0.05
