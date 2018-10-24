'''
Created on 12 Oct 2018

@author: sgal
'''
import unittest
from Node import Node
from DAG import DAG

class TestStringMethods(unittest.TestCase):

    #Test Adding a New Node works correctly
    def test_newNode(self):
        newNode = Node(1, "Node 1")
        
        self.assertEquals(newNode.getValue(), 1)
        self.assertEquals(newNode.getKey(), "Node 1")
        self.assertEquals(newNode.getLeft(), None)
        self.assertEquals(newNode.getRight(), None)
        
        #Set the value of Node 1 to 2
        newNode.setValue(2)
        self.assertEquals(newNode.getValue(), 2)

    def test_edge(self):
        dag = DAG()
        #create 5 new nodes
        node1 = Node(1, "Node 1")
        node2 = Node(2, "Node 2")
        node3 = Node(3, "Node 3")
        
        #add nodes to the digraph
        dag.addNode(node1)
        dag.addNode(node2)
        dag.addNode(node3)
        
        #add edges to DAG
        #Node 1 will point to 2, 3
        dag.addEdge(node1, node2)
        dag.addEdge(node1, node3)
        
        # 1->2        !2->1
        self.assertEqual(node1.hasEdgeTo(node2.getKey()),True)
        self.assertEqual(node2.hasEdgeTo(node1.getKey()),False)
        
        # 1->3        !3->1
        self.assertEqual(node1.hasEdgeTo(node3.getKey()),True)
        self.assertEqual(node3.hasEdgeTo(node1.getKey()),False)
        
        
        
        
        
        
        
        