
# Scrivere un progreamma che data un urna con 3  palline rosee 
# 5 palline gialle e 18 nere estrae 3 palline dall'urna ogni volta senza rimettere la pallina
# e stampa a schermo i colori della pallina estratta

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
        

urna = [3,5,18]

frequenza = [0,0,0]

inumProve = 3


for i in range (inumProve):

    
    inum1 = PorceduraEstraiUrna(urna)


    if inum1 == 0:

        frequenza[0] +=1
        urna[0] = urna[0] -1

    if inum1 == 1:

        frequenza[1] +=1
        urna[1] = urna[1] -1

    if inum1 == 2:

        frequenza[2] +=1
        urna[2] = urna[2] -1
        


print(f'Colori delle palline estratte: \n  \nRosse: {frequenza[0]} \
    \nGialle: {frequenza[1]} \nNere: {frequenza[2]}')

