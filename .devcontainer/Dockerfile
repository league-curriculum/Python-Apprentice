FROM ghcr.io/league-infrastructure/jtlpython:20240719
ENV VNC_RESOLUTION=600x600x16
ENV PASSWORD=code4life

RUN curl -fsSL https://code-server.dev/install.sh | sh
CMD ["code-server", "--bind-addr", "0.0.0.0:8080", "/workspace"]
