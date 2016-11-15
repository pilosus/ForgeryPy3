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

"""Generate random `Lorem ipsum` style text."""

import random
import re

from ..dictionaries_loader import get_dictionary

__all__ = [
    'word', 'words', 'title', 'sentence',
    'sentences', 'paragraph', 'paragraphs',
    'characters', 'character', 'lorem_ipsum_characters',
    'lorem_ipsum_words', 'text'
]

_words = None


def word():
    """Return a random word."""
    return words(quantity=1)


def words(quantity=10, as_list=False):
    """Return random words."""
    global _words

    if not _words:
        _words = ' '.join(get_dictionary('lorem_ipsum')).lower().\
            replace('\n', '')
        _words = re.sub(r'\.|,|;/', '', _words)
        _words = _words.split(' ')

    result = random.sample(_words, quantity)

    if as_list:
        return result
    else:
        return ' '.join(result)


def title(words_quantity=4):
    """Return a random sentence to be used as e.g. an e-mail subject."""
    result = words(quantity=words_quantity)
    result += random.choice('?.!')
    return result.capitalize()


def sentence():
    """Return a random sentence."""
    return sentences(quantity=1)


def sentences(quantity=2, as_list=False):
    """Return random sentences."""
    result = [sntc.strip() for sntc in
              random.sample(get_dictionary('lorem_ipsum'), quantity)]

    if as_list:
        return result
    else:
        return ' '.join(result)


def paragraph(separator='\n\n', wrap_start='', wrap_end='',
              html=False, sentences_quantity=3):
    """Return a random paragraph."""
    return paragraphs(quantity=1, separator=separator, wrap_start=wrap_start,
                      wrap_end=wrap_end, html=html,
                      sentences_quantity=sentences_quantity)


def paragraphs(quantity=2, separator='\n\n', wrap_start='', wrap_end='',
               html=False, sentences_quantity=3, as_list=False):
    """Return random paragraphs."""
    if html:
        wrap_start = '<p>'
        wrap_end = '</p>'
        separator = '\n\n'

    result = []
    try:
        for _ in xrange(0, quantity):
            result.append(wrap_start +
                          sentences(sentences_quantity) +
                          wrap_end)
    # Python 3 compatibility
    except NameError:
        for _ in range(0, quantity):
            result.append(wrap_start +
                          sentences(sentences_quantity) +
                          wrap_end)

    if as_list:
        return result
    else:
        return separator.join(result)


def _to_lower_alpha_only(s):
    """Return a lowercased string with non alphabetic chars removed.

    White spaces are not to be removed."""
    s = re.sub(r'\n', ' ',  s.lower())
    return re.sub(r'[^a-z\s]', '', s)


def characters(quantity=10):
    """Return random characters."""
    line = map(_to_lower_alpha_only,
               ''.join(random.sample(get_dictionary('lorem_ipsum'), quantity)))
    return ''.join(line)[:quantity]


def character():
    """Return a random character."""
    return characters(quantity=1)


def text(what="sentence", *args, **kwargs):
    """An aggregator for all above defined public methods."""

    if what == "character":
        return character(*args, **kwargs)
    elif what == "characters":
        return characters(*args, **kwargs)
    elif what == "word":
        return word(*args, **kwargs)
    elif what == "words":
        return words(*args, **kwargs)
    elif what == "sentence":
        return sentence(*args, **kwargs)
    elif what == "sentences":
        return sentences(*args, **kwargs)
    elif what == "paragraph":
        return paragraph(*args, **kwargs)
    elif what == "paragraphs":
        return paragraphs(*args, **kwargs)
    elif what == "title":
        return title(*args, **kwargs)
    else:
        raise NameError('No such method')


def lorem_ipsum_characters():
    """Return a whole lorem_ipsum dictionary as a lowercase string."""
    return _to_lower_alpha_only(''.join(get_dictionary('lorem_ipsum')))


def lorem_ipsum_words():
    """Return a list of all lowercased words.

    Words are taken from the `lorem_ipsum dictionary`."""
    return lorem_ipsum_characters().strip().split(' ')
