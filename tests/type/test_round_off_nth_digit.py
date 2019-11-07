import unittest
from src.type.round_off_nth_digit import round_off_nth_digit


class TestRoundOffNthDigit(unittest.TestCase):
    def test_round_off_nth_digit1(self):
        num = 123.456
        digit = 2

        actual = round_off_nth_digit(num, digit)
        expected = round(num, digit)

        self.assertEqual(actual, expected)

    def test_round_off_nth_digit2(self):
        num = 123.456
        digit = 0

        actual = round_off_nth_digit(num, digit)
        expected = round(num, digit)

        self.assertEqual(actual, expected)
