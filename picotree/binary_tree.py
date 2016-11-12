# -*- coding: utf-8 -*-

from .node import Node
from .parser import parse_node

class BinaryTree(object):
    def __init__(self, root=None):
        assert type(root) is Node
        self.root = root

    @classmethod
    def from_str(cls, marshalled):
        assert type(marshalled) is str

        p = parse_node(marshalled)
        assert p[0] != None

        return cls(root=p[1])

    def __repr__(self):
        return str(self.root)
