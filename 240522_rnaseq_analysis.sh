#!/bin/bash

## --- Section 1: Installation ---

# Download pre-compiled SRA toolkit from NCBI
cd ~/opt
wget https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/3.1.0/sratoolkit.3.1.0-ubuntu64.tar.gz
tar -zxvf sratoolkit.3.1.0-ubuntu64.tar.gz
cd sratoolkit.3.1.0-ubuntu64/bin

# Install java runtime environment (JRE) if not exists
sudo apt install default-jre
java -version

# Download and uncompress FastQC application
wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.12.1.zip
unzip fastqc_v0.12.1.zip

# Install and compile STAR from source
wget https://github.com/alexdobin/STAR/archive/2.7.11b.tar.gz
tar -xzf 2.7.11b.tar.gz
cd STAR-2.7.11b
cd STAR/source
make STAR

# Append paths to the analysis tools into PATH
PATH=$PATH:/home/sukjun/opt/sratoolkit.3.1.0-ubuntu64/bin  # sratoolkit
PATH=$PATH:/home/sukjun/opt/fastqc-v0.12.1  # FastQC
PATH=$PATH:/home/sukjun/opt/STAR-2.7.10b/source  # STAR aligner

# --- Section 2: Analysis ---

# Download raw reads
fastq-dump --split-files SRR27922610  # GSM8072137
fastq-dump --split-files SRR27922609  # GSM8072138
fastq-dump --split-files SRR27922608  # GSM8072139
fastq-dump --split-files SRR27922607  # GSM8072140
fastq-dump --split-files SRR27922606  # GSM8072141
fastq-dump --split-files SRR27922605  # GSM8072142

# Check quality of reads by FastQC
fastqc SRR27922610_1.fastq
fastqc SRR27922610_2.fastq
fastqc SRR27922609_1.fastq
fastqc SRR27922609_2.fastq
fastqc SRR27922608_1.fastq
fastqc SRR27922608_2.fastq
fastqc SRR27922607_1.fastq
fastqc SRR27922607_2.fastq
fastqc SRR27922606_1.fastq
fastqc SRR27922606_2.fastq
fastqc SRR27922605_1.fastq
fastqc SRR27922605_2.fastq

# Download primary assembly of human genome sequence
wget ftp://ftp.ensembl.org/pub/release-112/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz

# Download gene annotation data
wget ftp://ftp.ensembl.org/pub/release-112/gtf/homo_sapiens/Homo_sapiens.GRCh38.112.chr.gtf.gz

# Build STAR index
STAR --runMode genomeGenerate \
    --runThreadN 16 \
    --genomeDir Homo_sapiens.GRCh38.star \
    --genomeFastaFiles Homo_sapiens.GRCh38.dna.primary_assembly.fa \
    --sjdbGTFfile Homo_sapiens.GRCh38.112.chr.gtf

# Align reads to human genome GRCh38
sra_run_id=SRR27922610
genome_dir=/home/sukjun/data/ensembl/release-112/Homo_sapiens.GRCh38.star
mkdir -p ${sra_run_id}_star
STAR --runThreadN 16 \
    --genomeDir ${genome_dir} \
    --readFilesIn ${sra_run_id}_1.fastq ${sra_run_id}_2.fastq \
    --outFilterType BySJout \
    --outFilterMultimapNmax 20 \
    --alignSJoverhangMin 8 \
    --alignSJDBoverhangMin 1 \
    --outFilterMismatchNmax 999 \
    --outFilterMismatchNoverReadLmax 0.04 \
    --alignIntronMin 20 \
    --alignIntronMax 1000000 \
    --outFileNamePrefix ${sra_run_id}_star/
