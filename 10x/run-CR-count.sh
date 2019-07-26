ID="scCapSt13"
#FASTQ_DIR="scCapSt13/outs/fastq_path/HWYH7BGX7/"
FASTQ_DIR="scCapSt13/outs/fastq_path/HWYH7BGX7/scCapSt13"
REF="../XENLA_10X/XENLA_GCA001663975v1_XBv9p2"
EXP_CELLS=5000
~/src/10X/cellranger-2.1.1/cellranger count --id=$ID --transcriptome=$REF\
    --fastqs=$FASTQ_DIR --sample=scCapSt13 \
    --chemistry=SC3Pv2 --expect-cells=$EXP_CELLS
