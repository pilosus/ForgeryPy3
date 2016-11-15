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


"""Generate random date-related data."""

import random

from ..dictionaries_loader import get_dictionary
from .name import first_name
from forgery_py.forgery import lorem_ipsum

__all__ = [
    'user_name', 'top_level_domain', 'domain_name',
    'email_address', 'email_subject', 'cctld', 'ip_v4',
    'ip_v6'
]


def user_name(with_num=False):
    """Return a random user name.

    Basically it's lowercased result of
    :py:func:`~forgery_py.forgery.name.first_name()` with a number appended
    if `with_num`.
    """
    result = first_name()
    if with_num:
        result += str(random.randint(63, 94))

    return result.lower()


def top_level_domain():
    """Return a random top-level domain name."""
    return random.choice(get_dictionary('top_level_domains')).strip()


def domain_name():
    """Return a random domain name.

    Lowercased result of :py:func:`~forgery_py.forgery.name.company_name()`
    plus :py:func:`~top_level_domain()`.
    """
    result = random.choice(get_dictionary('company_names')).strip()
    result += '.' + top_level_domain()

    return result.lower()


def email_address(user=None):
    """Return random e-mail address in a hopefully imaginary domain.

    If `user` is ``None`` :py:func:`~user_name()` will be used. Otherwise it
    will be lowercased and will have spaces replaced with ``_``.

    Domain name is created using :py:func:`~domain_name()`.
    """
    if not user:
        user = user_name()
    else:
        user = user.strip().replace(' ', '_').lower()

    return user + '@' + domain_name()


def email_subject(words_quantity=4):
    """An alias for lorem_ipsum.title(words_quantity)"""
    return lorem_ipsum.title(words_quantity=words_quantity)


def cctld():
    """Return a random country code TLD."""
    return random.choice(get_dictionary('country_code_top_level_domains')).\
        strip()


def ip_v4():
    """Return a random IPv4 address."""
    return '.'.join([str(random.randint(0, 255)) for _ in range(0, 4)])


def _py2_ip_v6():
    """Return a random IPv6 address for Python versions prior to 3.3."""
    # 4-digit hexadecimal numbers
    magnitude = 16 ** 4
    # credits: http://stackoverflow.com/a/7660959/4241180
    return ":".join(("%x" % random.randint(0, magnitude) for _ in range(8)))


def ip_v6():
    """Return a random IPv6 address."""
    try:
        # module was introduced in Python 3.3
        import ipaddress
    except ImportError:
        return _py2_ip_v6()
    # credits: http://stackoverflow.com/a/2811349/4241180
    return str(ipaddress.IPv6Address(random.randint(0, 2**128)))
