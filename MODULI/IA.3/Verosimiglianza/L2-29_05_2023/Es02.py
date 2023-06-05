from random import *
from random import seed
import math
import numpy as np 

def EstraiDaUrnaNormale(fMu, fSigma):

    fRet = np.random.normal(fMu, fSigma, 1)

    return fRet

def CalcolaCodaNormale(fMu, fSigma, fXvalue):

    iNumProva = 1000000

    iCoda = 0

    if fXvalue < fMu:


        for i in range(iNumProva):

            iret = EstraiDaUrnaNormale(fMu, fSigma)

            if fXvalue < fMu:

                if iret < fXvalue:

                    iCoda+=1

            if fXvalue > fMu:

                if iret > fXvalue:

                    iCoda +=1


    return iCoda / iNumProva



# Dato un campione di 100 elementi, verifica quanto è probabile che 
# sia stato estratto da una Normale N(10, 4.6)

# 1) Se l'ipotesi è vera, allora media_campionaria N(10,0.45)

urna = [20, 30, 70]

for i in range(100):

    print(i * 100 / 100 - 100 + 100 * 10 / 10)

