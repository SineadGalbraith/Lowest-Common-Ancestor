'''
Created on 12 Oct 2018

@author: sgal
'''
from Node import Node
class DAG:
    
    digraph = [] 
    
    def __init__(self, digraph = None):
        self.digraph = []
        
    def addEdge(self, startNode, endNode):
        startNode.pointsToNode(endNode)
        
    def addEdgeUsingKey(self, key1,key2):
        node1 = self.returnNodeByKey(key1)
        node2 = self.returnNodeByKey(key2)
        if(key1!=key2 and node1 != None and node2 != None):
            self.addEdge(node1, node2)
            
    def addAcyclicEdge(self, key1, key2):
        if(self.existsPathBetween(key2, key1) == False):
            self.addEdgeUsingKey(key1, key2)
            return
        return -1
    
    def addMulEdge(self, edgeList):
        for edge in edgeList:
            self.addEdgeUsingKey(edge[0], edge[1])
        
        
    def addNode(self, newNode):
        for node in self.digraph:
            if(node.getKey() == newNode.getKey()):
                node.setValue(newNode.getValue())
                return
        self.digraph.append(newNode)
        
    def addMulNode(self, valueList, keyList):
        x = 0 
        for key in keyList:
            value = valueList[x]
            x= x+1
            node = Node(value, key)
            self.addNode(node)
        
    def returnNode(self, nodeKey):
        for node in self.digraph:
            if(node.getKey() == nodeKey):
                return node
        return None
    
    def returnNodeByKey(self, nodeKey):
        for node in self.digraph:
            if node.key == nodeKey:
                return node
        return None
    
    def existsPathBetween(self,startKey,endKey):
        node = self.returnNodeByKey(startKey)
        if(node==None):
            return False
        return node.findIfPathExists(endKey)
        
        