# -*- coding: utf-8 -*-
# Copyright (C) 2016 by Vitaly R. Samigullin <vrs {at} pilosus {dot} org>
#
# TODO
# License

from forgery_py.forgery import internet, lorem_ipsum


def address(user=None):
    """An alias for internet.email_address(user)."""
    return internet.email_address(user=user)


def body(quantity=2, separator='\n\n', wrap_start='', wrap_end='',
                html=False, sentences_quantity=3, as_list=False):
    """Return random email text."""
    return lorem_ipsum.paragraphs(quantity=quantity, separator=separator,
                                  wrap_start=wrap_start, wrap_end=wrap_end,
                                  html=html, sentences_quantity=sentences_quantity,
                                  as_list=as_list)


def subject(words_quantity=4):
    """An alias for lorem_ipsum.title(words_quantity)"""
    return lorem_ipsum.title(words_quantity=words_quantity)




