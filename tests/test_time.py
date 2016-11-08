# -*- coding: utf-8 -*-

from unittest import TestCase
from forgery_py.forgery import time
from forgery_py.dictionaries_loader import get_dictionary


class TimeForgeryTestCase(TestCase):
    def test_zone(self):
        zone = time.zone()
        self.assertTrue(zone + '\n' in get_dictionary('zones'))
