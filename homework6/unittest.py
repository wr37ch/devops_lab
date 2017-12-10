import unittest
import task6


class Test(unittest.TestCase):

    def setUp(self):
        """init"""

    def test_if_empty(self):
        """tests if dict is empty"""
        self.assertTrue(task6.dictionary)

    def tearDown(self):
        """finish"""


