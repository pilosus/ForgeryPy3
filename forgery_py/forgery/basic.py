# -*- coding: utf-8 -*-
# MIT License
#
# Copyright (c) 2016 Vitaly R. Samigullin
# Copyright (C) 2012 by Tomasz Wójcik <labs@tomekwojcik.pl>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


"""Generate misc random data."""

import random
import string
import hashlib
import binascii
from datetime import datetime

from ..dictionaries_loader import get_dictionary

HEX_DIGITS = string.hexdigits[:-6].upper()
BOOLEAN = [True, False]

__all__ = ['hex_color', 'hex_color_short', 'text', 'boolean', 'encrypt',
           'frequency', 'number', 'password', 'color']


def hex_color():
    """Return random HEX color."""
    return ''.join(random.sample(HEX_DIGITS, 6))


def hex_color_short():
    """Return random short HEX color (e.g. `FFF` color)."""
    return ''.join(random.sample(HEX_DIGITS, 3))


def text(length=None, at_least=10, at_most=15, lowercase=True,
         uppercase=True, digits=True, spaces=True, punctuation=False):
    """
    Return random text.

    If `length` is present the text will be exactly this chars long. Else the
    text will be something between `at_least` and `at_most` chars long.
    """
    base_string = ''
    if lowercase:
        base_string += string.ascii_lowercase

    if uppercase:
        base_string += string.ascii_uppercase

    if digits:
        base_string += string.digits

    if spaces:
        base_string += ' '

    if punctuation:
        base_string += string.punctuation

    if len(base_string) == 0:
        return ''

    if not length:
        length = random.randint(at_least, at_most)

    result = ''
    try:
        for _ in xrange(0, length):
            result += random.choice(base_string)
    # Python 3 compatibility
    except NameError:
        for i in range(0, length):
            result += random.choice(base_string)

    return result


def boolean():
    """Return random boolean."""
    return random.choice(BOOLEAN)


def color():
    """Return random color name."""
    return random.choice(get_dictionary('colors')).strip()


def encrypt(password='password', salt=None):
    """
    Return SHA1 hexdigest of a password (optionally salted with a string).


    """
    if not salt:
        salt = str(datetime.utcnow())

    try:
        #  available for python 2.7.8 and python 3.4+
        dk = hashlib.pbkdf2_hmac('sha1', password.encode(), salt.encode(), 100000)
        hexdigest = binascii.hexlify(dk).decode('utf-8')
    except AttributeError:
        # see https://pymotw.com/2/hashlib/
        # see https://docs.python.org/release/2.5/lib/module-hashlib.html
        dk = hashlib.sha1()
        dk.update(password.encode() + salt.encode())
        hexdigest = dk.hexdigest()
    return hexdigest


def frequency():
    """Return random frequency rate.

    Frequency rate is taken from the `frequencies` dictionary."""
    return random.choice(get_dictionary('frequencies')).strip()


def number(at_least=0, at_most=10):
    """Return a random number in the range specified."""
    return random.choice(range(at_least, at_most))


def password(at_least=6, at_most=12, lowercase=True,
             uppercase=True, digits=True, spaces=False, punctuation=False):
    """Return a random string for use as a password."""
    return text(at_least=at_least, at_most=at_most, lowercase=lowercase,
                uppercase=uppercase, digits=digits, spaces=spaces,
                punctuation=punctuation)
