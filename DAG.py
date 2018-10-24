'''
Created on 12 Oct 2018

@author: sgal
'''
from platform import node
from Node import Node
class DAG:
    
    digraph = [] 
    
    def __init__(self):
        self.resetGraph()
        
    def resetGraph(self):
        self.digraph = []
        
    def addEdge(self, node1, node2):
        node1.pointsToNode(node2)
        
    def addNode(self, newNode):
        for node in self.digraph:
            if(node.getKey() == newNode.getKey()):
                node.setValue(newNode.getValue())
                return
        self.digraph.append(newNode)
        
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
        
        