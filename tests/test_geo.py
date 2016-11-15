# -*- coding: utf-8 -*-

from unittest import TestCase
from forgery_py.forgery import geo


class GeoForgeryTestCase(TestCase):
    def test_latitude(self):
        latitude = geo.latitude()
        self.assertTrue(-90.0 <= latitude <= 90.0)

    def test_latitude_degrees(self):
        latitude = geo.latitude_degrees()
        self.assertTrue(-180 <= latitude <= 180)

    def test_latitude_direction(self):
        direction = geo.latitude_direction()
        self.assertIn(direction, ['N', 'S'])

    def test_latitude_minutes(self):
        minutes = geo.latitude_minutes()
        self.assertIn(minutes, range(60))

    def test_latitude_seconds(self):
        seconds = geo.latitude_seconds()
        self.assertIn(seconds, range(60))

    def test_longitude(self):
        longitude = geo.longitude()
        self.assertTrue(-180.0 <= longitude <= 180.0)

    def test_longitude_degrees(self):
        longitude = geo.longitude_degrees()
        self.assertTrue(-180 <= longitude <= 180)

    def test_longitude_direction(self):
        direction = geo.longitude_direction()
        self.assertIn(direction, ['E', 'W'])

    def test_longitude_minutes(self):
        minutes = geo.longitude_minutes()
        self.assertIn(minutes, range(60))

    def test_longitude_seconds(self):
        seconds = geo.longitude_seconds()
        self.assertIn(seconds, range(60))
