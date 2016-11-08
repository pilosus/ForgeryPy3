# -*- coding: utf-8 -*-
# Copyright (C) 2016 by Vitaly R. Samigullin <vrs {at} pilosus {dot} org>
#
# TODO
# License

"""Generate credit card random data."""

import random
from ..dictionaries_loader import get_dictionary

__all__ = ['zone']


def zone():
    """Return random color name."""
    return random.choice(get_dictionary('zones')).strip()