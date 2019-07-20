import unittest
from src.sample import sample


class TestSample(unittest.TestCase):
    def test_sample(self):
        self.assertEqual("Hello", sample())
