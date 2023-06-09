"""
Created on Sun Apr 9 2023

@author: Adan Alvarez
"""

import networkx as nx
import matplotlib.pyplot as plt

# Lista de grafos ejemplo. Nodo origen, destino y peso
G = [["A", "B", 20], ["A", "C", 7], ["B", "C", 15], ["B", "D", 15], ["C", "D", 25], ["C", "E", 6], ["D", "E", 4], ["C", "F", 7], ["F", "A", 6], ["F", "G", 4], ["G", "E", 20], ["G", "H", 6], ["H", "B", 12]]

# Crear grafo vacio
G_nx = nx.Graph()
# Añadimos los parametros de cada nodo de la lista
for Origen, Destino, Peso in G:
    G_nx.add_edge(Origen, Destino, weight=Peso)

#Arbol Parcial Minimo de Kruskal
T = nx.minimum_spanning_tree(G_nx)

# Arbol de expancion maxima
Maxima = nx.maximum_spanning_tree(G_nx)

# Visualizar el grafo Original
pos = nx.circular_layout(G_nx)

nx.draw_networkx(G_nx, pos, with_labels=True)
#Obtiene el peso de cada nodo del diccionario para mostrarlo
labels = nx.get_edge_attributes(G_nx, 'weight')
nx.draw_networkx_edge_labels(G_nx, pos, edge_labels=labels)
plt.title("Grafo Original")
plt.show()


# Visualizar el árbol parcial mínimo

nx.draw_networkx(T, pos, with_labels=True)
labels = nx.get_edge_attributes(T, 'weight')
nx.draw_networkx_edge_labels(T, pos, edge_labels=labels)
plt.title("Árbol Parcial Mínimo")

plt.show()

#Arbol de expancion maxima
nx.draw_networkx(Maxima, pos, with_labels=True)
labels = nx.get_edge_attributes(Maxima, 'weight')
nx.draw_networkx_edge_labels(Maxima, pos, edge_labels=labels)
plt.title("Árbol Parcial Maxima")
plt.show()