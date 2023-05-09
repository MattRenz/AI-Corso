import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram


# Simulate a dataset with 10 samples and 3 features
data = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'])

# Compute the distance matrix using Euclidean distance
distance_matrix = sns.clustermap(data.corr(), method='average', metric='euclidean').dendrogram_row.linkage

# Plot the dendrogram
plt.figure(figsize=(10, 5))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
dendrogram(distance_matrix, leaf_rotation=90., leaf_font_size=8.)
plt.show()

"""
Questo programma simula innanzitutto un set di dati con 10 campioni e 3 
caratteristiche utilizzando la funzione np.random.randn() della libreria NumPy 
e lo memorizza in un DataFrame Pandas. Quindi calcola la matrice di distanza tra 
i campioni utilizzando la funzione clustermap() della libreria seaborn, con il 
metodo impostato su 'average' e la metrica su 'euclidean', che calcola la distanza 
euclidea tra i campioni.

Infine, il programma traccia il dendrogramma utilizzando la funzione dendrogram() 
del modulo scipy.cluster.hierarchy, con i parametri leaf_rotation e leaf_font_size 
impostati per personalizzare l'aspetto del grafico. Il dendrogramma risultante 
dovrebbe mostrare il raggruppamento gerarchico del set di dati simulati, con i 
campioni in basso e i cluster in alto, e la distanza tra di essi rappresentata 
dall'altezza dei rami.
"""