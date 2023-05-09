
import matplotlib.pyplot as plt
import csv
import sys

file = input("Path file: ")
iris = []
faetures = []

with open(file, "r") as file:
    
    reader = csv.reader(file)
    faetures = next(reader)
    items = (riga for riga in reader)

    for r in items:

        iris.append(r)


def PrendiDa1a4(l):

    return l[1:5]

def Prendi5(l):

    return l[5]

data = list(map(PrendiDa1a4, iris)) # map vuole 1 funzione 1 lista
target = list(map(Prendi5, iris))

data = list(map(lambda v: list(map(lambda x: float(x), v)), data))

print(data, target)


fig, ax = plt.subplots()
colors = ['blue', 'red', 'green']

for label, color in zip(range(len(target)), colors):
    ax.hist(data[0], 
            label=target[label],
            color=color)

ax.set_xlabel(faetures[0])
ax.legend(loc='upper right')

plt.show()
