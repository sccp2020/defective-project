import unittest
from src.type.string_format import string_format


class TestCompareLength(unittest.TestCase):
    def test_compare_length_cond1(self):
        actual = string_format("123", "456")
        expected = 'Result: 579'
        self.assertEqual(actual, expected)

    def test_compare_length_cond2(self):
        actual = string_format('123', '345')
        expected = 'Result: 468'
        self.assertEqual(actual, expected)
