""" 
Scrivere un programma che legga un file CSV e crei un grafico a dispersione
dei dati 
"""

import matplotlib.pyplot as plt
import pandas as pd


file = input("Path del file: ")

data = pd.read_csv(file)
plt.scatter(data['x'], data['y'])
plt.show()


"""
I dati
x,y
1,2
2,4
3,6
4,8
5,10
"""