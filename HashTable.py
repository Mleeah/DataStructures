if True:
    DICTIONARY_SIZE = 26
    NUMBER = 13

class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
        pass

class HashTable:
    def __init__(self):
        self.list = [None] * DICTIONARY_SIZE

    def hashFunc(self, key):
        return (key * NUMBER) % DICTIONARY_SIZE

    def insert(self, key, value):
        hashValue = self.hashFunc(key)

        if self.list[hashValue] == None:
            self.list[hashValue] = Node(key,value)

        else:
            currentNode = self.list[hashValue]
            while currentNode.next != None:
                if currentNode.key == key:
                    currentNode.value = value
                    return
                
                currentNode = currentNode.next
            currentNode.next = Node(key, value)
        pass

    def find(self, key):
        hashValue = self.hashFunc(key)
        if self.list[hashValue] != None:

            currentNode = self.list[hashValue]
            while currentNode.next != None:
                if currentNode.key == key:
                    #print("your value is in list")
                    return currentNode.value                    
                currentNode = currentNode.next
            if currentNode.key == key:
                return currentNode.value

        else:
            print("There is no such key")
            return
            
        pass
        pass

    def remove(self, key):
        hashValue = self.hashFunc(key)

        
        if self.list[hashValue] != None:
            currentNode = self.list[hashValue]
            previousNode = currentNode
            count = 0
            while currentNode.next != None:
                if currentNode.key == key:
                    if count == 0:
                        self.list[hashValue] = currentNode.next
                    else:
                        previousNode.next = currentNode.next
                        
                count += 1
                previousNode = currentNode
                currentNode = currentNode.next
                
        else:
            return
        

if True:
    hashTable = HashTable()
    hashTable.insert(10, "banana")
    hashTable.insert(30, "apple")
    print(hashTable.find(10))
    print(hashTable.find(13))
    hashTable.remove(10)
    print(hashTable.find(10))
    hashTable.remove(13)
    pass