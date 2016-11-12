# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def encode(self):
        encode_subtree = lambda tree: 'X' if tree is None else tree.encode()
        return '%d:(%s,%s)' % (self.key, encode_subtree(self.left), encode_subtree(self.right))

    def __repr__(self):
        return self.encode()
