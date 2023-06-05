"""
Mappa di calore: Una heatmap è una rappresentazione grafica bidimensionale dei dati in cui i 
valori sono rappresentati da colori diversi. Le heatmap possono essere utilizzate per 
visualizzare la correlazione tra le diverse caratteristiche di un set di dati. Ad esempio, il 
codice seguente traccia una heatmap della matrice di correlazione per il set di dati Iris
"""

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = sns.load_dataset("iris")
corr = iris_df.corr(numeric_only = True)
sns.heatmap(corr, annot=True, cmap="YlGnBu")
plt.show()

