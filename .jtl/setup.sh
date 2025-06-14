#!/bin/bash
set -x

TARGET_DIR=$1
THIS_DIR=$(dirname "$(realpath "$0")")

echo "❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖"
echo "TARGET_DIR: $TARGET_DIR"
echo "THIS_DIR: $THIS_DIR"

cd $TARGET_DIR

pip install -r requirements.txt

# Put a newline in the prompt to make it easier to read.
echo "export PYTHONPATH=$(pwd)/.lib/:$PYTHONPATH" >> ~/.bashrc

