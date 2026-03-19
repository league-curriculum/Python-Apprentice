#!/bin/bash

# Find all .ipynb files from the current directory downwards
find . -name "*.ipynb" | while read -r notebook_path; do
    # Clear the outputs using nbconvert
    echo "Clearing outputs for ${notebook_path}"
    jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace "${notebook_path}"
done


