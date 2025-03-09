#!/bin/bash
set -x

TARGET_DIR=$1

THIS_DIR=$(dirname "$(realpath "$0")")

echo "❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖"
echo "TARGET_DIR: $TARGET_DIR"
echo "THIS_DIR: $THIS_DIR"

cd $TARGET_DIR

# Create a virtual environment and install the requirements.
(
    cd $TARGET_DIR && \
    python -mvenv .venv && \
    source .venv/bin/activate && \
    python -mpip install --upgrade pip && \
    pip3 install  -r $THIS_DIR/requirements.txt
)

# Git will ask how you want to merge when you pull, 
# and it's confusing to students. 
git config --global pull.rebase true

# Put a newline in the prompt to make it easier to read.
echo "export PYTHONPATH=$(pwd)/.lib/:$PYTHONPATH" >> ~/.bashrc
echo 'export PS1="${PS1}\n$ "' >> ~/.bashrc

# Install workspace settings. 
cp $THIS_DIR/settings-student.json $TARGET_DIR/.vscode/settings.json