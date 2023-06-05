# In un'urna ci sono 8 palline blu e 5 bianche. Estraggo una pallina: se è
# blu estraggo l'altezza di una persona da una popolazione normale
# con media 170 e scarto quadratico medio 6.5. Se esce una pallina 
# bianca estraggo da una normale con media 180 e varianza 36. 
# Qual'è la probabilità di estrarre una persona più alta di 2 metri?

from random import *
from random import seed
import math
import numpy as np 

def EstraiDaUrnaNormale(fMu, fSigma):

    fRet = np.random.normal(fMu, fSigma, 1)

    return fRet


def ProceduraEstraiUrna(lurna):

    somaPallineLista = sum(lurna) 

    numCasuale = randint(1, somaPallineLista)

    lunghezzaLista = len(lurna) 

    ipartialLen = 0

    for i in range(lunghezzaLista):

        ipartialLen += lurna[i]

        if numCasuale <= ipartialLen:

            return i
        

urna = [8,5]
labels = ["blu", "bianche"]
numProve = 1000000
succ = 0
succBianca = 0

mediaBlue = 170
sigmaBlue = 6.5

mediaBianca = 180
sigmaBianca = math.sqrt(36)


for i in range(numProve):

    estrazione = ProceduraEstraiUrna(urna)
    
    # blue
    if estrazione == 0:
        
        estrazioneH = EstraiDaUrnaNormale(mediaBlue, sigmaBlue)

    # bianca
    if estrazione == 1:

        estrazioneH = EstraiDaUrnaNormale(mediaBianca, sigmaBianca)

        
    if estrazioneH > 200:
        succ +=1
        

print((succ / numProve))




        

        






    





