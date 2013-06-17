====================
 Command line input
====================


Avoiding hard-coding
====================

Up to this point,
we have been hard-coding many elements in the code.
For example,
in ``get_gene_coords.py``,
we explicitly provide the file name for the genes of interest.
This is problematic
because if we want to extract coordinates from another file,
we have to change the source code itself.


Command line arguments
======================

A better way to do this is to provide this information
as input the the program.
A very common way to do this is as command line arguments.


Providing command line arguments
--------------------------------

To provide input to a program at run time,
additional arguments can be given after the program name.

.. code-block:: bash

  $ python program arg1 arg2 ...

.. note:: The ``$`` above is often used to indicate
          that the command is being given at the command line
          (in the terminal or Windows Command Prompt)

For ``get_gene_coords.py``,
this would look like this:

.. code-block:: bash

  $ python get_gene_coords.py ../data/genes-5random.txt

First, we provide the name of the script to run
and then we provide one argument as input:
the path to the file containing the genes of interest


Accessing command line arguments
--------------------------------

Now that we have given the argument to the program,
we have to write code that makes use of it.
To do this,
we need to import a module, ``sys``.

.. code-block:: python

  import sys

``sys`` contains a list,
named ``argv``,
that has information
about the command line arguments.

Make a script (name it ``argtest.py``)
that imports the ``sys`` module and then prints ``argv``.

.. code-block:: python

  import sys
  print(sys.argv)

Now test it from the command line.

.. code-block:: bash

  $ python argtest.py

This should print a list that contains "argtest.py".
Now try to pass an argument.

.. code-block:: bash

  $ python argtest.py somearg

This should print the script name as above,
but the list should contain a second string, "somearg".
Each additional argument passed will be added to the list.

We can apply this to ``get_gene_coords.py`` example.
Before, we were explicitly declaring the file name:

.. code-block:: python

  gene_file = '../data/genes-5random.txt'

Instead, we can do this:

.. code-block:: python

  import sys
  gene_file = sys.argv[1]
  ## rest of script ...

This allows any file that has the correct format
(in this case, one gene name per line)
to be given as input to the script.

.. code-block:: bash

  $ python get_gene_coords.py newfile



Checking the number of arguments
================================

If something seems wrong with the input arguments,
it is often a good idea to stop the program
and print a helpful usage message.
A simple (and good) thing to check is whether
the right number of arguments has been given.
For example,
``get_gene_coords.py`` needs exactly one argument
to work properly.
What code could you write
to check that the correct number of arguments has been passed?
