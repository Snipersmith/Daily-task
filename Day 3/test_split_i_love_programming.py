import unittest
from split_i_love_programming import *

class TestGetSplitWord(unittest.TestCase):

    def test_sentence(self):
        self.assertEqual(get_split_word("I love programming"), ["I", "love", "programming"])

    def test_single_word(self):
        self.assertEqual(get_split_word("Love"), ["Love"])

    def test_empty_string(self):
        self.assertEqual(get_split_word(""), [""])

   