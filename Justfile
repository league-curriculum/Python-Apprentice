set shell := ["zsh", "-cu"]

[group('release')]
release-clear-outputs:
	find lessons -name '*.ipynb' -print0 | xargs -0 uv run --with nbconvert jupyter nbconvert --clear-output --inplace

[group('release')]
release: release-clear-outputs