# 1) Si considerino due urne: la prima contenente 2 palline rosse e 8 verdi e la seconda contenente 4 palline rosse e 6 verdi.
# a) Si consideri un esperimento che consiste nell’estrarre con ripetizione
# due palline dalla prima urna e si determini la probabilità che entrambe
# le palline siano rosse.
# b) Si consideri l’esperimento che consiste nell’estrarre una pallina dalla
# prima urna, nell’inserirla nella seconda urna e nell’estrarre una pallina dalla seconda urna. Determinare la probabilità che la pallina estratta sia rossa.
# c) Sapendo che la pallina estratta dalla seconda urna è rossa, calcolare la probabilità che la pallina estratta dalla prima urna sia verde.

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
        


def Condozione(estrazione1, estrazione2): 

    if estrazione1 == 0 and estrazione2 == 0:

        return 1
    
    return 0

def Condizione1(estrazone):

    if estrazone == 0:
        return 1
    
    return 0

def Condizione2(estrazione):
    
    if estrazione == 1:
        return 1
    return 0

    

urna1 = [2,8]

urna2 = [4,6]

numProva = 1000000

pallRosse = 0
pallRosseUrna2 = 0
pallVerdeUrna1RossoUrna2 = 0
inumprova1 = 0 

for i in range(numProva):

    estrazioneUrna1_1 = PorceduraEstraiUrna(urna1)
    estrazioneUrna1_2 = PorceduraEstraiUrna(urna1)

    if Condozione(estrazioneUrna1_1, estrazioneUrna1_2) == 1:

        pallRosse +=1

    if estrazioneUrna1_1 == 0:

        urna2[0] +=1

    if estrazioneUrna1_2 == 1:

        urna2[1]+=1


    estrazioneUrna2 = PorceduraEstraiUrna(urna2)

    if estrazioneUrna2 == 0:
        inumprova1 += 1
        
    if Condizione1(estrazioneUrna2) == 1:

        pallRosseUrna2 +=1



    if urna2[0] == 5:
        urna2[0] = 4

    if urna2[1] == 7:
        urna2[1] = 6

    

probRosse_urna1 = pallRosse / numProva
probRosseUrna2 = pallRosseUrna2 / numProva


print(f'Probabilità Rosse urna1: {probRosse_urna1} \
      \nProbabilità Rosse urna 2: {probRosseUrna2}')




