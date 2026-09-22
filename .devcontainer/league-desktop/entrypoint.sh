#!/bin/sh
# Container entrypoint for league-desktop. Starts the desktop in the
# background, then hands off to whatever command the container was given.
# A desktop failure must never keep the container from starting.
/usr/local/bin/league-desktop start >/tmp/league-desktop-start.log 2>&1 \
    || echo "league-desktop: failed to start, see /tmp/league-desktop-start.log" >&2

if [ "$#" -gt 0 ]; then
    exec "$@"
fi
