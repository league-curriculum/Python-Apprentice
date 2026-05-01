#!/bin/bash
set -euxo pipefail

TARGET_DIR=$1
THIS_DIR=$(dirname "$(realpath "$0")")
VENV_DIR="$TARGET_DIR/.venv"
PREFERRED_PYTHON="/usr/local/bin/python"
FALLBACK_PYTHON="/usr/bin/python3"

echo "❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖"
echo "TARGET_DIR: $TARGET_DIR"
echo "THIS_DIR: $THIS_DIR"

if [ -x "$PREFERRED_PYTHON" ]; then
	BASE_PYTHON="$PREFERRED_PYTHON"
elif [ -x "$FALLBACK_PYTHON" ]; then
	BASE_PYTHON="$FALLBACK_PYTHON"
else
	echo "No Python interpreter found for virtual environment setup." >&2
	exit 1
fi

cd "$TARGET_DIR"

"$BASE_PYTHON" -m venv "$VENV_DIR"
"$VENV_DIR/bin/python" -m pip install --upgrade pip
"$VENV_DIR/bin/python" -m pip install -r requirements.txt

append_if_missing() {
	local line="$1"
	local file="$2"

	if ! grep -Fqx "$line" "$file"; then
		echo "$line" >> "$file"
	fi
}

append_if_missing "export PYTHONPATH=$TARGET_DIR/.lib:\${PYTHONPATH:-}" "$HOME/.bashrc"
append_if_missing "if [ -f \"$VENV_DIR/bin/activate\" ]; then . \"$VENV_DIR/bin/activate\"; fi" "$HOME/.bashrc"

