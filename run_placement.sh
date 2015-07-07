#!/bin/bash -x

sample=$1
phylo_positions=$2
vcf_file=$3

samtools view -h alignments/${sample}_PAO1.sorted.bam | python /mnt/phatso/josh/nanopore_readplacer/get_alleles_from_sam.py ${sample} ${phylo_positions} ${vcf_file} fast_genotyping/${sample}.fasta > fast_genotyping/$sample.report.txt

