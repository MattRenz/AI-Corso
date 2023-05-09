"""
Caricare il dataset MNIST utilizzando la libreria Scikit-learn e tracciare alcune 
immagini di esempio utilizzando la libreria libreria Matplotlib.
"""

import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digits = load_digits()
fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(6, 6))
for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap="binary")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(digits.target[i])
plt.show()
