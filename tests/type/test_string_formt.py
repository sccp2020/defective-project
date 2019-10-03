import unittest
from src.type.string_format import string_format


class TestStringFormat(unittest.TestCase):
    def test_string_format1(self):
        actual = string_format("123", "456")
        expected = 'Result: 579'
        self.assertEqual(actual, expected)

    def test_string_format2(self):
        actual = string_format('123', '345')
        expected = 'Result: 468'
        self.assertEqual(actual, expected)
