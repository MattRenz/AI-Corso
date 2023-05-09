"""
Caricare il dataset Wine utilizzando la libreria Scikit-learn e tracciare un
grafico di dispersione di due caratteristiche con colori diversi per ogni classe.
con colori diversi per ogni classe utilizzando la libreria Matplotlib.
"""

import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

wine = load_wine()
fig, ax = plt.subplots()
for i, target_name in enumerate(wine.target_names):
    X = wine.data[wine.target == i, :]
    ax.scatter(X[:, 0], X[:, 1], label=target_name)
ax.set_xlabel(wine.feature_names[0])
ax.set_ylabel(wine.feature_names[1])
ax.legend()
plt.show()

