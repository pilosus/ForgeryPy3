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

"""Generate random geo data."""

import random

__all__ = [
    'latitude', 'latitude_degrees', 'latitude_direction', 'latitude_minutes',
    'latitude_seconds', 'longitude', 'longitude_degrees', 'longitude_direction',
    'longitude_minutes', 'longitude_seconds'
]


def latitude():
    """Return a random latitude in the range of [-90.0, +90.0].

    Latitude is a float."""
    return random.uniform(0.0, 1.0) * 180.0 - 90.0


def latitude_degrees():
    """Return a random latitude's degrees component in the range [-180, +180].

    Latitude's degree is an int."""
    return random.randint(0, 360) - 180


def latitude_direction():
    """Return a random a latitude's direction component.

    Latitude's direction is denoted as either "N" (north) or "S" (south)."""
    return random.choice(['N', 'S'])


def latitude_minutes():
    """Return a random latitude's minutes component in the range [0, 60).

    Latitude's minutes is an int."""
    return random.randint(0, 60 - 1)


def latitude_seconds():
    """Return a random latitude's seconds component in the range [0, 60).

    Latitude's seconds is an int."""
    return random.randint(0, 60 - 1)


def longitude():
    """Return a random longitude in the range [-180.0, +180.0].

    Longitude is a float."""
    return random.uniform(0.0, 1.0) * 360.0 - 180.0


def longitude_degrees():
    """Return a random longitude's degrees component in the range [-180, +180].

    Longitude's degrees is an int."""
    return latitude_degrees()


def longitude_direction():
    """Return a random longitude's direction component.

    Longitude's direction is denoted as either "E" (east) or "W" (west)."""
    return random.choice(['E', 'W'])


def longitude_minutes():
    """Return a random longitude's minutes component in the range [0, 60).

    longitude's minutes is an int."""
    return latitude_minutes()


def longitude_seconds():
    """Return a random longitude's seconds component in the range [0, 60).

    Longitude's seconds is an int."""
    return latitude_seconds()
