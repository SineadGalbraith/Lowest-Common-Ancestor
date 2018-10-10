from Node import Node
import unittest

class TestStringMethods(unittest.TestCase):

	def test_newNode(self):
		node = Node(1, "first")
		self.assertEquals(node.getKey(),1)
		self.assertEquals(node.getVal(), "first")