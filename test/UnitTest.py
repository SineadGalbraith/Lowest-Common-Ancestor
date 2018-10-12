'''
Created on 12 Oct 2018

@author: sgal
'''
from Node import Node
import unittest
from faulthandler import _read_null

class TestStringMethods(unittest.TestCase):

    def test_newNode(self):
        node = Node(1, "first")
        self.assertEquals(node.getKey(),1)
        self.assertEquals(node.getValue(), "first")
        self.assertEquals(node.getLeft(), None)
        self.assertEquals(node.getRight(), None)
