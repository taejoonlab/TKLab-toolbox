STAR --genomeLoad Remove --genomeDir ~/pub/db.star/HUMAN_ens85_dna_sm

for FQ1 in $(ls ../fastq/*untie_1.fastq.gz)
do
  FQ2=${FQ1/untie_1/untie_2}
  OUT=$(basename $FQ1)
  OUT=${OUT/.untie_1.fastq.gz/}"."
  STAR --genomeDir ~/pub/db.star/HUMAN_ens85_dna_sm --runThreadN 16 --readFilesIn $FQ1 $FQ2 --readFilesCommand zcat --outSAMtype BAM SortedByCoordinate --outFileNamePrefix $OUT --limitBAMsortRAM 50000000000
done

