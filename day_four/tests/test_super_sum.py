from unittest import TestCase
from super_sum import super_sum 

class SuperSumTestCase(TestCase):
	"""test case for super sum"""


	def test_empty_input(self):
		"""test empty input"""
		self.assertEqual(super_sum(), "please enter numbers")
		