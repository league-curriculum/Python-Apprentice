#!/bin/bash
set -x

TARGET_DIR=$1
THIS_DIR=$(dirname "$(realpath "$0")")

# Set extension directory based on whether /vscode exists
if [ -d "/vscode" ]; then
    EXT_DIR="/vscode/extensionsCache/"
else
    EXT_DIR="$THIS_DIR/extensionsCache/"
fi

SYLLABUS_EXTENSION=https://github.com/league-infrastructure/league-vscode-ext/releases/download/v1.20250510.2/jtl-syllabus-v1.20250510.2.vsix

echo "❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖"
echo "TARGET_DIR: $TARGET_DIR"
echo "THIS_DIR: $THIS_DIR"

cd $TARGET_DIR


pip install -r requirements.txt

# Put a newline in the prompt to make it easier to read.
echo "export PYTHONPATH=$(pwd)/.lib/:$PYTHONPATH" >> ~/.bashrc

# Fetch the syllabus extension to /vscode/extensionsCache/
mkdir -p $EXT_DIR
curl -L $SYLLABUS_EXTENSION -o  $EXT_DIR/$(basename $SYLLABUS_EXTENSION)
vsix_file=" $EXT_DIR/$(basename $SYLLABUS_EXTENSION)"
base_name=$(basename "$SYLLABUS_EXTENSION" .vsix)
target_dir="$TARGET_DIR/.vscode/extensions/$base_name"
mkdir -p "$target_dir"
unzip -q "$vsix_file" -d "$target_dir"

