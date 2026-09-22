#!/usr/bin/env bash
# Build-time installer for the league-desktop feature. Runs as root.
#
# Installs a minimal X desktop (Xtigervnc + fluxbox) and the Debian noVNC
# client, served by websockify. The process layout mirrors the League
# code-server image (docker-codeserver-python/app/conf.d/novnc.conf), which
# has been reliable in production.
set -euo pipefail

RESOLUTION="${RESOLUTION:-1024x768}"
DEPTH="${DEPTH:-24}"
WEBPORT="${WEBPORT:-6080}"
HEARTBEAT="${HEARTBEAT:-25}"

FEATURE_DIR="$(cd "$(dirname "$0")" && pwd)"
SHARE_DIR=/usr/local/share/league-desktop
NOVNC_DIR=/usr/share/novnc

# The user the desktop runs as. The devcontainer CLI sets _REMOTE_USER;
# fall back to the usual devcontainer user, then root.
DESKTOP_USER="${_REMOTE_USER:-}"
if [ -z "$DESKTOP_USER" ] || [ "$DESKTOP_USER" = "root" ]; then
    if id vscode >/dev/null 2>&1; then DESKTOP_USER=vscode; else DESKTOP_USER=root; fi
fi
DESKTOP_HOME="$(getent passwd "$DESKTOP_USER" | cut -d: -f6)"

echo "league-desktop: user=$DESKTOP_USER resolution=$RESOLUTION depth=$DEPTH port=$WEBPORT"

export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y --no-install-recommends \
    tigervnc-standalone-server \
    tigervnc-tools \
    fluxbox \
    x11-xserver-utils \
    xfonts-base \
    novnc \
    python3-websockify \
    supervisor
rm -rf /var/lib/apt/lists/*

# Debian enables a system supervisord service; we run our own instance from
# the entrypoint instead, so there is exactly one config to reason about.
rm -f /etc/supervisor/conf.d/*.conf

mkdir -p "$SHARE_DIR"
install -m 0755 "$FEATURE_DIR/entrypoint.sh" "$SHARE_DIR/entrypoint.sh"
install -m 0755 "$FEATURE_DIR/league-desktop" /usr/local/bin/league-desktop

# Bake option values into the supervisor config.
sed -e "s|@USER@|$DESKTOP_USER|g" \
    -e "s|@HOME@|$DESKTOP_HOME|g" \
    -e "s|@DEPTH@|$DEPTH|g" \
    -e "s|@WEBPORT@|$WEBPORT|g" \
    -e "s|@HEARTBEAT@|$HEARTBEAT|g" \
    "$FEATURE_DIR/supervisord.conf" > "$SHARE_DIR/supervisord.conf"

# Default resolution; DESKTOP_RESOLUTION in the environment overrides it.
echo "DEFAULT_RESOLUTION=$RESOLUTION" > "$SHARE_DIR/defaults"

# Our client page reconnects after any drop (the stock vnc.html doesn't).
# index.html sends the bare port URL, which is what Codespaces and the
# League extension open, to it.
install -m 0644 "$FEATURE_DIR/league.html" "$NOVNC_DIR/league.html"
install -m 0644 "$FEATURE_DIR/index.html" "$NOVNC_DIR/index.html"

echo "league-desktop: installed"
