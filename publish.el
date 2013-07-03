(add-to-list 'load-path (car (file-expand-wildcards "~/.emacs.d/elpa/org-*")))
(add-to-list 'load-path (car (file-expand-wildcards "~/.emacs.d/elpa/htmlize-*")))

(setq custom-theme-directory "~/.emacs.d/theme")
(load-theme 'barely)

(require 'org)
(require 'htmlize)

(org-publish "python-tutorial" t)
