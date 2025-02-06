#!/bin/bash

pip3 install --upgrade pip
pip3 install  -r requirements.txt

git config --global pull.rebase true

code --extensions-dir /app/extensions \
--install-extension "ms-python.python" \
--install-extension "ms-python.vscode-pylance" \
--install-extension "ms-python.autopep8" \
--install-extension "ms-python.debugpy" \
--install-extension "ms-python.isort" \
--install-extension "ms-toolsai.jupyter" 

echo "export PYTHONPATH=$(pwd)/.lib/:$PYTHONPATH" >> ~/.bashrc

source ~/.bashrc
