
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    #head = Node()
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        newNode = Node(value)
        currentNext = self.head
        while currentNext.next is not None:
            currentNext = currentNext.next
        currentNext.next = newNode

    def insert(self, value, pos):
        newNode = Node(value)

        if pos == 0:
            newNode.next = self.head
            self.head = newNode
            return
        
        count = 0
        currentNext = self.head

        while count < pos-1:
            if currentNext.next is None:
                print("Insertion Out of Bounds")
                return
            count+=1
            currentNext = currentNext.next
        
        newNode.next = currentNext.next
        currentNext.next = newNode

    def remove(self, pos):
        if pos == 0:
            self.head = self.head.next
            return
        
        count = 0
        currentNext = self.head
        previous = self.head
        while count < pos-1:
            if currentNext.next is None:
                print("Insertion Out of Bounds")
                return
            count+=1
            previous = currentNext
            currentNext = currentNext.next
        
        previous = currentNext
        currentNext = currentNext.next
        previous.next = currentNext.next

    def length(self):
        count = 0
        currentNext = self.head
        while currentNext.next is not None:
            count+=1
            currentNext = currentNext.next
        return count+1
    
    def printList(self):
        currentNext = self.head
        while currentNext.next is not None:
            print(currentNext.value)
            currentNext = currentNext.next
        print(currentNext.value)
        


if True:
    root = LinkedList(10)

    root.append(1)
    print("length is ", root.length())
    root.append(5)

    root.append(15)
    root.insert(2, 4)
    root.printList()
    root.remove(4)
    print("length is ", root.length())
    root.printList()
