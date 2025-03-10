

this_dir := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
base_dir := $(abspath $(this_dir)/..)

.PHONY: config

VERSION := "1.20250309.3"

ver:
	@echo $(VERSION)

push:
	git commit --allow-empty -a -m "Release version $(VERSION)"
	git push
	git tag v$(VERSION) 
	git push --tags



config:
	@echo "base_dir: $(base_dir) "

# Install the student version of settings.json, which wil hide a lot of dot files. 
student-config:
	if [ ! -f $(base_dir)/.jtl/settings-dev.json ]; then mv $(base_dir)/.vscode/settings.json $(base_dir)/.jtl/settings-dev.json; fi
	cp  $(base_dir)/.jtl/settings-student.json $(base_dir)/.vscode/settings.json

# Restore the developers version of the settings.json file.
dev-config:
	if [ -f $(base_dir)/.jtl/settings-dev.json ]; then mv $(base_dir)/.jtl/settings-dev.json $(base_dir)/.vscode/settings.json; fi
