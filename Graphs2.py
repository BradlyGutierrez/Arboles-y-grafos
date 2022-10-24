class Graph:
    def __init__(self):
        self.nodes = 0
        self.adjacentList = {}
    
    def addvertex(self,node):
        self.adjacentList[node] = []
        self.nodes += 1
    
    def addEdge(self,node1, node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)
    
    def __str__(self):
        return f"""Grafo = {self.adjacentList}"""
        

def main():
    grafica = Graph()

    i = [0,1,2,3,4,5,6]
    for v in i:
        grafica.addvertex(v)
        
    
    grafica.addEdge(2,0)
    grafica.addEdge(0,5)
    grafica.addEdge(5,6)
    grafica.addEdge(0,5)
    grafica.addEdge(6,3)
    grafica.addEdge(6,4)
    grafica.addEdge(1,4)
    grafica.addEdge(0,1)

    print(grafica.adjacentList)
    
main()