import unittest
from love_functions import in_love

class Testlove(unittest.TestCase):
	
	def test_love_is_both_even(self):
		result = in_love(2, 4)
		self.assertFalse(result)

	def test_love_is_both_odd(self):
		result = in_love(3, 5)
		self.assertFalse(result)

	def test_love_is_odd_even(self):
		result = in_love(7, 6)
		self.assertTrue(result)

	def test_love_is_even_odd(self):
		result = in_love(8, 9)
		self.assertTrue(result)