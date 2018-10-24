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
        

    def test_addEdge(self):
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
        
    def test_node(self):
        dag = DAG()
        
        node1 = Node(1, "Node 1")
        node2 = Node(2, "Node 2")
        node3 = Node(3, "Node 3")
        
        dag.addNode(node1)
        dag.addNode(node2)
        dag.addNode(node3)
        
        self.assertEqual(dag.returnNode(node1.getKey()),node1)
        
    def test_findPathBetween(self):
        dag = DAG()
        
        node1 = Node(1, "Node 1")
        node2 = Node(2, "Node 2")
        node3 = Node(3, "Node 3")
        node4 = Node(4, "Node 4")
        node5 = Node(5, "Node 5")
        node6 = Node(6, "Node 6")
        node7 = Node(7, "Node 7")
        node8 = Node(8, "Node 8")
        node9 = Node(9, "Node 9")
        node10 = Node(10, "Node 10")
        
        dag.addNode(node1)
        dag.addNode(node2)
        dag.addNode(node3)
        dag.addNode(node4)
        dag.addNode(node5)
        dag.addNode(node6)
        dag.addNode(node7)
        dag.addNode(node8)
        dag.addNode(node9)
        dag.addNode(node10)
        
        # 1->2
        # 1->3
        # 1->10
        # 2->6
        # 2->8
        # 3->4
        # 4->5
        # 5->6
        # 5->9
        # 6->4
        # 6->7
        # 7->10
        dag.addEdge(node1, node2)
        dag.addEdge(node1, node3)
        dag.addEdge(node1, node10)
        dag.addEdge(node2, node6)
        dag.addEdge(node2, node8)
        dag.addEdge(node3, node4)
        dag.addEdge(node4, node5)
        dag.addEdge(node5, node6)
        dag.addEdge(node5, node9)
        dag.addEdge(node6, node4)
        dag.addEdge(node6, node7)
        dag.addEdge(node7, node10)
        
        self.assertEqual(dag.existsPathBetween(node1.getKey(), node2.getKey()), True)
        #self.assertEqual(dag.existsPathBetween(node2.getKey(), node6.getKey()), True)
        self.assertEqual(dag.existsPathBetween(node4.getKey(), node10.getKey()), True)
        #self.assertEqual(dag.existsPathBetween(node5.getKey(), node4.getKey()), True)
        #self.assertEqual(dag.existsPathBetween(node6.getKey(), node10.getKey()), True)
        
        
        
        
        
        