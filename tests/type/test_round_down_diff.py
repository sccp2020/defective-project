import unittest
from src.type.round_down_diff import round_down_diff


class TestRoundDownDiff(unittest.TestCase):
    def test_round_down_diff1(self):
        actual = round_down_diff(32.8, 22.3)
        expected = 10
        self.assertEqual(actual, expected)

    def test_round_down_diff2(self):
        actual = round_down_diff(12.4, 9.9)
        expected = 3
        self.assertEqual(actual, expected)
