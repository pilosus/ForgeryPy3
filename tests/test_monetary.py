# -*- coding: utf-8 -*-

from unittest import TestCase
from forgery_py.forgery import monetary


class MonetaryForgeryTestCase(TestCase):
    def test_money(self):
        dollars = monetary.money()
        self.assertTrue(dollars.startswith('$'))

    def test_formatted_money(self):
        money = monetary.formatted_money(min=100, max=200)
        self.assertTrue(100 <= float(money) < 200)
        self.assertEqual(len(money.split('.')[1]), 2)
