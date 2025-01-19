#FROM ghcr.io/league-infrastructure/jtlpython:20240719

FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm
ENV VNC_RESOLUTION=600x600x16
ENV PASSWORD=code4life

COPY .devcontainer/install.sh /tmp/install-vnc.sh
# installs /usr/local/share/desktop-init.sh
RUN chmod 775 /tmp/install-vnc.sh 
RUN /tmp/install-vnc.sh

RUN apt-get update && apt-get install -y --no-install-recommends \
    x11-apps \
    git \
    imagemagick && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

EXPOSE 6080
EXPOSE 5901
EXPOSE 8080

#RUN mkdir /workspace
#RUN git clone https://github.com/league-curriculum/Python-Apprentice /workspace


RUN curl -fsSL https://code-server.dev/install.sh | sh

USER vscode

CMD ["code-server",  "--disable-workspace-trust",  "--bind-addr", "0.0.0.0:8080", "/workspace"]
