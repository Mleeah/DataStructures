class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

        
class Deque:
    def __init__ (self, value):
        self.head = Node(value)
        self.tail = Node(value)

        self.head.next = self.tail
        self.tail.previous = self.head
        self.length = 1

    def addRear(self, value):
        
        if self.length == 1:
            self.tail.value = value
            self.length += 1
        else:
            node = Node(value)
            self.tail.previous.next = node
            node.previous = self.tail.previous
            
            node.next = self.tail
            self.tail.previous = node
            self.length += 1

            """
            beforeUpdateTailNode = self.tail
            beforeUpdateTailNode.next = Node(value)
            beforeUpdateTailNode.next.previous = beforeUpdateTailNode
            
            self.length += 1
            
            newNode.next = self.tail

            self.tail.previous.next = newNode
            self.tail.previous = newNode
            self.tail.value = value
            self.length += 1
            """

    def removeRear(self):

        prevNode = self.tail.previous
        self.tail.previous = prevNode.previous
        value = self.tail.value
        self.tail.next = None
        
        return value
        

    def printQue(self):
        currentNode = self.head
        count = 0
        if self.length == 1:
            print(self.head.value)
            return
        
        while currentNode != None:
            print(currentNode.value, " ", count)
            count+=1
            currentNode = currentNode.next  

    def addFront(self, value):
        
        pass

    def removeFront(self):
        currentNode = self.head

        value = currentNode.value
        currentNode = currentNode.next
        self.head = currentNode
        self.length -= 1

        return value

        


if True:
    que = Deque(10)
    que.addRear(2)
    que.addRear(3)
    que.addRear(5)

    que.printQue()
    print()
    print(que.removeFront())
    print(que.removeRear())
    print()
    que.printQue()