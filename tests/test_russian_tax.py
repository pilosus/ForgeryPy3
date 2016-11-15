# -*- coding: utf-8 -*-

from unittest import TestCase
from forgery_py.forgery import russian_tax


class RussianTaxForgeryTestCase(TestCase):
    def test_account_number(self):
        account = russian_tax.account_number()
        self.assertEqual(len(account), 20)
        self.assertFalse('0' in account)

    def test_bik(self):
        bik = russian_tax.bik()
        self.assertEqual(len(bik), 9)
        self.assertTrue(bik.startswith('04'))
        self.assertTrue(50 <= int(bik[-2:]) < 100)

    def test_inn(self):
        person_inn = russian_tax.inn("person")
        self.assertEqual(len(person_inn), 12)

        legal_inn = russian_tax.inn("legal")
        self.assertEqual(len(legal_inn), 10)

        default_inn = russian_tax.inn()
        self.assertEqual(len(default_inn), len(legal_inn))

    def test_legal_inn(self):
        inn = russian_tax.legal_inn()
        self.assertEqual(len(inn), 10)

        mask = [2, 4, 10, 3, 5, 9, 4, 6, 8]
        last_digit = sum([int(v) * mask[i]
                          for i, v in enumerate(inn[:-1])]) % 11 % 10
        self.assertEqual(last_digit, int(inn[-1]))

    def test_legal_ogrn(self):
        legal_ogrn = russian_tax.legal_ogrn()
        self.assertEqual(len(legal_ogrn), 13)
        self.assertFalse('0' in legal_ogrn[:-1])
        self.assertEqual(int(legal_ogrn[:-1]) % 11 % 10, int(legal_ogrn[-1]))

    def test_ogrn(self):
        person_ogrn = russian_tax.ogrn("person")
        self.assertEqual(len(person_ogrn), 15)

        legal_ogrn = russian_tax.ogrn("legal")
        self.assertEqual(len(legal_ogrn), 13)

        default_ogrn = russian_tax.ogrn()
        self.assertEqual(len(default_ogrn), len(legal_ogrn))

    def test_person_inn(self):
        inn = russian_tax.person_inn()
        self.assertEqual(len(inn), 12)

        mask11 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
        mask12 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]

        digit11 = sum([int(v) * mask11[i]
                       for i, v in enumerate(inn[:-2])]) % 11 % 10
        self.assertEqual(digit11, int(inn[-2]))

        digit12 = sum([int(v) * mask12[i]
                       for i, v in enumerate(inn[:-1])]) % 11 % 10
        self.assertEqual(digit12, int(inn[-1]))

    def test_person_ogrn(self):
        person_ogrn = russian_tax.person_ogrn()
        self.assertEqual(len(person_ogrn), 15)
        self.assertFalse('0' in person_ogrn[:-1])
        self.assertEqual(int(person_ogrn[:-1]) % 13 % 10, int(person_ogrn[-1]))
