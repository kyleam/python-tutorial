=================================
 Python installation on Mac OS X
=================================


Install homebrew
================

homebrew is a package manager for Mac OS X. It is the easiest way to
install python, but it requires that you have Xcode installed. For
earlier versions of OS X, this should come with your install
disk. Otherwise, you can get it from the app store for free.


To install homebrew, copy this into a terminal and hit enter::

  ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"


After that, install python3 by running this in the terminal::

  brew install python3


Install IPython
===============

This is an enhanced interactive shell. To install it, open up command
prompt or terminal and run::

  pip3 install ipython


Now you need to add the newly install ipython to your path. To do this,
open a terminal and enter::

  echo 'export PATH=/usr/local/share/python3:$PATH' >> $HOME/.bash_profile

Once you have this, open a new terminal and type ``ipython3`` to enter
into the ipython shell.
