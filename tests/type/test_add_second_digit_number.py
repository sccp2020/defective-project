import unittest
from src.type.add_second_digit_number import add_second_digit_number


class TestAddSecondDigitNumber(unittest.TestCase):
    def test_add_second_digit_number_cond1(self):
        actual = add_second_digit_number(123, 234)
        expected = 5
        self.assertEqual(actual, expected)

    def test_add_second_digit_number_cond2(self):
        actual = add_second_digit_number(12_345, 4567)
        expected = 10
        self.assertEqual(actual, expected)
