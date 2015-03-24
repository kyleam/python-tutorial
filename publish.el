(add-to-list 'load-path "~/src/emacs/org-mode/lisp/")
(add-to-list 'load-path "~/src/emacs/org-mode/contrib/lisp/")

(require 'org)
(require 'htmlize)

(org-publish "python-tutorial" t)
