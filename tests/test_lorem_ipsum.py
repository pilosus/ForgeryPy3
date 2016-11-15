# -*- coding: utf-8 -*-

import re
import string
import random
from unittest import TestCase

from forgery_py.forgery import lorem_ipsum


class LoremIpsumForgeryTestCase(TestCase):
    def test_word(self):
        result = lorem_ipsum.word()
        assert re.match(r'[a-z]+?$', result) is not None

    def test_words(self):
        result = lorem_ipsum.words(5)
        assert len(result.split(' ')) == 5

        result = lorem_ipsum.words(5, as_list=True)
        assert len(result) == 5

    def test_title(self):
        result = lorem_ipsum.title()
        assert result[0] in string.ascii_uppercase
        assert len(result.split(' ')) == 4
        assert result[-1] in '?.!'

    def test_sentence(self):
        result = lorem_ipsum.sentence()
        assert len(result.split('.')) == 2

    def test_sentences(self):
        result = lorem_ipsum.sentences()
        assert len(result.split('.')) == 3

        result2 = lorem_ipsum.sentences(as_list=True)
        self.assertTrue(type(result2) == list)

    def test_paragraph(self):
        result = lorem_ipsum.paragraph()
        assert len(result.split('.')) == 4

    def test_paragraphs(self):
        result = lorem_ipsum.paragraphs(separator='|')
        assert len(result.split('|')) == 2

        result = lorem_ipsum.paragraphs(as_list=True)
        assert len(result) == 2

        result = lorem_ipsum.paragraphs(html=True, as_list=True)

        for paragraph in result:
            assert paragraph.startswith('<p>')
            assert paragraph.endswith('</p>')

    def test_characters(self):
        chars1 = lorem_ipsum.characters()
        self.assertEqual(len(chars1), 10)

        chars2 = lorem_ipsum.characters(25)
        self.assertEqual(len(chars2), 25)

        chars3 = lorem_ipsum.characters(30)
        self.assertEqual(chars3, chars3.lower())

    def test_character(self):
        result = lorem_ipsum.character()
        self.assertEqual(len(result), 1)

    def test_lorem_ipsum_characters(self):
        ipsum1 = lorem_ipsum.lorem_ipsum_characters()
        self.assertEqual(ipsum1, ipsum1.lower())
        self.assertTrue(len(ipsum1) > 10)

    def test_lorem_ipsum_words(self):
        words = lorem_ipsum.lorem_ipsum_words()
        self.assertIsInstance(words, list)

        word = random.choice(words)
        self.assertEqual(word, word.lower())

    def test_text(self):
        char = lorem_ipsum.text("character")
        self.assertEqual(len(char), 1)

        chars1 = lorem_ipsum.text("characters", 10)
        self.assertEqual(len(chars1), 10)

        chars2 = lorem_ipsum.text("characters", quantity=25)
        self.assertEqual(len(chars2), 25)

        chars3 = lorem_ipsum.text("characters", quantity=30)
        self.assertEqual(chars3, chars3.lower())

        word = lorem_ipsum.text("word")
        self.assertIsNotNone(re.match(r'[a-z]+?$', word))

        words = lorem_ipsum.text("words", quantity=5, as_list=True)
        self.assertEqual(len(words), 5)

        sentence = lorem_ipsum.text("sentence")
        self.assertEqual(len(sentence.split('.')), 2)

        sentences = lorem_ipsum.text("sentences")
        self.assertEqual(len(sentences.split('.')), 3)

        paragraph = lorem_ipsum.text("paragraph")
        self.assertEqual(len(paragraph.split('.')), 4)

        paragraphs = lorem_ipsum.text("paragraphs", separator='|')
        self.assertEqual(len(paragraphs.split('|')), 2)

        title = lorem_ipsum.text("title")
        self.assertIn(title[-1], '?.!')

        with self.assertRaises(NameError):
            lorem_ipsum.text(what="no_such_method")
