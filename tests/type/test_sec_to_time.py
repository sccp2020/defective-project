import unittest
from src.type.sec_to_time import sec_to_time


class TestCompareLength(unittest.TestCase):
    def test_compare_length_cond1(self):
        actual = sec_to_time(3600)
        expected = '01:00:00'
        self.assertEqual(actual, expected)

    def test_compare_length_cond2(self):
        actual = sec_to_time(46_979)
        expected = '13:02:59'
        self.assertEqual(actual, expected)
