i=$1

bwa mem reference/NC_002516.fasta <(zcat /mnt/phatso/alnQC/plate65/DH_Pseudomonas/1/${i}_1_trimmed.fastq.gz /mnt/phatso/alnQC/plate65/DH_Pseudomonas/2/${i}_1_trimmed.fastq.gz) <(zcat /mnt/phatso/alnQC/plate65/DH_Pseudomonas/1/${i}_2_trimmed.fastq.gz /mnt/phatso/alnQC/plate65/DH_Pseudomonas/2/${i}_2_trimmed.fastq.gz) | samtools view -bS - | samtools sort - alignments/${i}_PAO1.sorted

samtools index alignments/${i}_PAO1.sorted.bam
