RSTS := $(wildcard *.rst)
PDFS := $(patsubst %.rst, %.pdf, $(RSTS))
CMD = rst2pdf
OPTS = -s tutorial.style
pdf: $(PDFS)

%.pdf: %.rst
	$(CMD) $(OPTS) $<

help:
	@echo "All rst files are converted to pdf files"
	@echo
	@echo "pdf          make pdf files from tex files"
	@echo "clean        remove pdfs"


clean:
	-rm -f $(PDFS)

.PHONY: clean help
