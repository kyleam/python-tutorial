=================
 Types in Python
=================

Some of the major types of variables in python include

1. Boolean
2. integers
3. floats
4. strings
5. lists
6. dictionaries

.. note:: The ``>>>`` below indicates that
          this is happening at an interactive shell.
          Although ``>>>`` is for the standard python shell,
          you should use IPython instead
          (type ``ipython`` in a terminal).

Boolean
=======

Boolean values are represented by ``True`` and ``False``.
The often are produced by comparison operations.

.. code-block:: python

   >>> 3 > 2
   True
   >>> 10/5 == 1
   False

Integers
========

Pretty much what you would expect

.. code-block:: python

  >>> x = 1
  >>> x + 3
  4


Floats
======

Again, as expected

.. code-block:: python

  >>> x = 1.0
  >>> x + 3
  4.0

If you add an integer to a float, the result will be a float.


Strings
=======

These are characters and words.
They must be surrounded by either single or double quotes.

.. code-block:: python

   >>> name = 'john'

Strings have some convenient methods associated with them.
For example:

.. code-block:: python

  >>> name.upper()
  'JOHN'
  >>> name.capitalize()
  'John'

.. note:: To discover the methods available for an object
          (like the string ``name`` above),
          type the object and a period and then hit tab.
          So, in this case, ``name.<TAB>``
          will show you all the available methods.

Lists
=====

A list is a sequence of values

.. code-block:: python

  >>> primes = [2, 3, 5]

Each value can be accessed individually

.. code-block:: python

  >>> primes[0]
  2
  >>> primes[2]
  5

The index (the value inside the brackets) is 0-based.

Lists can also be iterated over one-by-one

.. code-block:: python

  >>> for prime in primes:
  ...     print(prime)
  2
  3
  5


Dicts
=====

Provides key-value look up.

.. code-block:: python

  >>> prices = {'car' : 40000, 'pop' : 1}
  >>> prices['pop']
  1
