#!/bin/bash

opt_root=$HOME/opt

# Create a directory
mkdir -p ${opt_root} && cd ${opt_root}

# Download pre-compiled version of salmon
# https://github.com/COMBINE-lab/salmon/releases/tag/v1.10.0
wget https://github.com/COMBINE-lab/salmon/releases/download/v1.10.0/salmon-1.10.0_linux_x86_64.tar.gz

# Uncompress downloaded file and rename directory
tar -zxvf salmon-1.10.0_linux_x86_64.tar.gz
mv salmon-latest_linux_x86_64 salmon-1.10.0
