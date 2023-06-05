import matplotlib.pyplot as plt
import numpy as np

"""
Scrivete un programma Python che legga un file di testo chiamato "es03voti.txt" che 
contiene i voti degli studenti nel formato "nome, voto" (ad esempio "John Smith,25\n").
Il programma deve creare un grafico a barre che mostri il voto medio di ogni studente.
"""

file = input("Path del file: ")

with open(file, 'r') as file:
    lines = file.readlines()

voti = {}
for line in lines:
    nome, voto = line.strip().split(',')
    if nome in voti:
        voti[nome].append(int(voto))
    else:
        voti[nome] = [int(voto)]

nomes = list(voti.keys())
avg_voti = [np.mean(voti[nome]) for nome in nomes]

plt.bar(nomes, avg_voti)
plt.xlabel('Studente')
plt.ylabel('Voto medio')
plt.title('Voti medi degli studenti')
plt.show()


""" 
I dati
John Smith,27
Alice, 29
Jane Doe,29
Kathy, 30
John Smith,24
Jane Doe,30
Kathy, 22
Alice, 30
John Smith,26
Jane Doe,28
Kathy, 23
John Smith,29
Alice, 28
Jane Doe,30
Kathy, 25
John Smith,28
Jane Doe,28
Kathy, 30
Alice, 29
John Smith,29
Jane Doe,29
""" 