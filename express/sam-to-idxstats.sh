#!/bin/bash
NUM_THREADS=8

for SAM in $(ls *sam)
do
  BAM=${SAM/.sam/}".bam"
  SORTED_BAM=${SAM/.sam/}".sorted.bam"
  IDXSTATS=${SAM/.sam/}".idxstats"

  if [ -e $IDXSTATS ]; then
    echo "Skip $SAM"
  else
    echo "Make $IDXSTATS"
    samtools view -bS -@ $NUM_THREADS -o $BAM -O BAM $SAM
    samtools sort -@ $NUM_THREADS -o $SORTED_BAM -O BAM $BAM
    samtools index $SORTED_BAM
    samtools idxstats $SORTED_BAM > $IDXSTATS
  fi
done
