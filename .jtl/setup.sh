#!/bin/bash

TARGET_DIR=$1

THIS_DIR=$(dirname "$(realpath "$0")")

cd $TARGET_DIR

(
    cd $TARGET_DIR && \
    python -mvenv .venv && \
    source .venv/bin/activate && \
    python -mpip install --upgrade pip && \
    pip3 install  -r .jtl/requirements.txt
)

git config --global pull.rebase true

# Put a newline in the prompt to make it easier to read.
echo "export PYTHONPATH=$(pwd)/.lib/:$PYTHONPATH" >> ~/.bashrc
echo 'export PS1="${PS1}\n$ "' >> ~/.bashrc

# Install workspace settings. 
cp $THIS_DIR/settings-student.json $TARGET_DIR/.vscode/settings.json