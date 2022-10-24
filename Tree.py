from turtle import left


class Node: 
    def __init__(self, value, right = None, left=None):
        self.right = right
        self.left = left
        self.value = value

class Tree: 
    def __init__(self) :
        self.root = None
    
    def insert(self,value):
        nodo = Node(value)
        if(self.root == None):
            self.root = nodo
        else:
            currentNode = self.root
            while(currentNode):
                if(currentNode.value > value):
                    if(currentNode.left != None):
                        currentNode.left = nodo
                    currentNode.left = nodo
                else:
                    if(currentNode.left != None):
                        currentNode.right = nodo
                    currentNode.right = nodo

    def search(self, value):
        currentNode = self.root
        while(currentNode.value!=value and currentNode!=value):
            if(currentNode.value < value):
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return currentNode

tree = Tree()
tree.insert(2)
tree.insert(4)
tree.insert(5)
