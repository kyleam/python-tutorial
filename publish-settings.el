(defvar python-tutorial-dir
  (file-name-as-directory "~/projects/python-tutorial")
  "Top directory of python tutorials")

(setq org-publish-project-alist
  `(("python-tutorial-orgfiles"
    :base-directory ,(concat python-tutorial-dir "src")
    :base-extension "org"
    :exclude "setup.org"
    :publishing-directory ,(concat python-tutorial-dir "output")
    :publishing-function (org-html-publish-to-html)
    :headline-levels 3
    :section-numbers nil
    :with-toc t
    :html-head "<link rel=\"stylesheet\" href=\"../css/theme.css\" type=\"text/css\"/>"
    :html-head-include-default-style nil
    :html-head-include-scripts nil
    :html-preamble nil
    :html-postamble nil
    :recursive t)
  ("python-tutorial-css"
   :base-directory ,(concat python-tutorial-dir "css")
   :base-extension "css"
   :publishing-directory ,(concat python-tutorial-dir "output/css")
   :publishing-function org-publish-attachment)
  ("python-tutorial-code"
   :base-directory ,(concat python-tutorial-dir "code")
   :base-extension "py"
   :publishing-directory ,(concat python-tutorial-dir "output/code")
   :publishing-function org-publish-attachment
   :recursive t)
  ("python-tutorial-data"
   :base-directory ,(concat python-tutorial-dir "data")
   :base-extension any
   :publishing-directory ,(concat python-tutorial-dir "output/data")
   :publishing-function org-publish-attachment
   :recursive t)
  ("python-tutorial" :components ("python-tutorial-orgfiles"
                                  "python-tutorial-css"
                                  "python-tutorial-code"
                                  "python-tutorial-data"))))

(setq org-html-htmlize-output-type "css")
