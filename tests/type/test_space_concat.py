import unittest
from src.type.space_concat import space_concat


class TestSpaceConcat(unittest.TestCase):
    def test_space_concat1(self):
        actual = space_concat('123', '456')
        expected = '123 456'
        self.assertEqual(actual, expected)

    def test_space_concat2(self):
        actual = space_concat('123', ' 345')
        expected = '123  345'
        self.assertEqual(actual, expected)
