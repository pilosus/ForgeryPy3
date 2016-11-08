# -*- coding: utf-8 -*-
# Copyright (C) 2016 by Vitaly R. Samigullin <vrs {at} pilosus {dot} org>
#
# TODO
# License

"""Generate random geo data."""

import random


def latitude():
    """Return a random latitude in the range of [-90.0, +90.0] as a float."""
    return random.uniform(0.0, 1.0) * 180.0 - 90.0


def latitude_degrees():
    """Return a random latitude's degrees component in the range [-180, +180] as an int."""
    return random.randint(0, 360) - 180


def latitude_direction():
    """Return a random a latitude's direction component, either "N" (north) or "S" (south)."""
    return random.choice(['N', 'S'])


def latitude_minutes():
    """Return a random latitude's minutes component in the range [0, 60) as an int."""
    return random.randint(0, 60 - 1)


def latitude_seconds():
    """Return a random latitude's seconds component in the range [0, 60) as an int."""
    return random.randint(0, 60 - 1)


def longitude():
    """Return a random longitude in the range [-180.0, +180.0] as a float."""
    return random.uniform(0.0, 1.0) * 360.0 - 180.0


def longitude_degrees():
    """Return a random longitude's degrees component in the range [-180, +180] as an int."""
    return latitude_degrees()


def longitude_direction():
    """Return a random longitude's direction component, either "E" (east) or "W" (west)."""
    return random.choice(['E', 'W'])


def longitude_minutes():
    """Return a random longitude's minutes component in the range [0, 60) as an int."""
    return latitude_minutes()


def longitude_seconds():
    """Return a random longitude's seconds component in the range [0, 60) as an int."""
    return latitude_seconds()