class Node:
    def __init__(self, value):
        self.value = value
        self.nodes = list()

class Trie:
    def __init__(self):
        self.nodes = [Node(None)]
    
    def insert_key(self, value):
        currentList = self
        for i in range(len(value)):
            foundNode = -1
            for j in range(len(currentList.nodes)):
                if value[i] == currentList.nodes[j].value:
                    foundNode = j
                    break

            if foundNode == -1:
                currentList.nodes.append(Node(value[i]))
                currentList = currentList.nodes[-1]
            if foundNode != -1:
                currentList = currentList.nodes[foundNode]
            
                            

    def search_key(self, value):
        currentList = self
        for i in range(len(value)):
            foundNode = -1
            for j in range(len(currentList.nodes)):
                print(currentList.nodes[j].value, " ", end="")
                if value[i] == currentList.nodes[j].value:
                    foundNode = j
                    break
            #print()        
            if foundNode == -1:
                return False
            if foundNode != -1:
                currentList = currentList.nodes[foundNode]
        return True
        


if True:
    root = Trie()
    inputStrings = ["apple", "banana","pear","peach","watermelon","cherry","melon"]
    for i in range(len(inputStrings)):
        root.insert_key(inputStrings[i])

    print("gone trough inserting")
    findStrings = ["apple","peach","watermelon","melon", "oow", "appple"]
    for i in range(len(findStrings)):
        if root.search_key(findStrings[i]):
            print(findStrings[i], " string is present in data base")
        else:
            print(findStrings[i], " string is not in data base")


