class Node: 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def rebalance(self):
        
        values = self.getAllValues()
        values.sort()
        valueCount = len(values)
        middle = round(valueCount/2)
       
        newRoot = BinarySearchTree(values[middle])
        values.pop(middle)
        for i in range(valueCount-1):
            newRoot.insert(values[i])
            pass

        return newRoot 

        pass

    def insert(self, value):
        newNode = Node(value)
        currentNode = self
        while True:
            if value > currentNode.value:
                if currentNode.right != None:
                    currentNode = currentNode.right
                else:
                    currentNode.right = newNode
                    return

            elif value < currentNode.value:
                if currentNode.left != None:
                    currentNode = currentNode.left
                else:
                    currentNode.left = newNode
                    return
            else:
                return

    def find(self, value):
        currentNode = self
        while True:
            if value > currentNode.value:
                if currentNode.right != None:
                    currentNode = currentNode.right
                else:
                    return False

            elif value < currentNode.value:
                if currentNode.left != None:
                    currentNode = currentNode.left
                else:
                    return False
            elif value == currentNode.value:
                return True
            else:
                return False
            
    def remove(self, value):
        pass

    def getAllValues(self):
        array = []
        currentNode = self
        array.append(currentNode.value)
        ## left 
        getBSTvalues(currentNode, array)
        ## right
        
        return array


def getBSTvalues(currentNode, array):

    if currentNode.left != None:
        array.append(currentNode.left.value)
        getBSTvalues(currentNode.left, array)

    if currentNode.right != None:
        array.append(currentNode.right.value)
        getBSTvalues(currentNode.right, array)



if True:
    root = BinarySearchTree(10)
    root.insert(5)
    root.insert(3)
    root.insert(13)
    root.insert(20)

    print(root.getAllValues())
    root.rebalance()
    print(root.getAllValues())
