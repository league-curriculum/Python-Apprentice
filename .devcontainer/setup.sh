#!/bin/bash

pip3 install --upgrade pip
pip3 install  -r requirements.txt

git config --global pull.rebase true

echo "export PYTHONPATH=$(pwd)/.lib/:$PYTHONPATH" >> ~/.zshrc
echo "export PYTHONPATH=$(pwd)/.lib/:$PYTHONPATH" >> ~/.bashrc
echo "export PYTHONPATH=$(pwd)/.lib/:$PYTHONPATH" >> ~/.profile

source ~/.bashrc


