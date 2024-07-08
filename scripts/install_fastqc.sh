#!/bin/bash

opt_root=$HOME/opt

# Create a directory
mkdir -p ${opt_root} && cd ${opt_root}

# Install java runtime environment (JRE) if not exists
sudo apt install default-jre

# Check java version
java -version

# Download and uncompress FastQC application
wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.12.1.zip
unzip fastqc_v0.12.1.zip
