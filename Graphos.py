class Vertice: 
    def __int__(self, id):
        self.id  = id
        self.vistado = False
        self.nivel = -1
        self.vecinos = []
    
    def agregarVecinos(self, v):
        if not v in self.vecinos:
            self.vecinos.append(v)

class Grafica:
    def __init__(self):
        self.vertices = {}

    def agregaVertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)
    
    def agregarArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecinos(b)
            self.vertices[b].agregaVecinos(a)

def main():
    grafica = Grafica()

    i = [0,1,2,3,4,5,6]
    for v in i:
        grafica.agregaVertice(v)
    
    l = [2,0,0,6,6,3,0,5,6,5,0,1,6,4,1,4]
    for i in range(0, len(1) -1,2):
        grafica.agregarArista(l[i], l[i] + 1)

    for v in grafica.vertices:
        print(v,grafica.vertices[v].vecinos)
    
main()