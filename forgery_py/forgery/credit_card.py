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

"""Generate credit card random data."""

import random

import forgery_py.forgery.basic as basic

__all__ = [
    'type', 'check_digit', 'number'
]

CARDS = {'Visa': {'length': 16, 'prefixes': [4539, 4556, 4916, 4532, 4929,
                                             40240071, 4485, 4716, 4]},
         'MasterCard': {'length': 16, 'prefixes': [51, 52, 53, 54, 55]},
         'American Express': {'length': 15, 'prefixes': [34, 37]},
         'Discover': {'length': 16, 'prefixes': [6011]}
         }


def type():
    """Return a random credit card type."""
    return random.choice(list(CARDS.keys()))


def check_digit(num):
    """Return a check digit of the given credit card number.

    Check digit calculated using Luhn algorithm ("modulus 10")
    See: http://www.darkcoding.net/credit-card/luhn-formula/
    """
    sum = 0

    # drop last digit, then reverse the number
    digits = str(num)[:-1][::-1]

    for i, n in enumerate(digits):
        # select all digits at odd positions starting from 1
        if (i + 1) % 2 != 0:
            digit = int(n) * 2
            if digit > 9:
                sum += (digit - 9)
            else:
                sum += digit
        else:
            sum += int(n)

    return ((divmod(sum, 10)[0] + 1) * 10 - sum) % 10


def number(type=None, length=None, prefixes=None):
    """
    Return a random credit card number.

    :param type: credit card type. Defaults to a random selection.
    :param length: length of the credit card number.
                   Defaults to the length for the selected card type.
    :param prefixes: allowed prefixes for the card number.
                     Defaults to prefixes for the selected card type.
    :return: credit card randomly generated number (int)
    """
    # select credit card type
    if type and type in CARDS:
        card = type
    else:
        card = random.choice(list(CARDS.keys()))

    # select a credit card number's prefix
    if not prefixes:
        prefixes = CARDS[card]['prefixes']
    prefix = random.choice(prefixes)

    # select length of the credit card number, if it's not set
    if not length:
        length = CARDS[card]['length']

    # generate all digits but the last one
    result = str(prefix)

    for d in range(length - len(str(prefix))):
        result += str(basic.number())

    last_digit = check_digit(int(result))

    return int(result[:-1] + str(last_digit))
