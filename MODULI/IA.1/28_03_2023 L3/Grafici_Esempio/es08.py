"""
Boxplot: Un boxplot è un modo per visualizzare la distribuzione dei dati in base ai quartili. 
I boxplot possono essere utilizzati per identificare gli outlier, confrontare la distribuzione 
di diverse caratteristiche e rilevare eventuali asimmetrie o simmetrie. Ad esempio, il codice 
seguente traccia un boxplot della variabile target nel set di dati Boston Housing:
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

plt.boxplot(target)
plt.xticks([1], ["Housing Price"])
plt.ylabel("Price ($1000s)")
plt.title("Boxplot of Boston Housing Prices")
plt.show()
