#!/bin/bash

opt_root=$HOME/opt

# Create a directory
mkdir -p ${opt_root} && cd ${opt_root}

# Download gffread
# http://ccb.jhu.edu/software/stringtie/gff.shtml
wget http://ccb.jhu.edu/software/stringtie/dl/gffread-0.12.7.Linux_x86_64.tar.gz

# Uncompress downloaded file
tar -zxvf gffread-0.12.7.Linux_x86_64.tar.gz
