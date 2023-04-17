"""
Created on Sun Apr 8 2023

@author: Adan Alvarez
"""
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    #  añadir edge
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            # asignacion nodos padre
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):

        # El arbol de alto rango
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x

        else:
            parent[y] = x
            rank[x] += 1

    #  Funcion Kruskal Pyton
    def KruskalMST(self):

        #  guardara el resultante en MST
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Numeros de bordes
        while e < self.V - 1:

            # Escoge el menor  y lo incrementa
            # se crea una bandera para la siguiente iteracion
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else descarta el edge

        minimumCost = 0
        print("\nBordes en el MST construido")
        for u, v, peso in result:
            minimumCost += peso
            print("%d -- %d == %d" % (u, v, peso ))
        print("Arbol de expansion Minima", minimumCost)


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    # Llamar funcion principal
    g.KruskalMST()
