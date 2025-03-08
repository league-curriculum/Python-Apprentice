#!/bin/bash

TARGET_DIR=$1

THIS_DIR=$(dirname "$(realpath "$0")")

cd $TARGET_DIR


(
    cd ../ && \
    python -mvenv .venv && \
    source .venv/bin/activate && \
    python -mpip install --upgrade pip && \
    pip3 install  -r requirements.txt
)

git config --global pull.rebase true

# Put a newline in the prompt to make it easier to read.
echo "export PYTHONPATH=$(pwd)/.lib/:$PYTHONPATH" >> ~/.bashrc
echo 'export PS1="${PS1}\n$ "' >> ~/.bashrc

# Install workspace settings. 
cp $THIS_DIR/.jtl/settings-student.json .vscode/settings.json