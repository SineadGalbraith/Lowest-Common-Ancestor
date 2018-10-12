from _overlapped import NULL
class Node :
    value = 0
    key = ""
    left = None
    right = None

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
