#!/bin/bash

# Download and install pyenv
curl https://pyenv.run | bash

# Append the following lines to .bashrc
# -----
# export PYENV_ROOT="$HOME/.pyenv"
# [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
# eval "$(pyenv init -)"
# eval "$(pyenv virtualenv-init -)"

# Install python 3.11.8
pyenv install 3.11.8

# Create a virtual environment using python 3.11.8
pyenv virtualenv 3.11.8 py311

# Apply a virtual environment to the specific folder
cd seolab-ngs-tutorial
pyenv local py311
