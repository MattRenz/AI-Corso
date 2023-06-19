"""
MEDIA CAMPIONARIA
"""
from math import sqrt

import numpy as np
from random import*

def EstraiDaUrna(lUrna):
    #conta le palline dell'urna
    SommaElementiLista = sum(lUrna)
    #genera un intero da 1 a SommaElementiLista
    iRand = randint(1, SommaElementiLista)
    #print("Numero: ", iRand)
    #ciclo for da 1 a SommaElementiLista
    #ciclo for per la dimensione della lista
    iPartialLen = 0
    for i in range(len(lUrna)):
        iPartialLen += lUrna[i]
        if iRand <= iPartialLen:
            #print("Classe: ", i)
            return i

def EstraiDaUrnaNormale(fMu, fSigma):
    fRet = np.random.normal(fMu, fSigma, size=1)
    return fRet

def CalcolaCodaNormale(fMu, fSigma, fXvalue):
    #più è vicino a 0.5 e più è tipico, più è lontano da 0.5 più è atipico
    #misura quanto un valore è tipico rispetto ad una popolazione
    iNumprove = 1000000
    iCoda = 0
    if fXvalue < fMu:
        for i in range(iNumprove):
            ret = EstraiDaUrnaNormale(fMu, fSigma)
            if ret < fXvalue:
                iCoda += 1
    elif fXvalue > fMu:
        for i in range(iNumprove):
            ret = EstraiDaUrnaNormale(fMu, fSigma)
            if ret > fXvalue:
                iCoda += 1
    return iCoda/iNumprove

# for i in range(100):
#     num = randint(0, 100)
#
#
# lUrnaPedine = [5, 8, 11, 13, 16]
# lFrequenze = [12, 31, 55, 28, 7]
#
# iCampione = 100
# media = 0
# for i in range(iCampione):
#     variabile = EstraiDaUrna(lUrnaPedine)
#     media += lFrequenze[variabile]
# x_media = media/iCampione
# print(x_media)
#
# print(CalcolaCodaNormale(10, 0.45, x_media))

Mu = 10
sigma = 4.5
alpha = 0.1
iCampione = 100

#genero un campione di 100 elementi (una lista di 100 elementi)
lUrna = [12, 30, 50, 27, 10]
lEtichette = [6, 8, 10, 12, 14]
media_campionaria = 0
for i in range(100):
    ret = EstraiDaUrna(lUrna)
    media_campionaria += lEtichette[ret]

#calcola la media sui 100 elementi
media_campionaria = media_campionaria/100

#richiama CalcolaCodaNormale
ret = CalcolaCodaNormale(Mu, sigma/sqrt(iCampione), media_campionaria)
if ret < alpha/2:
    print("Ipotesi rifiutata; cioè il campione non proviene dalla normale")
else:
    print("Ipotesi corretta")