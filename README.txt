
ForgeryPy documentation
***********************

ForgeryPy3 is a fake data generator fully compatible with Python 2 and
3.

ForgeryPy3 solves the problem of **generating simple, random, yet
meaningful data for testing and development**.

ForgeryPy3 is a fork of Tomek Wójcik's ForgeryPy project, which is, in
turn, based on the Ruby forgery gem.

ForgeryPy3 takes up where ForgeryPy left off, reflecting the current
state of the original "forgery" package, carefully following its API.


Using
*****

Basic usage is easy and straightforward. Fire up your Python REPL and
try:

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
*******

* "address" Module
* "basic" Module
* "credit_card" Module
* "currency" Module
* "date" Module
* "email" Module
* "geo" Module
* "internet" Module
* "lorem_ipsum" Module
* "name" Module
* "personal" Module
* "russian_tax" Module
* "time" Module


Source code
***********

Source code is available on GitHub:
https://github.com/pilosus/ForgeryPy3


Credits
*******

The project is based on ForgeryPy package by Tomek Wójcik.

ForgeryPy, in its turn, gets use of dictionaries from the original
Ruby forgery gem.


License
*******

The project is licensed under MIT License. For further information see
"LINCENSE".

