.. ForgeryPy documentation master file, created by
   sphinx-quickstart on Wed Jul 11 20:31:25 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ForgeryPy documentation
=======================

ForgeryPy3 is a fake data generator fully compatible with Python 2 and 3.

ForgeryPy3 solves the problem of **generating simple, random, yet
meaningful data for testing and development**.

ForgeryPy3 is a fork of Tomek Wójcik's `ForgeryPy`_ project, which is,
in turn, based on the Ruby `forgery`_ gem.

ForgeryPy3 takes up where ForgeryPy left off, reflecting the current
state of the original ``forgery`` package, carefully following its
API.


Using
=====

Basic usage is easy and straightforward. Fire up your Python REPL and
try::

  >>> import forgery_py
  >>> forgery_py.address.street_address()
  '4358 Shopko Junction'
  >>> forgery_py.basic.hex_color()
  '3F0A59'
  >>> forgery_py.credit_card.type()
  'Visa
  >>> forgery_py.currency.description()
  'Slovenia Tolars'
  >>> forgery_py.date.date()
  datetime.date(2012, 7, 27)
  >>> forgery_py.email.address()
  'debra@tavu.edu
  >>> forgery_py.internet.ip_v4()
  '150.64.188.100''
  >>> forgery_py.lorem_ipsum.title()
  'Pretium nam rhoncus ultrices!'
  >>> forgery_py.monetary.money()
  '$4.50'
  >>> forgery_py.name.full_name()
  'Mary Peters'
  >>> forgery_py.personal.language()
  'Hungarian'
  >>> forgery_py.russian_tax.person_inn()
  '768974545606'
  >>> forgery_py.time.zone()
  'Melbourne'




Modules
=======

.. toctree::

   address
   basic
   credit_card
   currency
   date
   email
   geo
   internet
   lorem_ipsum
   name
   personal
   russian_tax
   time


Source code
===========

Source code is available on `GitHub`_.


Credits
=======

The project is based on `ForgeryPy`_ package by Tomek Wójcik.

ForgeryPy, in its turn, gets use of dictionaries from the original
Ruby `forgery`_ gem.


License
=======

The project is licensed under MIT License. For further information see
``LINCENSE``.

.. _ForgeryPy: https://github.com/tomekwojcik/ForgeryPy
.. _forgery: https://github.com/sevenwire/forgery
.. _documentation: https://pilosus.github.io/ForgeryPy3/
.. _GitHub: https://github.com/pilosus/ForgeryPy3


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

