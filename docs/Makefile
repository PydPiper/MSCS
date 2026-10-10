SPHINXBUILD ?= sphinx-build
SOURCEDIR = .
BUILDDIR = _build

.PHONY: html slides clean

slides:
	$(SPHINXBUILD) -b revealjs $(SOURCEDIR) $(BUILDDIR)/revealjs

html:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)/html

clean:
	$(SPHINXBUILD) -M clean $(SOURCEDIR) $(BUILDDIR)
