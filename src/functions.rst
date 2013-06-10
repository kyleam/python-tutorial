===========
 Functions
===========

.. contents::

Functions are reusable pieces of code that do something
(that's not a strict enough definition, but it works).
In their purest form,
functions take some input,
do some calculation,
and then return an output.

Let's write a function that,
given a gene's start position,
returns a set of "promoter" coordinates.
We'll coarsely define this
as 1,000 bases upstream and 500 based downstream
of the start position.

So, if we have a set of coordinates for a gene of interest
(chr7:73,095,248-73,097,781),
we can get the start of the promoter
by subtracting 1,000 from 73,095,248
and the end the promoter by adding 500 to the same value.
But we also need to consider the strand.
Because this gene is on the negative strand,
we should add 1,000 to 73,097,781
to get the start position of the promoter
and subtract 500 from the same value to get the stop position.

In code, this would look like this:

.. code-block:: python

  >>> ## details for the specific gene
  >>> genestart = 73097781
  >>> ## promoter calculation (for case of negative strand)
  >>> promstart = genestart - 1000
  >>> promend = genestart + 500

If we have one set of gene coordinates,
we might be tempted to do this,
but it doesn't lead to good code.
It is mixing the details of a specific case
(the gene coordinates)
with general calculation logic
(finding the promoter).
Functions allow us to
separate out this calculation logic,
give a name to it,
and then apply it throughout the code by the name.

Defining functions
==================

Let's create a function named ``get_promoter``.
This is done using ``def``.

.. code-block:: python

  >>> def get_promoter():
  ...     pass

At this point, the function doesn't do anything.
It doesn't take any arguments and it doesn't return any values.

A good place to start when defining a function is the docstring,
which serves as documentation for what the function does.

.. code-block:: python

  >>> def get_promoter():
  ...     """Return promoter for given coordinates and strand"""
  ...     pass  ## placeholder until we fill in the code

Next, we should declare what arguments the function receives.

.. code-block:: python

  >>> def get_promoter(start, strand):
  ...     """Return promoter of gene
  ...
  ...     Parameters
  ...     ----------
  ...     start : int
  ...         start coordinate of gene
  ...     strand : str
  ...         strand direction indicated by + or -
  ...     """
  ...     pass

The arguments are specified between the parentheses
(everything added between the triple quotes is documentation
that, while often helpful, is not required).

Calling functions
=================

We can use the `genestart` defined above and the strand
as input to our new function.

.. code-block:: python

  >>> get_promoter(genestart, '-')

We have called the function,
but it doesn't do anything yet.
Let's add in the calculation.

.. code-block:: python

  >>> def get_promoter(start, strand):
  ...     """Return promoter of gene
  ...
  ...     Parameters
  ...     ----------
  ...     start : int
  ...         start coordinate of gene
  ...     strand : str
  ...         strand direction indicated by + or -
  ...     """
  ...     if strand == '+':
  ...         promstart = start - 1000
  ...         promend = start + 500
  ...     elif strand == '-':
  ...         promstart = start + 1000
  ...         promend = start - 500
  ...     else:
  ...         print('strand not recognized')
  ...     print(promstart, promend)


Now our function should do something.

.. code-block:: python

  >>> get_promoter(genestart, '-')
  73098781 73097281

Looks like it is performing the calculation,
but at this point it is only printing out the values.
We know this because
if we try to assign its return value to a variable (``promoter``),
it is ``None``.

.. code-block:: python

  >>> promoter = get_promoter(genestart, '-')
  73098781 73097281
  >>> print(promoter)
  None

To get back the result,
we can modify the function to include a return statement.

.. code-block:: python

  >>> def get_promoter(start, strand):
  ...     """Return promoter of gene
  ...
  ...     Parameters
  ...     ----------
  ...     start : int
  ...         start coordinate of gene
  ...     strand : str
  ...         strand direction indicated by + or -
  ...     """
  ...     if strand == '+':
  ...         promstart = start - 1000
  ...         promend = start + 500
  ...     elif strand == '-':
  ...         promstart = start + 1000
  ...         promend = start - 500
  ...     else:
  ...         print('strand not recognized')
  ...     return promstart, promend

When we call the new function,
the result is returned
(because we've added the return statement at the end)
and no longer printed out
(because we removed the print statement).

.. code-block:: python

  >>> promoter = get_promoter(genestart, '-')

The variable ``promoter`` now contains the returned results.

.. code-block:: python

  >>> print(promoter)
  (73098781, 73097281)

.. note:: Due to how the return statement was specified,
          a tuple has been returned.
          Any type can be returned.
          If square brackets were given around the results
          (``return [promstart, promend]``),
          a list would have been returned instead.
          For now, tuples can be thought of as very similar to lists,
          though there are some very important differences
          (particularly in terms of mutability,
          which we have not discussed).


Keyword arguments
=================

In the above example,
we have two required arguments:
``start`` and ``strand`` must be given.
If we call the function without an argument,
we get an error.

.. code-block:: python

  >>> get_promoter(genestart)
  Traceback (most recent call last):
  ...
  TypeError: get_promoter() missing 1 required positional argument: 'strand'

Required arguments are a good thing,
but in some cases,
it is useful to allow optional arguments.
For example,
the 1,000 bases upstream/500 bases downstream
used to define the promoter are parameters
that should probably be tunable,
so we can provide then as default values that can be overridden
when the function is called.

.. code-block:: python

  >>> def get_promoter(start, strand, upstream=1000, downstream=500):
  ...     """Return promoter of gene
  ...
  ...     Parameters
  ...     ----------
  ...     start : int
  ...         start coordinate of gene
  ...     strand : str
  ...         strand direction indicated by + or -
  ...     upstream, downstream : int
  ...         number of bases upstream/downstream of start used to
  ...         define promoter
  ...     """
  ...     if strand == '+':
  ...         promstart = start - upstream
  ...         promend = start + downstream
  ...     elif strand == '-':
  ...         promstart = start + upstream
  ...         promend = start - downstream
  ...     else:
  ...         print('strand not recognized')
  ...     return promstart, promend

Now we can call the function as before and get the same results.

.. code-block:: python

  >>> get_promoter(genestart, '-')
  (73098781, 73097281)

If we choose to,
we can override the default values.
For example, we could bring the upstream bases down to 500:

.. code-block:: python

  >>> get_promoter(genestart, '-', upstream=500)
  (73098281, 73097281)

Both optional arguments can be tweaked at the same time:

.. code-block:: python

  >>> get_promoter(genestart, '-', upstream=500, downstream=400)
  (73098281, 73097381)

In the above examples,
we provide the keywords with the value,
but they can also be given without the keywords
as long as the order is preserved.

.. code-block:: python

  >>> get_promoter(genestart, '-', 500, 400)
  (73098281, 73097381)

In this case, however,
leaving out the keywords makes the function less readable.


Done
====

We now have a function that is reusable throughout the code.
In addition to simplifying our code,
this makes it easier to modify the code later if needed
because the code only has to be changed in one place.
This function can also be shared with other python files.
We'll talk about this more when we go over modules.
