#!/bin/bash

opt_root=$HOME/opt

# Create a directory
mkdir -p ${opt_root} && cd ${opt_root}

# Download SRAtoolkit
wget https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/3.1.0/sratoolkit.3.1.0-ubuntu64.tar.gz

# Uncompress downloaded file
tar -zxvf sratoolkit.3.1.0-ubuntu64.tar.gz
