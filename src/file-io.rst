=======================
 File input and output
=======================

.. contents::


Reading in files
================

First, we'll define the filename as a string. The specifies where the
file exists on the system.

.. code-block:: python

  >>> infile = '../data/weights.csv'

.. note:: In the path of the filename,
          ``..`` stands for go one directory up
          from the current directory.
          So in the above case,
          ``weights.csv`` is in the ``data`` directory
          that is one directory up.

          ::

            .
            |_ current directory
            |   |
            |   |_ current python file
            |
            |_ data
                |
                |_ weights.csv


In order to work with files, a file handle needs to be created.
This is done using ``open``.

.. code-block:: python

  >>> infh = open(infile)

Once the file handle is created,
there are several ways to read in the contents.

.. _`first read example`:

read
----

The first way is ``read``.


.. code-block:: python

  >>> file_content = infh.read()
  >>> file_content
  'person,weight\nJohn,201\nSue,120\nPaul,150\n'
  >>> infh.close()  # file should be closed after reading

As can be seen in the results,
the contents are stored as a single string
(with new lines indicated by ``\n``).

We could separate these lines into a list by using ``split``.

.. code-block:: python

  >>> file_content.split('\n')
  ['person,weight', 'John,201', 'Sue,120', 'Paul,150', '']

While this works fine,
this is such a common operation that there is a builtin method for it.


readlines
---------

To get the file contents into a list separated by new lines,
``readlines`` can be used.

.. code-block:: python

  >>> infh = open(infile)
  >>> file_lines = infh.readlines()
  >>> file_lines
  ['person,weight\n', 'John,201\n', 'Sue,120\n', 'Paul,150\n']
  >>> infh.close()


Using a for loop
----------------

A common method for reading in file contents
is to do it one line at a time.
This is particularly useful for large files
that are too big to fit into memory.

.. code-block:: python

  >>> infh = open(infile)
  >>> for line in infh:
  ...     print('current line: ' + line.strip())
  current line: person,weight
  current line: John,201
  current line: Sue,120
  current line: Paul,150
  >>> infh.close()

.. note:: ``strip`` is used above to remove the new line (``\n``)
          at the end of the line


Writing files
=============

Writing files is very similar to reading files,
but there are a few differences.
Again, a file handle is created using ``open``,
but the second argument to open must be ``'w'``.
This tells ``open`` the file is to be written to,
as opposed to reading.
Another difference is that the file
that you a writing to does not need to exist on your file system
(in fact, it usually does not).

.. warning:: If you open a file for writing that already exists,
             its content will be overwritten.

.. code-block:: python

  outfile = 'test-outfile.txt'
  outfh = open(outfile, 'w')

  for number in range(3):
       outfh.write('this is line {}\n'.format(number))
  outfh.close()

The would result in a file (``test-outfile.txt``)
that looks like this::

  this is line 0
  this is line 1
  this is line 2


A better way to close files
===========================

In all the examples above,
the file needs to be explicitly closed after opening it.
The ``with`` statement provides a convenient way
to deal with the opening and closing of files.

This is how the first  `first read example`_ would look
using a ``with`` statement.

.. code-block:: python

  >>> infile = '../data/weights.csv'
  >>> with open(infile) as infh:
  ...     file_content = infh.read()

The ``with`` takes care of closing the file
once the current level (marked by indentation) is left.
If a ``'w'`` is passed to ``open``,
the exact same method can be used for writing files.
