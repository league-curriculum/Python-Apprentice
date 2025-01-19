


docker run \
    --sig-proxy=false \
    -a STDOUT \
    -a STDERR \
    --mount type=bind,source=/Users/eric/proj/league-projects/curriculum/Python-Apprentice,target=/workspaces/Python-Apprentice,consistency=cached \
    -l devcontainer.local_folder=/Users/eric/proj/league-projects/curriculum/Python-Apprentice \
    -l devcontainer.config_file=/Users/eric/proj/league-projects/curriculum/Python-Apprentice/.devcontainer/devcontainer.json \
    -e SDL_VIDEO_WINDOW_POS=0,0 \
    -e SDL_AUDIODRIVER=dummy \
    -p 8080:8080 \
    -p 6080:6080 \
    --init \
    --entrypoint /bin/sh \
    vsc-python-apprentice-c62618d2fa57d89881a493d3711298df25a53492283fc9697df93e45ef9b6a14 \
    -c "echo Container started"