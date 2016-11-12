# -*- coding: utf-8 -*-

import unittest

from .context import picotree
from picotree import BinaryTree, Node

class BinaryTreeParserTest(unittest.TestCase):
    """For testing the parser (duh!)."""

    def test_depth_one(self):
        marshalled_tree = '1:(X,X)'
        actual_tree = BinaryTree(root=Node(key=1))
        self.assertEqual(str(BinaryTree.from_str(marshalled_tree)), str(actual_tree))

    def test_depth_two(self):
        marshalled_tree = '1:(2:(X,X),3:(X,X))'
        actual_tree = BinaryTree(root=Node(key=1, left=Node(key=2), right=Node(key=3)))
        self.assertEqual(str(BinaryTree.from_str(marshalled_tree)), str(actual_tree))

    def test_depth_three(self):
        marshalled_tree = '1:(2:(4:(1:(X,X),2:(X,X)),5:(X,X)),3:(6:(X,X),X))'
        actual_tree = BinaryTree(root=Node(key=1, left=Node(key=2, left=Node(key=4, left=Node(key=1), right=Node(key=2)), right=Node(key=5)), right=Node(key=3, left=Node(key=6))))
        self.assertEqual(str(BinaryTree.from_str(marshalled_tree)), str(actual_tree))

if __name__ == '__main__':
    unittest.main()
