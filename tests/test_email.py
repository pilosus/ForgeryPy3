# -*- coding: utf-8 -*-

import re
import string
from unittest import TestCase
from forgery_py.forgery import email


class EmailForgeryTestCase(TestCase):
    def test_address(self):
        email1 = email.address()
        self.assertIsNotNone(re.match(r'[a-z]+?@[a-z]+?\.[a-z]{3,4}$', email1))

        email2 = email.address('Vitaly Samigullin')
        self.assertTrue(email2.startswith('vitaly_samigullin'))

    def test_body(self):
        body1 = email.body(separator='|')
        self.assertEqual(len(body1.split('|')), 2)

        body2 = email.body(as_list=True)
        self.assertEqual(len(body2), 2)

        body3 = email.body(html=True, as_list=True)

        for paragraph in body3:
            self.assertTrue(paragraph.startswith('<p>'))
            self.assertTrue(paragraph.endswith('</p>'))

    def test_subject(self):
        result = email.subject()
        self.assertIn(result[0], string.ascii_uppercase)
        self.assertEqual(len(result.split(' ')), 4)
        self.assertIn(result[-1], '?.!')
