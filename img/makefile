texs := $(wildcard *.tex)
pdf_files := $(patsubst %.tex, %.pdf, $(texs))
svg_files := $(patsubst %.tex, %.svg, $(texs))
pdfcmd = latexmk -pdf -pdflatex="pdflatex -interactive=nonstopmode" -use-make
svgcmd = pdf2svg
toclean = *.aux *.log *.fdb_latexmk *.fls *.pdf

help:
	@echo "pdf          make pdf files from tex files"
	@echo "svg          make svg files from tex files"
	@echo "clean        remove $(toclean)"
	@echo "cleanse      remove $(toclean) and svg files"

svg: $(svg_files)

%.svg: %.pdf
	$(svgcmd) $< $@

pdf: $(pdf_files)


%.pdf: %.tex
	$(pdfcmd) $<

clean:
	-rm -f $(toclean)

cleanse: clean
	-rm -f *.svg

.PHONY: clean cleanse help
