# League Desktop (devcontainer feature)

A virtual X desktop that students view in the browser, so turtle, tkinter,
pygame and guizero windows work in Codespaces. It replaces
`ghcr.io/devcontainers/features/desktop-lite`.

It is built the same way as the desktop in the League code-server image
(`code-server-mono/docker-codeserver-python/app/conf.d/novnc.conf`):

| Piece | What it does |
|---|---|
| `Xtigervnc :1` | X server with built-in VNC on `localhost:5901`, no password (`-localhost` so only websockify can reach it) |
| `fluxbox` | Window manager |
| `websockify --heartbeat=25` | Serves the noVNC web client on 6080 and pings the websocket every 25s so idle sessions aren't dropped |
| `supervisord` | Restarts any of the above if it dies |
| `league.html` | Our client page. Reconnects after *any* disconnect (stock `vnc.html?reconnect=true` only reconnects after a clean close) |
| `index.html` | Redirects the bare port URL to `league.html` |

Everything comes from Debian packages on a pinned base image
(`python:3.12-bookworm`), so a rebuild doesn't pull in new versions by
surprise.

## Usage

```jsonc
"features": {
    "./league-desktop": {
        "resolution": "1024x768"   // optional
    }
},
"forwardPorts": [6080]
```

Open the forwarded port 6080 in a browser. The League VS Code extension's
"Virtual Display" command already opens
`https://$CODESPACE_NAME-6080.app.github.dev/`.

Options: `resolution` (default `1024x768`), `depth` (`16` or `24`),
`webPort` (default `6080`), `heartbeat` (seconds, default `25`). Set
`DESKTOP_RESOLUTION` in `containerEnv` to change the size without
rebuilding.

## Troubleshooting

Inside the container:

```bash
league-desktop status     # process states
league-desktop restart    # restart the whole desktop
league-desktop logs       # tail of all logs in /tmp/league-desktop/
```

The start-up log is `/tmp/league-desktop-start.log`.

## Moving this to its own repo

This directory is self-contained so it can be moved as-is into a features
repo using the [devcontainers feature template](https://github.com/devcontainers/feature-starter)
layout:

1. Copy this directory to `src/league-desktop/` in the new repo.
2. Publish with the `devcontainers/action` GitHub Action, e.g. to
   `ghcr.io/league-infrastructure/features/league-desktop`.
3. Update `documentationURL` in `devcontainer-feature.json`.
4. In each curriculum repo, replace `"./league-desktop": {}` with
   `"ghcr.io/league-infrastructure/features/league-desktop:1": {}` and
   delete the local copy.

`league.html` works with the code-server image's noVNC too (same Debian
package), so that image can switch to it and pick up the reconnect fix.
