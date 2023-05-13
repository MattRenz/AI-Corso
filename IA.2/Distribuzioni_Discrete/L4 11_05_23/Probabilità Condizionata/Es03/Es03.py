
from random import *
from random import seed


def PorceduraEstraiUrna(lurna):

    somaPallineLista = sum(lurna) 

    numCasuale = randint(1, somaPallineLista)

    lunghezzaLista = len(lurna) 

    ipartialLen = 0

    for i in range(lunghezzaLista):

        ipartialLen += lurna[i]

        if numCasuale <= ipartialLen:

            return i
        

urna = []

for i in range(365):
  urna.append(1)  

numProva = 1000000

successi10 = 0

# (y, 10)
for i in range(numProva):

    numPersone = 10

    frequenza = []
    for i in range(365):
       frequenza.append(0)

    for i in range(numPersone):

        estrazione = PorceduraEstraiUrna(urna)

        frequenza[estrazione] +=1

    iMax = max(frequenza)

    if iMax > 1:
       
       successi10 +=1
       
       
import matplotlib.pyplot as plt

prob10Persone = successi10 / numProva

x = [prob10Persone] 
for i in (100):
  x.append(i)  

y = []


plt.plot(x,y)
plt.show()