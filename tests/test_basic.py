# -*- coding: utf-8 -*-

import re
from unittest import TestCase
import datetime

from forgery_py.forgery import basic
from forgery_py.dictionaries_loader import get_dictionary


class BasicForgeryTestCase(TestCase):
    def test_hex_color(self):
        color = basic.hex_color()

        assert re.match(r'[0-9A-F]{6}$', color) is not None

    def test_hex_color_short(self):
        color = basic.hex_color_short()

        assert re.match(r'[0-9A-F]{3}$', color) is not None

    def test_text(self):
        text1 = basic.text(length=10)
        assert len(text1) == 10

        text2 = basic.text(at_least=10, at_most=15)
        assert len(text2) >= 10 and len(text2) <= 15

        text3 = basic.text(length=26, lowercase=False, uppercase=True,
                           digits=False, spaces=False, punctuation=False)
        assert re.match(r'[A-Z]{26}$', text3) is not None

        text4 = basic.text(length=26, lowercase=True, uppercase=False,
                           digits=False, spaces=False, punctuation=False)
        assert re.match(r'[a-z]{26}$', text4) is not None

        text5 = basic.text(length=10, lowercase=False, uppercase=False,
                           digits=True, spaces=False, punctuation=False)
        assert re.match(r'[0-9]{10}$', text5) is not None

        text6 = basic.text(length=1, lowercase=False, uppercase=False,
                           digits=False, spaces=True, punctuation=False)
        assert text6 == ' '

        text7 = basic.text(length=32, lowercase=False, uppercase=False,
                           digits=False, spaces=False, punctuation=True)
        assert re.match(r"""[!"#$%&\\'()*+,-\.\/:;<=>?@\[\]^_`{|}~]{32}$""",
                        text7) is not None

        text8 = basic.text(length=0, at_least=0, at_most=0, lowercase=False,
                           spaces=False, uppercase=False, digits=False,
                           punctuation=False)

        self.assertEqual(text8, '')

    def test_boolean(self):
        result = basic.boolean()
        self.assertTrue(result in [True, False])
        self.assertFalse(result in
                         ['true', 'false', 'True', 'False', 'yes', 'no'])

    def test_color(self):
        result = basic.color()
        self.assertTrue(result + '\n' in get_dictionary('colors'))

    def test_encrypt(self):
        salt = str(datetime.datetime(2007, 12, 6, 16, 29, 43, 79043))
        encrypt1 = basic.encrypt()
        self.assertTrue(len(encrypt1) == 40)
        self.assertTrue(encrypt1 != basic.encrypt())
        self.assertTrue(encrypt1 !=
                        basic.encrypt('password',
                                      str(datetime.datetime.utcnow())))
        encrypt2 = basic.encrypt(salt=salt)
        self.assertTrue(len(encrypt2) == 40)
        self.assertTrue(encrypt2 !=
                        basic.encrypt('password',
                                      str(datetime.datetime.utcnow())))

    def test_frequency(self):
        result = basic.frequency()
        self.assertTrue(result + '\n' in get_dictionary('frequencies'))

    def test_number(self):
        result = basic.number()
        self.assertTrue(0 <= result < 10)
        self.assertTrue(10 <= basic.number(10, 20) < 20)

    def test_password(self):
        password1 = basic.password(at_least=10, at_most=15)
        self.assertTrue(10 <= len(password1) <= 15)

        password2 = basic.password(at_least=10, at_most=10, lowercase=False,
                                   uppercase=True, digits=False, spaces=False,
                                   punctuation=False)
        self.assertTrue(re.match(r'[A-Z]{10}$', password2) is not None)

        password3 = basic.password(at_least=4, at_most=5, lowercase=True,
                                   uppercase=False, digits=False, spaces=False,
                                   punctuation=False)
        self.assertTrue(re.match(r'[a-z]{4,}$', password3) is not None)

        password4 = basic.text(at_least=10, lowercase=False, uppercase=False,
                               digits=True, spaces=False, punctuation=False)
        self.assertTrue(re.match(r'[0-9]{10,}$', password4) is not None)

        password5 = basic.text(at_least=32, at_most=32, lowercase=False,
                               uppercase=False, digits=False, spaces=False,
                               punctuation=True)
        self.assertTrue(
            re.match(r"""[!"#$%&\\'()*+,-\.\/:;<=>?@\[\]^_`{|}~]{32}$""",
                     password5) is not None)
