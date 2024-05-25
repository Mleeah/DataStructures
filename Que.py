class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class TailNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        
class Que:
    def __init__ (self, value):
        self.head = Node(value)
        self.tail = TailNode(value)
        self.head.next = self.tail
        self.tail.previous = self.head
        self.length = 1

    def add(self, value):
        newNode = Node(self.tail.value)
        if self.length == 1:
            self.tail.value = value
            self.length += 1
        else:
            newNode.next = self.tail
            self.tail.previous.next = newNode
            self.tail.previous = newNode
            self.tail.value = value
            self.length += 1

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

    def pop(self):
        value = self.head.value
        self.head = self.head.next
        self.length -= 1

        return value

        


if True:
    que = Que(10)
    que.add(2)
    que.add(3)
    que.printQue()
    print(que.pop())
    que.printQue()