# -*- coding: utf-8 -*-

from unittest import TestCase
from forgery_py.forgery import credit_card


class CreditCardForgeryTestCase(TestCase):
    def test_check_digit(self):
        result = credit_card.check_digit(4539750423451972)
        self.assertEqual(result, 2)

    def test_number(self):
        card1 = credit_card.number()
        self.assertFalse(str(card1).startswith('9999'))

        card2 = credit_card.number()
        self.assertEqual(divmod(card2, 10)[1],
                         credit_card.check_digit(card2))

        card3 = credit_card.number(type='MasterCard')
        self.assertIn(int(str(card3)[:2]),
                      credit_card.CARDS['MasterCard']['prefixes'])

        card4 = credit_card.number(type='American Express', length=15)
        self.assertEqual(len(str(card4)), 15)

        card5 = credit_card.number(type='Visa', length=15)
        self.assertEqual(len(str(card5)), 15)

        card6 = credit_card.number(type='SuperCard', length=20,
                                   prefixes=[666, 777, 888, 999])
        self.assertEqual(len(str(card6)), 20)
        self.assertIn(int(str(card6)[:3]), [666, 777, 888, 999])
        self.assertEqual(divmod(card6, 10)[1],
                         credit_card.check_digit(card6))

    def test_type(self):
        result = credit_card.type()
        self.assertTrue(result in credit_card.CARDS)
