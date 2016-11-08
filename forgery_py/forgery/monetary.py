# -*- coding: utf-8 -*-
# Copyright (C) 2016 by Vitaly R. Samigullin <vrs {at} pilosus {dot} org>
#
# TODO
# License

"""Generate random monetary data."""

import random

__all__ = ['money', 'formatted_money']


def money(min=0, max=10):
    """Return a random sum of money with a dollar sign as a prefix."""
    return "$%1.2f" % float(formatted_money(min=min, max=max))


def formatted_money(min=0, max=10):
    """Return a string with a random sum of money with 2 digits after a decimal point."""
    value = random.choice(range(min * 100, max * 100))
    return "%1.2f" % (float(value) / 100)
