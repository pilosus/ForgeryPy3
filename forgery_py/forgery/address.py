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


"""Generate forged address-related data."""

import random
import string

from ..dictionaries_loader import get_dictionary

__all__ = [
    'street_name', 'street_number', 'street_suffix', 'street_address',
    'city', 'state', 'state_abbrev', 'province', 'province_abbrev',
    'zip_code', 'phone', 'country', 'continent'
]


def street_name():
    """Return a random street name."""
    return random.choice(get_dictionary('street_names')).strip()


def street_number():
    """Return a random street number."""
    length = int(random.choice(string.digits[1:6]))
    return ''.join(random.sample(string.digits, length))


def street_suffix():
    """Return a random street suffix."""
    return random.choice(get_dictionary('street_suffixes')).strip()


def street_address():
    """Return a random street address.

    Equivalent of ``street_number() + ' ' +
    street_name() + ' ' + street_suffix()``.
    """
    return '%s %s %s' % (street_number(), street_name(), street_suffix())


def city():
    """Return a random city name."""
    return random.choice(get_dictionary('cities')).strip()


def state():
    """Return a random US state name."""
    return random.choice(get_dictionary('states')).strip()


def state_abbrev():
    """Return a random US abbreviated state name."""
    return random.choice(get_dictionary('state_abbrevs')).strip()


def province():
    """Return random Canadian province or territory."""
    return random.choice(get_dictionary('provinces')).strip()


def province_abbrev():
    """Return random Canadian province or territory abbreviation."""
    return random.choice(get_dictionary('province_abbrevs')).strip()


def zip_code():
    """Return a random ZIP code, either in `#####` or `#####-####` format."""
    format = '#####'
    if random.random() >= 0.5:
        format = '#####-####'

    result = ''
    for item in format:
        if item == '#':
            result += str(random.randint(0, 9))
        else:
            result += item

    return result


def phone():
    """Return a random phone number in `#-(###)###-####` format."""
    format = '#-(###)###-####'

    result = ''
    for item in format:
        if item == '#':
            result += str(random.randint(0, 9))
        else:
            result += item

    return result


def country():
    """Return a random country name."""
    return random.choice(get_dictionary('countries')).strip()


def continent():
    """Return a random continent name."""
    return random.choice(get_dictionary('continents')).strip()
