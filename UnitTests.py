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
        
        directed.addNode(node1)
        directed.addNode(node2)
        
        directed.addEdge(node1, node2)
        
        self.assertEqual(node1.hasEdgeTo(node2.getKey()), True)
        self.assertEqual(node2.hasEdgeTo(node1.getKey()), False)
        
    def test_ifPathExists(self):
        dag = DAG()
        valueList = ["Node 1", "Node 2", "Node 3", "Node 4", "Node 5"]
        keyList = [1,2,3,4,5]
        edgeList = [[1,2],[1,4],[2,3],[4,3],[4,5]]
        dag.addMulNode(valueList, keyList)
        dag.addMulEdge(edgeList)
        node1 = dag.returnNodeByKey(1)
        node2 = dag.returnNodeByKey(2)
        node3 = dag.returnNodeByKey(3)
        node4 = dag.returnNodeByKey(4)
        node5 = dag.returnNodeByKey(5)
        self.assertEquals(node1.hasEdgeTo(node2.getKey()),True)
        self.assertEquals(node1.hasEdgeTo(node4.getKey()),True)
        self.assertEquals(node2.hasEdgeTo(node3.getKey()),True)
        self.assertEquals(node4.hasEdgeTo(node3.getKey()),True)
        self.assertEquals(node4.hasEdgeTo(node5.getKey()),True)
        
        
        
        
        
    def test_addAcyclicEdge(self):
        acyclicGraph = DAG()
        
        node1 = Node(1, "Node 1")
        node2 = Node(2, "Node 2")
        node3 = Node(3, "Node 3")
        node4 = Node(4, "Node 4")
        node5 = Node(5, "Node 5")
        
        acyclicGraph.addNode(node1)
        acyclicGraph.addNode(node2)
        acyclicGraph.addNode(node3)
        acyclicGraph.addNode(node4)
        acyclicGraph.addNode(node5)
        
        acyclicGraph.addAcyclicEdge(1,2)
        #self.assertEqual(node1.hasEdgeTo(node2.getKey()), True)
        
        
        
        
        
        
        
        
        
        
        
        
       