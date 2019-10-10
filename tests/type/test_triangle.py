import unittest
from src.type.triangle import triangle


class TestTriangle(unittest.TestCase):
    def test_triangle1(self):
        actual = triangle(3, 4, 5)
        self.assertTrue(actual)

    def test_triangl2(self):
        actual = triangle(3, 3, 7)
        self.assertFalse(actual)

    def test_triangl3(self):
        actual = triangle(2, 2, 2)
        self.assertTrue(actual)
