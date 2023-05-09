#
# Data un urnacon 3 palline rosse 5 palline gialle e 18 palline nere calcolare 
# la probabilità di estrarre una pallina gialla

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

    if inum1 == 1:

        frequenza[1] +=1

    if inum1 == 2:

        frequenza[2] +=1


# scrivere provedura calciola probabilità che ritorna una probabilità


eventi = [0,1,0]


def CalcolaProbabilita(lurna,tentativi,leventi):

    fprobabilita = 0

    for i in range(tentativi):

        iret = PorceduraEstraiUrna(lurna)

        if leventi[iret] == 1:

            fprobabilita+=1

    return fprobabilita / tentativi


iret = CalcolaProbabilita(urna,inumProve,eventi)

print(iret)


