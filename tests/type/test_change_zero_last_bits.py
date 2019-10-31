import unittest
from src.type.change_zero_last_bits import change_zero_last_bits


class TestChangeZeroLastBits(unittest.TestCase):
    def test_change_zero_last_bits_1(self):
        actual = change_zero_last_bits(int('11111', 2), 4)
        expected = int('10000', 2)
        self.assertEqual(actual, expected)

    def test_change_zero_last_bits_2(self):
        actual = change_zero_last_bits(int('10101', 2), 4)
        expected = int('10000', 2)
        self.assertEqual(actual, expected)

    def test_change_zero_last_bits_3(self):
        actual = change_zero_last_bits(int('1101111', 2), 3)
        expected = int('1101000', 2)
        self.assertEqual(actual, expected)

    def test_rchange_zero_last_bits_4(self):
        actual = change_zero_last_bits(int('11', 2), 4)
        expected = int('0', 2)
        self.assertEqual(actual, expected)
