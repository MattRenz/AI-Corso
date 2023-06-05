"""
Un dendrogramma è un diagramma che mostra la relazione gerarchica tra oggetti, 
gruppi o cluster. È comunemente usato nell'analisi dei dati, nel clustering e 
nella classificazione per rappresentare visivamente le somiglianze e le differenze
tra gli elementi.

Per creare un dendrogramma, è necessario eseguire un'analisi di clustering 
gerarchico sui dati. Ciò comporta il raggruppamento degli oggetti in base 
alla loro somiglianza o dissimilarità e la successiva fusione di questi gruppi 
in altri più grandi, fino a quando tutti gli oggetti si trovano in un unico cluster.

La struttura gerarchica risultante può essere rappresentata come un diagramma ad 
albero, con i singoli oggetti in basso e i cluster in alto. L'altezza di ogni 
ramo dell'albero rappresenta il grado di dissimilarità tra gli oggetti o i cluster.
"""

from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load the iris dataset
iris = load_iris()

# Perform hierarchical clustering on the iris data
Z = linkage(iris.data, 'ward') #ward, single, average, complete weighted centroid median 

# Plot the dendrogram
plt.figure(figsize=(10, 5))
plt.title('Hierarchical Clustering Dendrogram (Iris)')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
dendrogram(Z, leaf_rotation=90., leaf_font_size=8.)
plt.show()

"""
Questo programma carica innanzitutto il set di dati del fiore iris utilizzando la 
funzione load_iris() del modulo sklearn.datasets. Quindi esegue un clustering 
gerarchico sui dati utilizzando la funzione linkage() del modulo 
scipy.cluster.hierarchy, con il metodo impostato su "ward", che minimizza la
varianza delle distanze tra i cluster.

Infine, il programma traccia il dendrogramma usando la funzione dendrogram()
dello stesso modulo, con i parametri leaf_rotation e leaf_font_size impostati per 
personalizzare l'aspetto del grafico. Il dendrogramma risultante dovrebbe mostrare il 
raggruppamento gerarchico del set di dati dell'iride, con i campioni in basso e i 
cluster in alto, e la distanza tra di essi rappresentata dall'altezza dei rami.
"""
