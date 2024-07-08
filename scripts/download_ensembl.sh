#!/bin/bash

release_dir=$HOME/data/ensembl/release-112

# Create a directory
mkdir -p ${release_dir} && cd ${release_dir}

# Download primary assembly of human genome sequence
# https://ftp.ensembl.org/pub/release-112/fasta/homo_sapiens/dna/
wget ftp://ftp.ensembl.org/pub/release-112/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz
gunzip -c Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz > Homo_sapiens.GRCh38.dna.primary_assembly.fa

# Download gene annotation data
# https://ftp.ensembl.org/pub/release-112/gtf/homo_sapiens/
wget ftp://ftp.ensembl.org/pub/release-112/gtf/homo_sapiens/Homo_sapiens.GRCh38.112.chr.gtf.gz
gunzip -c Homo_sapiens.GRCh38.112.chr.gtf.gz > Homo_sapiens.GRCh38.112.chr.gtf
