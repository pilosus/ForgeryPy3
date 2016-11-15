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


from forgery_py.forgery import internet, lorem_ipsum

__all__ = ['address', 'body', 'subject']


def address(user=None):
    """An alias for internet.email_address(user)."""
    return internet.email_address(user=user)


def body(quantity=2, separator='\n\n', wrap_start='', wrap_end='',
         html=False, sentences_quantity=3, as_list=False):
    """Return a random email text."""
    return lorem_ipsum.paragraphs(quantity=quantity, separator=separator,
                                  wrap_start=wrap_start, wrap_end=wrap_end,
                                  html=html,
                                  sentences_quantity=sentences_quantity,
                                  as_list=as_list)


def subject(words_quantity=4):
    """An alias for lorem_ipsum.title(words_quantity)"""
    return lorem_ipsum.title(words_quantity=words_quantity)
