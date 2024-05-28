class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        self.node = Node(value)
        
    def insert(self, value):
        newNode = Node(value)
        newNode.next = self.node
        self.node = newNode
       
    
    def pop(self):
        currentNode = self.node
        value = currentNode.value
        self.node = self.node.next
        return value
    
    def printStack(self):
        currentNode = self.node
        while currentNode.next != None:
            print(currentNode.value)
            currentNode = currentNode.next
        print(currentNode.value)


if True:
    stack = Stack(1)
    stack.insert(2)
    stack.insert(3)
    stack.insert(4)
    stack.insert(2)
    stack.insert(2)
    stack.printStack()
    print()
    print()
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    stack.insert(20)
    print()
    print()
    stack.printStack()


    