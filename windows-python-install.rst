===============================
 Python installation on Windows
===============================


Download main python exe and run install
========================================

Download python 3:
http://www.python.org/download


Add python to Path
====================

Go here::

  Control Panel > System and Security > System > Change settings >
  Advanced > Environmental Variables

Select ``Path`` variables and append::

  ;C:\Python33;C:\Python33\Scripts;

You know this is working if you open up command prompt and type "python".


Install distribute and pip
==========================

Download and install `distribute
<http://www.lfd.uci.edu/~gohlke/pythonlibs/#distribute>`_ and then `pip
<http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip>`_.

These will allow you to install other python packages from the command prompt.


Install IPython
=================

This is an enhanced interactive shell. To install it, open up command
prompt or terminal and run::

  pip install ipython

One you have this, type ``ipython`` in your terminal
to enter into the ipython shell.
