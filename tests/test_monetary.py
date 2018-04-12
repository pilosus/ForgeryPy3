# -*- coding: utf-8 -*-

from unittest import TestCase
from forgery_py.forgery import monetary


class MonetaryForgeryTestCase(TestCase):
    def test_money(self):
        money = monetary.money()
        self.assertTrue(0 <= float(money) < 1000)
        self.assertEqual(len(money.split('.')[1]), 2)

    def test_formatted_money(self):
        dollars = monetary.formatted_money(min=100, max=200)
        self.assertTrue(dollars.startswith('$'))
