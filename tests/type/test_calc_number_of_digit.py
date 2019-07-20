import unittest
from src.type.calc_number_of_digit import calc_number_of_digit


class TestCalcNumberOfDigit(unittest.TestCase):
    def test_calc_number_of_digi_cond1(self):
        actual = calc_number_of_digit(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_calc_number_of_digi_cond2(self):
        actual = calc_number_of_digit(100)
        expected = 3
        self.assertEqual(actual, expected)

    def test_calc_number_of_digi_cond3(self):
        actual = calc_number_of_digit(123_456_789)
        expected = 9
        self.assertEqual(actual, expected)
