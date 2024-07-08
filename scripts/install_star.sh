#!/bin/bash

opt_root=$HOME/opt

# Create a directory
mkdir -p ${opt_root}
cd ${opt_root}

# Download STAR aligner
wget https://github.com/alexdobin/STAR/releases/download/2.7.10b/STAR_2.7.10b.zip

# Uncompress downloaded file
unzip STAR_2.7.10b.zip
