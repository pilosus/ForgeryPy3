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
#
# -------------------------------------------------------------------------------
# This software is based on the Tomasz Wójcik's ForgeryPy package.
# Original license is the following:
# -------------------------------------------------------------------------------


"""Generate various random ID numbers for Russian banking/taxation system.

Some types of IDs may have different patterns for different types of
legal personality: natural persons, sole contractors, local companies,
international companies.
"""

import random


__all__ = ['account_number', 'bik', 'inn', 'legal_inn', 'legal_ogrn',
           'ogrn', 'person_inn', 'person_ogrn']

TYPES = ['person', 'legal']


def account_number():
    """Return a random bank account number."""
    account = [random.randint(1, 9) for _ in range(20)]
    return "".join(map(str, account))


def bik():
    """Return a random bank identification number."""
    return '04' + \
           ''.join([str(random.randint(1, 9)) for _ in range(5)]) + \
           str(random.randint(0, 49) + 50)


def inn(type="legal"):
    """Return a random taxation ID number for either a person or a company.

    Further information on the topic can be found in [1] (in russian).
    [1]: https://ru.wikipedia.org/wiki/Идентификационный_номер_налогоплательщика
    """
    if (type in TYPES) and type == 'person':
        return person_inn()
    else:
        return legal_inn()


def legal_inn():
    """Return a random taxation ID number for a company."""
    mask = [2, 4, 10, 3, 5, 9, 4, 6, 8]
    inn = [random.randint(1, 9) for _ in range(10)]
    weighted = [v * mask[i] for i, v in enumerate(inn[:-1])]
    inn[9] = sum(weighted) % 11 % 10
    return "".join(map(str, inn))


def legal_ogrn():
    """Return a random government registration ID for a company."""
    ogrn = "".join(map(str, [random.randint(1, 9) for _ in range(12)]))
    ogrn += str((int(ogrn) % 11 % 10))
    return ogrn


def ogrn(type="legal"):
    """Return a random government registration ID for either a person or a company.

    Further information on the topic can be found in [1] (in russian).
    [1]: https://ru.wikipedia.org/wiki/Основной_государственный_регистрационный_номер
    """
    if (type in TYPES) and type == 'person':
        return person_ogrn()
    else:
        return legal_ogrn()


def person_inn():
    """Return a random taxation ID number for a natural person."""
    mask11 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    mask12 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    inn = [random.randint(1, 9) for _ in range(12)]

    # get the 11th digit of the INN
    weighted11 = [v * mask11[i] for i, v in enumerate(inn[:-2])]
    inn[10] = sum(weighted11) % 11 % 10

    # get the 12th digit of the INN
    weighted12 = [v * mask12[i] for i, v in enumerate(inn[:-1])]
    inn[11] = sum(weighted12) % 11 % 10

    return "".join(map(str, inn))


def person_ogrn():
    """Return a random government registration ID for a person."""
    ogrn = "".join(map(str, [random.randint(1, 9) for _ in range(14)]))
    ogrn += str((int(ogrn) % 13 % 10))
    return ogrn
