import unittest
from src.type.change_zero_last_bits import change_zero_last_bits


class TestChangeZeroLastBits(unittest.TestCase):
    def test_change_zero_last_bits_1(self):
        actual = change_zero_last_bits('11111'.to_i(2), 4)
        expected = '10000'.to_i(2)
        self.assertEqual(actual, expected)

    def test_change_zero_last_bits_2(self):
        actual = change_zero_last_bits('10101'.to_i(2), 4)
        expected = '10000'.to_i(2)
        self.assertEqual(actual, expected)

    def test_change_zero_last_bits_3(self):
        actual = change_zero_last_bits('1101111'.to_i(2), 3)
        expected = '1101000'.to_i(2)
        self.assertEqual(actual, expected)

    def test_rchange_zero_last_bits_4(self):
        actual = change_zero_last_bits('11'.to_i(2), 4)
        expected = '0'.to_i(2)
        self.assertEqual(actual, expected)
