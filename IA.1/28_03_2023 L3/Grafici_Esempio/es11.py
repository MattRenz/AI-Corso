"""
Grafico a matrice di dispersione: Un grafico a matrice di dispersione mostra i grafici di 
dispersione a coppie di diverse caratteristiche in un set di dati, dove ogni grafico di 
dispersione rappresenta la relazione tra due caratteristiche. I grafici delle matrici di 
dispersione possono essere utilizzati per visualizzare la correlazione tra diverse 
caratteristiche, identificare eventuali outlier o cluster ed esplorare eventuali relazioni non 
lineari. Ad esempio, il codice seguente traccia una matrice di dispersione delle prime quattro 
caratteristiche del dataset Planets:
"""


import matplotlib.pyplot as plt
import seaborn as sns

planets_df = sns.load_dataset("planets")
sns.pairplot(planets_df.iloc[:, :4])
plt.show()
