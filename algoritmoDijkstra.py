"""
Algoritmo de Dijkstra
Jesus Perez - C.I: 27.877.780
"""

class Vertice:
    
    def __init__(self, i):
        self.id = i
        self.visitado = False
        self.padre = None
        self.vecinos = []
        self.distancia = float('inf')

    def agregarVecino(self, v, p):
        if v not in self.vecinos:
            self.vecinos.append([v, p])

class Grafica:
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)

    def agregarArista(self, a, b, p):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b, p)
            self.vertices[b].agregarVecino(a, p)

    def imprimirGrafica(self):
        for v in self.vertices:
            print("La distancia del vertice "+str(v)+" es "+str(self.vertices[v].distancia)+" llegando desde "+str(self.vertices[v].padre))
            
    def camino(self, a, b):
        camino = []
        actual = b 
        while actual != None:
            camino.insert(0, actual)
            actual = self.vertices[actual].padre
        return [camino, self.vertices[b].distancia]

    def minimo(self, lista):
        if len(lista) > 0:
            m = self.vertices[lista[0]].distancia
            v = lista[0]
            for e in lista:
                if m > self.vertices[e].distancia:
                    m = self.vertices[e].distancia
                    v = e
            return v

    def dijkstra(self, a):
        if a in self.vertices:
            self.vertices[a].distancia = 0
            actual = a
            noVisitados = []

            for v in self.vertices:
                if v != a:
                    self.vertices[v].distancia = float('inf')
                self.vertices[v].padre = None
                noVisitados.append(v)

            while len(noVisitados) > 0:
                for vecino in self.vertices[actual].vecinos:
                    if self.vertices[vecino[0]].visitado == False:
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]].distancia = self.vertices[actual].distancia + vecino[1]
                            self.vertices[vecino[0]].padre = actual

                self.vertices[actual].visitado = True
                noVisitados.remove(actual)

                actual = self.minimo(noVisitados)
        else:
            return False

class main():
    g = Grafica()
    g.agregarVertice(1)
    g.agregarVertice(2)
    g.agregarVertice(3)
    g.agregarVertice(4)
    g.agregarVertice(5)
    g.agregarVertice(6)
    g.agregarVertice(7)
    g.agregarVertice(8)
    g.agregarVertice(9)
    g.agregarArista(1, 2, 4)
    g.agregarArista(1, 3, 9)
    g.agregarArista(2, 3, 11)
    g.agregarArista(2, 5, 9)
    g.agregarArista(3, 4, 7)
    g.agregarArista(3, 6, 1)
    g.agregarArista(4, 6, 6)
    g.agregarArista(5, 8, 4)
    g.agregarArista(5, 4, 2)
    g.agregarArista(6, 8, 2)
    g.agregarArista(7, 5, 7)
    g.agregarArista(8, 7, 15)
    g.agregarArista(8, 9, 11)
    g.agregarArista(7, 9, 10)

    print("\nLa ruta mas rapida por Dijkstra junto con su costo es: ")
    g.dijkstra(1)
    print(g.camino(1, 9))
    print("")
    print("Los valores finales de la grafica son los siguientes: ")
    g.imprimirGrafica()
