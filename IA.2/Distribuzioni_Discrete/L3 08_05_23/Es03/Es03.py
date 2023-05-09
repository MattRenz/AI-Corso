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
        



numProva = 10000007

urna1 = [450,550] 

urna1_0 = [350,100]

urna1_1 = [400,150]

labels1= ["non attaccati", "attaccati"]

notA_2009_2011 = 0


for i in range(numProva):

    estrazioneATM = PorceduraEstraiUrna(urna1_0)

    if estrazioneATM == 0:

        estrazioneATM2 = PorceduraEstraiUrna(urna1_0)

        if estrazioneATM2 == 0:

            notA_2009_2011+=1



prob_notA_2009_2011 = notA_2009_2011 / numProva

print(prob_notA_2009_2011)


