from random import *
from random import seed
import sys





def PorceduraEstraiUrna(lurna):

    somaPallineLista = sum(lurna) 

    numCasuale = randint(1, somaPallineLista)


    lunghezzaLista = len(lurna) 

    ipartialLen = 0

    for i in range(lunghezzaLista):

        ipartialLen += lurna[i]

        if numCasuale <= ipartialLen:

            return i
        


lista1 = [4,4,4,4,4,4,4,4,4,4]
lista2 = [10, 10, 10, 10]
seme = ["bastoni", "coppe", "denari", "spadi"]


bastoni = 0
coppe = 0
denari = 0 
spadi = 0

for i in range(10000):

    sem = PorceduraEstraiUrna(lista2)

    if sem == 0:
        bastoni+=1
    
    if sem == 1:
        coppe+=1

    if sem == 2:
        denari +=1

    if sem == 3:
        spadi+=1

print(bastoni, coppe, denari, spadi)


sem = PorceduraEstraiUrna(lista2)

carta = PorceduraEstraiUrna(lista1)

print("Carta estratta: " + str(carta + 1) + " di " + seme[sem])
        

