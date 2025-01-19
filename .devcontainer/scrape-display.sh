#!/bin/bash

while true; do
    xwd -root -silent -display :1 | convert xwd:- /workspace/frame.png
    sleep 1
done
