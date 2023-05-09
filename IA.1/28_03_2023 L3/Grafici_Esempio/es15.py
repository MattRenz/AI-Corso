import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Create a random dataset of 20 samples with 3 features
np.random.seed(0)
data = np.random.rand(20, 3)

# Compute the linkage matrix using Ward's method
Z = linkage(data, 'ward')

# Plot the dendrogram
plt.figure(figsize=(10, 5))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
dendrogram(Z, leaf_rotation=90., leaf_font_size=8.)
plt.show()

"""
Simile al 13 con dti generati come nel 14
"""