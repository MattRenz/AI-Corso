"""
Verifichiamo empiricamente che la media delle estrazioni da una normale
è ancora distribuita come una normale
"""
from math import sqrt
import numpy as np


def EstraiDaUrnaNormale(fMu, fSigma):
    fRet = np.random.normal(fMu, fSigma, size=1)
    return fRet

def EstraiDaMediaCampionariaNormale(fMu, sSigma, k):
    media = 0
    for i in range(k):
        fRet = EstraiDaUrnaNormale(fMu, sSigma)
        media += fRet
    return media/k

lUrnaNormale = [10, 4.5]
iNumProve = 100000
iSuccessiIntervallo1Sigma = 0
iSuccessiIntervallo2Sigma = 0
iSuccessiIntervallo3Sigma = 0
for i in range(iNumProve):
    fRet = EstraiDaUrnaNormale(lUrnaNormale[0], lUrnaNormale[1])
    if fRet >= 5.5 and fRet <= 14.5:
        iSuccessiIntervallo1Sigma += 1
    if fRet >= 1 and fRet <= 19:
        iSuccessiIntervallo2Sigma += 1
    if fRet >= -3.5 and fRet <= 23.5:
        iSuccessiIntervallo3Sigma += 1

# Verifica della normalità
# print("Intervallo di sigma", iSuccessiIntervallo1Sigma/iNumProve)
# print("Intervallo di due sigma", iSuccessiIntervallo2Sigma/iNumProve)
# print("Intervallo di tre sigma", iSuccessiIntervallo3Sigma/iNumProve)

k = 6
sSigma = 4.5
iSuccessi1NewSigma = 0
iSuccessi2NewSigma = 0
iSuccessi3NewSigma = 0
for i in range(iNumProve):
    variabile = EstraiDaMediaCampionariaNormale(lUrnaNormale[0], lUrnaNormale[1], k)
    if variabile >= 10 - (sSigma/sqrt(k)) and variabile <= 10 + (sSigma/sqrt(k)):
        iSuccessi1NewSigma += 1
    if variabile >= 10 - 2*(sSigma/sqrt(k)) and variabile <= 10 + 2*(sSigma/sqrt(k)):
        iSuccessi2NewSigma += 1
    if variabile >= 10 - 3*(sSigma/sqrt(k)) and variabile <= 10 + 3*(sSigma/sqrt(k)):
        iSuccessi3NewSigma += 1

print(iSuccessi1NewSigma/iNumProve)
print(iSuccessi2NewSigma/iNumProve)
print(iSuccessi3NewSigma/iNumProve)

