import unittest
from src.algorithm.map_normal import map_normal

class TestMapNormal(unittest.TestCase):
    def test_map_normal_cond1(self):
        arr = [2, 3, 6]
        actual = map_normal(arr, lambda x: x*2 )
        expected = [4, 6, 12]
        self.assertEqual(actual, expected)

    def test_map_normal_cond2(self):
        arr = [8, 4, 2]
        actual = map_normal(arr, lambda x: x//2)
        expected = [4, 2, 1]
        self.assertEqual(actual, expected)

    def test_map_normal_cond3(self):
        arr = [0, 7, 2, 3, 4, 5, 1]
        actual = map_normal(arr, lambda x: x%2==0)
        expected = [True, False, True, False, True, False, False]
        self.assertEqual(actual, expected)
