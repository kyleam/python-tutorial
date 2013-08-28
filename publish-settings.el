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
    :html-postamble t
    :recursive t)
  ("python-tutorial-css"
   :base-directory ,(concat python-tutorial-dir "css")
   :base-extension "css"
   :publishing-directory ,(concat python-tutorial-dir "output/css")
   :publishing-function org-publish-attachment)
  ("python-tutorial-code"
   :base-directory ,(concat python-tutorial-dir "code")
   :base-extension "i*py\\(nb\\)*"
   :exclude ".ipynb_checkpoints"
   :publishing-directory ,(concat python-tutorial-dir "output/code")
   :publishing-function org-publish-attachment
   :recursive t)
  ("python-tutorial-img"
   :base-directory ,(concat python-tutorial-dir "img")
   :base-extension "svg"
   :publishing-directory ,(concat python-tutorial-dir "output/img")
   :publishing-function org-publish-attachment)
  ("python-tutorial-data"
   :base-directory ,(concat python-tutorial-dir "data")
   :base-extension any
   :publishing-directory ,(concat python-tutorial-dir "output/data")
   :publishing-function org-publish-attachment
   :recursive t)
  ("python-tutorial" :components ("python-tutorial-orgfiles"
                                  "python-tutorial-css"
                                  "python-tutorial-code"
                                  "python-tutorial-data"
                                  "python-tutorial-img"))))

(setq org-html-htmlize-output-type "css")

(setq org-html-postamble-format
      '(("en" "<p class=\"license\">
Released under a
<a rel=\"license\"
href=\"http://creativecommons.org/licenses/by-sa/3.0/deed.en_US\">
Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.
</p>
<p class=\"creator\">Created with %c</p>
<p class=\"xhtml-validation\">%v</p>")))
