RSTS := $(wildcard *.rst)
PDFS := $(patsubst %.rst, %.pdf, $(RSTS))
CMD = rst2pdf
OPTS = -s tutorial.style
TEST = python3 -m doctest

all: pdf

pdf: $(PDFS)

%.pdf: %.rst
	$(TEST) $<
	$(CMD) $(OPTS) $<

help:
	@echo "Convert rst files to pdf files"
	@echo
	@echo "pdf          make pdf files from rst files"
	@echo "checkall     run tests on all rst files"
	@echo "clean        remove pdfs"


checkall:
	$(TEST) *.rst

clean:
	-rm -f $(PDFS)

.PHONY: clean help checkall
