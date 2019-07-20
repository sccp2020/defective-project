import unittest
from src.type.compare_length import compare_length


class TestCompareLength(unittest.TestCase):
    def test_compare_length_cond1(self):
        actual = compare_length(12_345, 67_890)
        self.assertTrue(actual)

    def test_compare_length_cond2(self):
        actual = compare_length(12, 122)
        self.assertFalse(actual)
