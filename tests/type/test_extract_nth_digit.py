import unittest
from src.type.extract_nth_digit import extract_nth_digit


class TestExtractNthDigit(unittest.TestCase):
    def test_extract_nth_digit_cond1(self):
        actual = extract_nth_digit(123_456, 3)
        expected = 4
        self.assertEqual(actual, expected)

    def test_extract_nth_digit_cond2(self):
        actual = extract_nth_digit(123_456_789, 6)
        expected = 4
        self.assertEqual(actual, expected)
