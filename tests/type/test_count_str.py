import unittest
from src.type.count_str import count_str

class TestCountStr(unittest.TestCase):
    def test_count_str(self):
        expected = {"a":3, "b":2, "c":1}
        actual = count_str("aaabbbc")
        self.assertEqual(expected, actual)

    def test_count_str2(self):
        expected = {"a":0, "b":5, "c":1}
        actual = count_str("bbcbbb")
        self.assertEqual(expected, actual)
