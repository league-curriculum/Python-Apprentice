#!/bin/bash
set -x

TARGET_DIR=$1
THIS_DIR=$(dirname "$(realpath "$0")")

echo "❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖"
echo "TARGET_DIR: $TARGET_DIR"
echo "THIS_DIR: $THIS_DIR"

cd $TARGET_DIR

install_requirements() {
	local python_cmd="$1"
	local resolved_path

	if [ ! -x "$python_cmd" ]; then
		return
	fi

	resolved_path=$(realpath "$python_cmd")
	for installed_path in "${INSTALLED_PYTHONS[@]}"; do
		if [ "$installed_path" = "$resolved_path" ]; then
			return
		fi
	done

	"$python_cmd" -m pip install --user -r requirements.txt
	INSTALLED_PYTHONS+=("$resolved_path")
}

INSTALLED_PYTHONS=()

# VS Code in Codespaces may launch either of these interpreters for Run/Debug.
install_requirements /usr/local/bin/python
install_requirements /usr/bin/python3

# Put a newline in the prompt to make it easier to read.
echo "export PYTHONPATH=$(pwd)/.lib/:$PYTHONPATH" >> ~/.bashrc

