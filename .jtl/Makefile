

this_dir := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
base_dir := $(abspath $(this_dir)/..)

.PHONY: config

VERSION := "1.20250310.1"

ver:
	@echo $(VERSION)

push:
	git commit --allow-empty -a -m "Release version $(VERSION)"
	git push
	git tag v$(VERSION) 
	git push --tags


config:
	@echo "base_dir: $(base_dir) "

