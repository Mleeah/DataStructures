class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Deque:
    def __init__(self, value):
        self.left = None
        self.rigth = None
        self.head = Node(value)
        self.tail = self.head
        self.size = 1
    
    def addEnd(self, value):
        pass
    def addFront(self, value):
        pass

    def popEnd(self):
        pass
    def popFront(self):
        pass

    def 
