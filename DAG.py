'''
Created on 12 Oct 2018

@author: sgal
'''
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
        
        