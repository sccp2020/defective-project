import unittest
from src.type.triangle import triangle


class TestCompareLength(unittest.TestCase):
    def test_compare_length_cond1(self):
        actual = triangle(3, 4, 5)
        self.assertTrue(actual)

    def test_compare_length_cond2(self):
        actual = triangle(3, 3, 7)
        self.assertFalse(actual)
