import unittest
from src.type.string_plus import string_plus


class TestStringPlus(unittest.TestCase):
    def test_string_plus_number(self):
        actual = string_plus(123, 456)
        expected = "123456"
        self.assertEqual(actual, expected)

    def test_string_plus_bool(self):
        actual = string_plus(True, False)
        expected = "TrueFalse"
        self.assertEqual(actual, expected)
