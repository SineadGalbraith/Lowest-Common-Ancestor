'''
Created on 12 Oct 2018

@author: sgal
'''
import unittest
from Node import Node
from DAG import DAG

class TestStringMethods(unittest.TestCase):

    def test_newNode(self):
        node1 = Node(1, "Node 1")
        
        self.assertEquals(node1.getValue(), 1)
        self.assertEquals(node1.getKey(), "Node 1")
        self.assertEquals(node1.getLeft(), None)
        self.assertEquals(node1.getRight(), None)
        
        node1.setValue(2)
        self.assertEquals(node1.getValue(), 2)
        
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
        dag = DAG()
       
        node1 = Node(1, "Node 1")
        node2 = Node(2, "Node 2")
        node3 = Node(3, "Node 3")
        node4 = Node(4, "Node 4")
        node5 = Node(5, "Node 5")
        
        dag.addNode(node1)
        dag.addNode(node2)
        dag.addNode(node3)
        dag.addNode(node4)
        dag.addNode(node5)

        dag.addEdge(node1, node2)
        dag.addEdge(node2, node3)
        dag.addEdge(node3, node1)
        dag.addEdge(node4, node2)
        dag.addEdge(node2, node5)
        dag.addEdge(node5, node3)
        
        
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
        
    def test_addAcyclicEdge(self):
        dag = DAG()
        valueList = ["Node 1", "Node 2", "Node 3", "Node 4", "Node 5", "Node 6", "Node 7", "Node 8", "Node 9"]
        keyList = [1,2,3,4,5,6,7,8,9]
        edgeList = [[1,2],[1,4],[2,3],[4,3],[4,5]]
        dag.addMulNode(valueList, keyList)
        dag.addMulEdge(edgeList)
        
        dag.addAcyclicEdge(7,8)
        dag.addAcyclicEdge(9,2)
        dag.addAcyclicEdge(5,8)
        dag.addAcyclicEdge(9,7)
        
        self.assertEqual(dag.existsPathBetween(7,8),True)
        self.assertEqual(dag.existsPathBetween(9,2),True)
        self.assertEqual(dag.existsPathBetween(2,9),False)
        self.assertEqual(dag.existsPathBetween(5,8),True) 
        self.assertEqual(dag.existsPathBetween(8,5),False)
        self.assertEqual(dag.existsPathBetween(9,7),True)
        self.assertEqual(dag.existsPathBetween(7,9),False)
        self.assertEqual(dag.existsPathBetween(1,8),True)
        self.assertEqual(dag.existsPathBetween(9,8),True)
        self.assertEqual(dag.existsPathBetween(4,9),False)
        self.assertEqual(dag.existsPathBetween(2,5),False)
        self.assertEqual(dag.addAcyclicEdge(8,1), -1)
        
    def test_LCA(self):
        dag = DAG()
        valueList = ["Node 1", "Node 2", "Node 3", "Node 4", "Node 5", "Node 6", "Node 7", "Node 8", "Node 9", "Node 10"]
        keyList = [1,2,3,4,5,6,7,8,9,10]
        edgeList = [[1,2],[1,4],[2,3],[2,5],[4,3],[4,5],[5,7],[5,10],[2,6],[6,7],[6,8],[3,9]]
        dag.addMulNode(valueList, keyList)
        dag.addMulEdge(edgeList)
        
        self.assertEqual(dag.lca(1,6,9),2)
        self.assertEqual(dag.lca(1,2,4),1)
        self.assertEqual(dag.lca(1,8,10),6)
        self.assertEqual(dag.lca(3,1,9),3)
        self.assertEqual(dag.lca(3,9,10),3)

    
        
        
        
        
        
        
        
        
    
        
       