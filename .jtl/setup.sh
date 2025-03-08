#!/bin/bash

TARGET_DIR=$1

THIS_DIR=$(dirname "$(realpath "$0")")

cd $TARGET_DIR

pip3 install --upgrade pip
pip3 install  -r requirements.txt

git config --global pull.rebase true

# Put a newline in the prompt to make it easier to read.
echo "export PYTHONPATH=$(pwd)/.lib/:$PYTHONPATH" >> ~/.bashrc
echo 'export PS1="${PS1}\n$ "' >> ~/.bashrc



cp $THIS_DIR/.jtl/ ~/.bash_aliases