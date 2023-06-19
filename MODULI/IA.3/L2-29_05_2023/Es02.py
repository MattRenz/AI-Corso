"""
Area della coda
"""
import numpy as np

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



lUrnaNormale = [8, 6]
iNumprove = 1000000
iSuccessi1 = 0
iSuccessi2 = 0
for i in range(iNumprove):
    fRet = EstraiDaUrnaNormale(lUrnaNormale[0], lUrnaNormale[1])
    if fRet > 16.3:
        iSuccessi1 += 1
    if fRet < 3.4:
        iSuccessi2 += 1

print("Coda a destra di 16.3: ", iSuccessi1/iNumprove)
print("Coda a sinistra di 3.4: ", iSuccessi2/iNumprove)

# Usando la procedura CalcolaCodaNormale()
print(CalcolaCodaNormale(8, 6, 16.3))
print(CalcolaCodaNormale(8, 6, 3.4))

