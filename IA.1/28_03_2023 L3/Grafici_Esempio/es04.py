"""
Caricare il dataset Iris utilizzando la libreria Scikit-learn e tracciare una matrice di
dispersione delle caratteristiche utilizzando la libreria Seaborn.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = sns.load_dataset("iris")
sns.pairplot(iris_df, hue="species")

plt.show()
