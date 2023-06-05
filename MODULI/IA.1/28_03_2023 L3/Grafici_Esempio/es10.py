"""
Grafico a violino: Un violin plot è una combinazione di boxplot e density plot, dove il box 
rappresenta l'intervallo interquartile e il density plot mostra la distribuzione dei dati. I 
violin plot possono essere utilizzati per confrontare la distribuzione di diverse 
caratteristiche o classi in un set di dati. Ad esempio, il codice seguente traccia un violin 
plot della lunghezza dei sepali per ogni specie nel set di dati Iris:
"""

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = sns.load_dataset("iris")
sns.violinplot(x="species", y="sepal_length", data=iris_df)
plt.show()