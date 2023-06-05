"""
Questo programma genera innanzitutto un dataset casuale con 100 campioni e 2 
feature, utilizzando la funzione make_blobs() del modulo sklearn.datasets. 
Quindi calcola il grafo dei k vicini più vicini dei dati utilizzando la funzione 
kneighbors_graph() del modulo sklearn.neighbors, con n_neighbors impostato su 
5 e la modalità "distance".

Il dendrogramma risultante dovrebbe mostrare il raggruppamento gerarchico dei 
dati basato sul grafico KNN, con i campioni in basso e i cluster in alto e la 
distanza tra loro rappresentata dall'altezza dei rami.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.neighbors import kneighbors_graph
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.cluster.hierarchy import dendrogram, linkage

# Generate a random dataset with 100 samples and 2 features
X, y = make_blobs(n_samples=100, centers=8, n_features=4, random_state=42)

# Compute the k-nearest neighbors graph of the data
knn_graph = kneighbors_graph(X, n_neighbors=30, mode='distance', include_self=False)

Z = linkage(knn_graph.toarray(), 'ward')

# Plot the dendrogram
plt.figure(figsize=(10, 5))
plt.title('Hierarchical Clustering Dendrogram (KNN)')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
dendrogram(Z, leaf_rotation=90., leaf_font_size=8.)
plt.show()
