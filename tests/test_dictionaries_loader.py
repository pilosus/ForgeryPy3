# -*- coding: utf-8 -*-

from unittest import TestCase
from forgery_py.dictionaries_loader import get_dictionary


class GetDictionaryTestCase(TestCase):
    def test_non_existent_test(self):
        with self.assertRaises(KeyError):
            get_dictionary('non_existent_file')
