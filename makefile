srcdir = src
builddir = doc
rstfiles := $(wildcard $(srcdir)/*.rst)
pdffiles := $(patsubst $(srcdir)/%.rst, $(builddir)/%.pdf, $(rstfiles))

cmd = rst2pdf
style = $(srcdir)/tutorial.style
cflags = -s $(style)

test = python3 -m doctest

all: pdf

pdf: $(pdffiles)

$(builddir)/%.pdf: $(srcdir)/%.rst $(style) | $(builddir)
	cd $(srcdir) && $(test) `basename $<`
	$(cmd) $(cflags) -o $@ $<

checkall:
	cd $(srcdir) && $(test) *.rst

clean:
	-rm -f $(pdffiles)

$(builddir):
	mkdir $(builddir)

.PHONY: clean help checkall

help:
	@echo "Convert rst files to pdf files"
	@echo
	@echo "pdf          make pdf files from rst files in $(srcdir)"
	@echo "checkall     run tests on all rst files in $(srcdir)"
	@echo "clean        remove pdfs"
