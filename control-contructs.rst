====================
 Control constructs
====================

.. contents::


if statements
=============

``if`` statements are used to perform code if a condition is true.

.. code-block:: python

   >>> is_rainy = True
   >>> if is_rainy:
   ...     print('bring your bumbershoot')
   bring your bumbershoot

These can be followed up by an ``else``:

.. code-block:: python

   >>> is_rainy = True
   >>> if is_rainy:
   ...     print('bring your bumbershoot')
   ... else:
   ...     print('no rain')
   bring your bumbershoot

.. note:: In python,
          whitespace is used to define levels in the code.
          It is convention to use 4 spaces (not tabs)
          as the first level of indentation.
          The second level would be 4 more spaces (8 total) and so on.

Now if we set ``is_rainy`` to ``False``:

.. code-block:: python

   >>> is_rainy = False
   >>> if is_rainy:
   ...     print('bring your bumbershoot')
   ... else:
   ...     print('no rain')
   no rain

More conditions can be added with ``elif``.

.. code-block:: python

   >>> is_rainy = False
   >>> is_sunny = True
   >>> if is_rainy:
   ...     print('bring your bumbershoot')
   ... elif is_sunny:
   ...     print('bring your hat')
   ... else:
   ...     print('no rain, no sun')
   bring your hat


Boolean operators
-----------------

It is common to use boolean operators with ``if`` statements.

Assume we have ``some_number``.

.. code-block:: python

  >>> some_number = 9
  >>> print(some_number)
  9

Here are some of the main boolean operators we can use
to check whether value of ``some_number`` meets a condition.

.. code-block:: python

  >>> some_number == 9  # == checks if equal, = assigns
  True
  >>> some_number == 22
  False
  >>> some_number != 1  # not equal
  True
  >>> some_number < 3
  False
  >>> some_number >= 8  # greater than or equal
  True


Using them within an ``if`` statement look like this:

.. code-block:: python

  >>> if some_number < 10:
  ...     print('there are less than 10')
  there are less than 10


for loops
=========

``for`` loops allow you to iterate over variables.

.. code-block:: python

  >>> genes = ['DNJC..uh', 'FOXP2', 'MET7B']
  >>> for gene in genes:
  ...     print('my favorite gene: ' + gene)
  my favorite gene: DNJC..uh
  my favorite gene: FOXP2
  my favorite gene: MET7B

``for`` and ``if`` statments can be nested.


.. code-block:: python

  >>> for gene in genes:
  ...     if gene != 'MET7B':
  ...         print(gene +  ', what a dumb gene')
  DNJC..uh, what a dumb gene
  FOXP2, what a dumb gene


Controlling for loops
---------------------

Once a ``for`` loop is running,
you often want to change the behavior based on the current iteration.
For example,
if a certain value encountered, skip the iteration.
This can be done with ``continue``,
which means stop the current iteration of the loop right here
and go to the next iteration.
Using ``continue``,
we can produce the exact same results as the last block.

.. code-block:: python

  >>> for gene in genes:
  ...     if gene == 'MET7B':
  ...         continue
  ...     print(gene +  ', what a dumb gene')
  DNJC..uh, what a dumb gene
  FOXP2, what a dumb gene

Another common behavior is to break out of the loop completely
if some condition is met.
``break`` is the command to do this.


.. code-block:: python

  >>> lottery_numbers = [888, 301, 405, 772, 332]
  >>> winning_number = 405
  >>> for number in lottery_numbers:
  ...     print(number)
  ...     if number == winning_number:
  ...         print('we have a winner')
  ...         break
  888
  301
  405
  we have a winner


while loops
===========

There are also ``while`` loops in python.
These allow the code to continually be executed
*while* a condition is met.
They aren't used much in practice,
but they look like this:

.. code-block:: python

  >>> number = 1
  >>> while number < 4:
  ...     print(number)
  ...     number += 1
  1
  2
  3

.. note:: The ``+=`` is an assignment operator.
          It adds the value to the current value of the variable
          and then assigns the new value back to the variable.
          It is equivalent to ``number = number + 1``.
          Similar operators exist for subtraction (``-=``),
          multiplication (``*=``), and division (``\=``).
