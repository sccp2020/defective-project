import unittest
from src.type.space_concat import space_concat


class TestCompareLength(unittest.TestCase):
    def test_compare_length_cond1(self):
        actual = space_concat('123', '456')
        expected = '123 456'
        self.assertEqual(actual, expected)

    def test_compare_length_cond2(self):
        actual = space_concat('123', ' 345')
        expected = '123  345'
        self.assertEqual(actual, expected)
