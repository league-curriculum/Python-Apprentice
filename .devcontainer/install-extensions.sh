#!/bin/bash

# List of extensions to install
extensions=(
    "ms-python.python"
    "ms-python.vscode-pylance"
    "ms-python.autopep8"
    "ms-python.debugpy"
    "ms-python.isort"
    "ms-toolsai.jupyter"
)

# Determine the command to use
if command -v code-server &> /dev/null; then
    CODE="code-server"
elif command -v code &> /dev/null; then
    CODE="code"
else
    echo "Error: Neither 'code' (VS Code CLI) nor 'code-server' is installed."
    exit 1
fi
# Function to install extensions
install_extensions() {
    for extension in "${extensions[@]}"; do
        echo "Installing VS Code extension: $extension"
        $CODE --install-extension "$extension" 
    done
}

# Check if VS Code is installed
if ! command -v code &> /dev/null; then
    echo "Error: VS Code (code) command is not available. Please install Visual Studio Code first."
    exit 1
fi

# Run the installation function
install_extensions

echo "All extensions have been installed successfully!"
