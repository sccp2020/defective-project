import unittest
from src.type.sec_to_time import sec_to_time


class TestSecToTime(unittest.TestCase):
    def test_sec_to_time1(self):
        actual = sec_to_time(3600)
        expected = '01:00:00'
        self.assertEqual(actual, expected)

    def test_sec_to_time2(self):
        actual = sec_to_time(46_979)
        expected = '13:02:59'
        self.assertEqual(actual, expected)
