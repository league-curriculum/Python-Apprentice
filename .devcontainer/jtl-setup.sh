#!/bin/bash

pip3 install --upgrade pip
pip3 install  -r requirements.txt

git config --global pull.rebase true

echo "export PYTHONPATH=$(pwd)/.lib/:$PYTHONPATH" >> ~/.bashrc
echo 'export PS1="${PS1}\n$ "' >> ~/.bashrc

# Clean out distracting files we no longer need. 
rm -rf .devcontainer .github .lib requirements.txt LICENSE 
    mv lessons/* .
    rm -rf lessons
    git add -A
    git commit -m "codeserver init"