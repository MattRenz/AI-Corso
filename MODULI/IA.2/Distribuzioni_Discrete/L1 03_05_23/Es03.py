
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
        


urna = [3,2]
listafrequenze = [0,0,0] # eventi

inumProve = 1000000

for i in range (inumProve):

    inum1 = PorceduraEstraiUrna(urna)
    inum2 = PorceduraEstraiUrna(urna)

    if inum1 == 1 and inum2 == 1:

        listafrequenze[0] +=1

    if inum1 == 0 and inum2 == 0:

        listafrequenze[1] +=1

    if inum1 == 0 and inum2 == 1 or inum1 == 1 and inum2 == 0:

        listafrequenze[2] +=1



print(f'Escano due palline nere: {listafrequenze[0]} \nEscano due palline binache: {listafrequenze[1]} \nEscano due palline di diverso colore: {listafrequenze[2]}')
    







