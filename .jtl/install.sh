#!/bin/bash

# Install required extensions. Not in the setup.sh 
# because this is much better to do in the Dockerfile.

code --extensions-dir /app/extensions \
--install-extension "ms-python.python" \
--install-extension "ms-python.vscode-pylance" \
--install-extension "ms-python.autopep8" \
--install-extension "ms-python.debugpy" \
--install-extension "ms-python.isort" \
--install-extension "ms-toolsai.jupyter" 

echo "export PYTHONPATH=$(pwd)/.lib/:$PYTHONPATH" >> ~/.bashrc

source ~/.bashrc
