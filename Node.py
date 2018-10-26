'''
Created on 12 Oct 2018

@author: sgal
'''
class Node:
    pointsTo = []
    left = None
    right = None 
    
    def __init__(self, value, key):
        self.value = value
        self.key = key 
        self.left = None
        self.right = None
        self.pointsTo = []
        
    def getKey(self):
        return self.key
    
    def getValue(self):
        return self.value
    
    def setValue(self,value):
        self.value = value
        
    def getRight(self):
        return self.right
    
    def getLeft(self):
        return self.left
    
    def pointsToNode(self, newNode):
        self.pointsTo.append(newNode)
        
    def returnNodesPointedTo(self, ):
        sent = ""
        for node in self.pointsTo:
            sent = sent + str(node.getKey()) + "\n"
            
        return sent
        
    def hasEdgeTo(self,newNodeKey):
        for node in self.pointsTo:
            if(node.getKey() == newNodeKey):
                return True
        return False
    
    def findIfPathExists(self, dstKey):
        if(self.getKey() == dstKey):
            return True
        for node in self.pointsTo:
            if(node.findIfPathExists(dstKey) == True):
                return True
        return False