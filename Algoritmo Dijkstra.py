"""
Created on Sun Mar 26 2023

@author: Adan Alvarez
"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# No de conecciones
num_filas = int(input("Ingrese el número de conexiones: "))

# Crear una matriz tipo de datos 'object'
array = np.empty((num_filas, 3), dtype='object')

# Entrada de datos
for i in range(num_filas):
    array[i][0] = input("Ingresa el Origen: ")
    array[i][1] = input("Ingresa el Destino: ")
    array[i][2] = input("Ingresa el Peso: ")

# Crear un grafo no dirigido vacío
grafo = nx.Graph()
# Crear un grafo dirigido para dijkstra
subgrafo = nx.DiGraph()

### Nodos de origen
origenes = set([fila[0] for fila in array])
### Nodos de destino
destinos = set([fila[1] for fila in array])
# se agregan todos los nodos a los grafos
nodos = origenes.union(destinos)
grafo.add_nodes_from(nodos)

#Se recorre el array y se toman los valores del
#origen, destino y peso para agregarlos al grafo
for fila in array:
    origen = fila[0]
    destino = fila[1]
    peso = int(fila[2])
    grafo.add_edge(origen, destino, peso=peso)

# Obtener los pesos de las conexiones
pesos = nx.get_edge_attributes(grafo, 'peso')

# Dibujar el grafo con los pesos de las conexiones
nx.draw(grafo, pos=nx.spectral_layout(grafo), with_labels=True, node_size=500, font_size=12, font_weight='bold')
nx.draw_networkx_edge_labels(grafo, pos=nx.spectral_layout(grafo), edge_labels=pesos)

dij = list(nx.dijkstra_path(grafo, source=input("¿Cual es el nodo de origen?"), target=input("¿Cual es el nodo de Destino?"), weight='peso'))
print(dij)

subgrafo.add_nodes_from(dij)
#se crean los pares de nodos para add_edges y generar el nuevo grafo
pares_nodos = [(dij[i], dij[i+1]) for i in range(len(dij)-1)]
pos = {pares_nodos[i]:[1,i] for i in range(len(pares_nodos)-1)}
subgrafo.add_edges_from(pares_nodos)
fig, ax = plt.subplots(figsize=(8,2))
nx.draw(subgrafo, with_labels=True, ax=ax)