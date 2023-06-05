
from random import *
from random import seed
import sys

pallineblu = []
pallinerosse = []
pallineverdi = []


#  palline blu 1-10
for i in range(0,10):

    NumCasuale = randint(1,10)
    pallineblu.append(NumCasuale)

# palline rosse 11-15
for i in range(0,5):

    NumCasuale = randint(11,15)
    pallinerosse.append(NumCasuale)

# palline verdi 16-18
for i in range(0,3):

    NumCasuale = randint(16,18)
    pallineverdi.append(NumCasuale)


urna = pallineblu + pallinerosse + pallineverdi


# SCRIVERE PROCEDURA ESTRAI DA URNA
def PorceduraEstraiUrna(lurna):

    somaPallineLista = sum(lurna) 

    numCasuale = randint(1, somaPallineLista)


    lunghezzaLista = len(lurna) 

    ipartialLen = 0

    for i in range(lunghezzaLista):

        ipartialLen += lurna[i]

        if numCasuale <= ipartialLen:

            return i
        




blu = 0
rosse = 0
verdi = 0


for i in range(1000000000):

    iret = PorceduraEstraiUrna([10,5,4])

    if iret == 0:

        blu+=1

    if iret == 1:

        rosse+=1
    
    if iret == 2:

        verdi +=1


print(blu, rosse, verdi)