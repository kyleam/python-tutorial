base_dir=$(CURDIR)

less_dir=$(base_dir)/css/less
less_files:=$(wildcard $(less_dir)/bootstrap/*.less)
less_files+=$(wildcard $(less_dir)/*.less)

src_dir=$(base_dir)/src
src_files:=$(wildcard $(src_dir)/*.org)
src_files+=$(wildcard $(base_dir)/doc/*.org)

output_dir=output
html_index:=$(output_dir)/index.html

css_dir=$(base_dir)/css
css_file=$(css_dir)/theme.css

img_dir=$(base_dir)/img
img_sentinel=$(img_dir)/.sentinel
img_tex:=$(wildcard $(img_dir)/*.tex)

github_remote=kyleam

site: css html img

github: site
	./import-to-ghpages.sh && git push -f $(github_remote) gh-pages

html: $(html_index)

$(html_index): $(css_file) $(src_files) $(img_sentinel)
	./publish.sh

css: |$(css_dir) $(css_file)

$(output_dir):
	mkdir -p $(output_dir)

$(css_dir):
	mkdir -p $(css_dir)

$(css_file): $(less_files)
	lessc -x $(less_dir)/theme.less $(css_file)

img: $(img_sentinel)

$(img_sentinel): $(img_tex)
	cd $(img_dir) && make svg
	touch $(img_dir)/.sentinel

.PHONY: clean
clean:
	-rm -rf $(output_dir)

.PHONY: help
help:
	@echo "site         build site files in output directory"
	@echo "github       build site and push to github pages"
	@echo "html         update site html without updating css"
	@echo "css          update site css without updating html"
	@echo "img	    build images in img directory"
	@echo "clean        remove output directory"
