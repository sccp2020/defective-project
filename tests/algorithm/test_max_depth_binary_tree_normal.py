import unittest
from src.algorithm.max_depth_binary_tree_normal import max_depth_binary_tree

class TestMaxDepthBinaryTree(unittest.TestCase):
    def test_max_depth_binary_tree_cond_1(self):
        expected = 2
        actual = max_depth_binary_tree([1,2,None])
        self.assertEqual(actual, expected)

    def test_max_depth_binary_tree_cond_2(self):
        expected = 4
        actual = max_depth_binary_tree([1, 2, 3, 4, 5, 6, None, 8])
        self.assertEqual(actual, expected)

    def test_max_depth_binary_tree_cond_3(self):
        expected = 5
        actual = max_depth_binary_tree([1, 2, 3, 4, 5, 6, None, 8, 9, 10, 11, 12, 13, 14])
        self.assertEqual(actual, expected)

    def test_max_depth_binary_tree_cond_4(self):
        tree = [1, None, 4, None, None, None, 9, None, None, None, None, None, None, 2, None]
        expected = 4
        actual = max_depth_binary_tree(tree)
        self.assertEqual(actual, expected)

    def test_max_depth_binary_tree_cond_5(self):
        tree = []
        expected = 0
        actual = max_depth_binary_tree(tree)
        self.assertEqual(actual, expected)

    def test_max_depth_binary_tree_cond_6(self):
        tree = [1]
        expected = 1
        actual = max_depth_binary_tree(tree)
        self.assertEqual(actual, expected)
