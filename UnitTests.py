'''
Created on 12 Oct 2018

@author: sgal
'''
import unittest
from Node import Node
from DAG import DAG

class TestStringMethods(unittest.TestCase):

    def test_newNode(self):
        newNode = Node(1, "Node 1")
        
        self.assertEquals(newNode.getValue(), 1)
        self.assertEquals(newNode.getKey(), "Node 1")
        self.assertEquals(newNode.getLeft(), None)
        self.assertEquals(newNode.getRight(), None)
        
        newNode.setValue(2)
        self.assertEquals(newNode.getValue(), 2)
        
    def test_node(self):
        dag = DAG()
        
        node1 = Node(1, "Node 1")
        node2 = Node(2, "Node 2")
        node3 = Node(3, "Node 3")
        
        dag.addNode(node1)
        dag.addNode(node2)
        dag.addNode(node3)
        
        self.assertEqual(dag.returnNode(node1.getKey()),node1)

    def test_addEdge(self):
        directed = DAG()
       
        node1 = Node(1, "Node 1")
        node2 = Node(2, "Node 2")
        node3 = Node(3, "Node 3")
        node4 = Node(4, "Node 4")
        node5 = Node(5, "Node 5")
        
        directed.addNode(node1)
        directed.addNode(node2)
        directed.addNode(node3)
        directed.addNode(node4)
        directed.addNode(node5)

        directed.addEdge(node1, node2)
        directed.addEdge(node2, node3)
        directed.addEdge(node3, node1)
        directed.addEdge(node4, node2)
        directed.addEdge(node2, node5)
        directed.addEdge(node5, node3)
        
        
        self.assertEqual(node1.hasEdgeTo(node2.getKey()), True)
        self.assertEqual(node2.hasEdgeTo(node1.getKey()), False)
        self.assertEqual(node2.hasEdgeTo(node3.getKey()), True)
        self.assertEqual(node3.hasEdgeTo(node2.getKey()), False)
        self.assertEqual(node3.hasEdgeTo(node1.getKey()), True)
        self.assertEqual(node1.hasEdgeTo(node3.getKey()), False)
        self.assertEqual(node4.hasEdgeTo(node2.getKey()), True)
        self.assertEqual(node2.hasEdgeTo(node4.getKey()), False)
        self.assertEqual(node2.hasEdgeTo(node5.getKey()), True)
        self.assertEqual(node5.hasEdgeTo(node2.getKey()), False)
        self.assertEqual(node5.hasEdgeTo(node3.getKey()), True)
        self.assertEqual(node3.hasEdgeTo(node5.getKey()), False)
        

     
    def test_ifPathExists(self):
        dag = DAG()
        valueList = ["Node 1", "Node 2", "Node 3", "Node 4", "Node 5"]
        keyList = [1,2,3,4,5]
        edgeList = [[1,2],[1,4],[2,3],[4,3],[4,5]]
        dag.addMulNode(valueList, keyList)
        dag.addMulEdge(edgeList)
        
        self.assertEqual(dag.existsPathBetween(1,2), True)
        self.assertEqual(dag.existsPathBetween(2,1), False)
        self.assertEqual(dag.existsPathBetween(1,4), True)
        self.assertEqual(dag.existsPathBetween(4,1), False)
        self.assertEqual(dag.existsPathBetween(2,3), True)
        self.assertEqual(dag.existsPathBetween(3,2), False)
        self.assertEqual(dag.existsPathBetween(4,3), True)
        self.assertEqual(dag.existsPathBetween(3,4), False)
        self.assertEqual(dag.existsPathBetween(4,5), True)
        self.assertEqual(dag.existsPathBetween(5,4), False)
        self.assertEqual(dag.existsPathBetween(1,5), True)
        self.assertEqual(dag.existsPathBetween(1,3), True)
        self.assertEqual(dag.existsPathBetween(3,5), False)
        self.assertEqual(dag.existsPathBetween(3,1), False)
    
        
       