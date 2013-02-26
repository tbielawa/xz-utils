#!/usr/bin/make

all:
	@find . -name "*~" -delete
	@mkdir -p ~/rpmbuild/SOURCES
	@tar -cjf ~/rpmbuild/SOURCES/xz-utils.tar ./xz-utils-1
	rpmbuild -ba ./xz-utils.spec
