from random import *
from random import seed
import numpy as np 

# Ad un esame universitario il voto medio è 24 con sigma = 4

# Clcolare la probabilità che uno studente abbia riportato un voto:

# > 27 // <= 22


def EstraiDaUrnaNormale(fMu, fSigma):

    fRet = np.random.normal(fMu, fSigma, 1)

    return fRet



numProva = 1000000

probVotosup27 = 0
probVotoNONinf22 = 0


for i in range(numProva):

    estrazione = EstraiDaUrnaNormale(24, 4)

    if estrazione > 27:

        probVotosup27 +=1

    if estrazione >=22:
        
        probVotoNONinf22 +=1


probVotoSup27 =  round((probVotosup27 / numProva) * 100, 2)
probVotoNONinf22 = round((probVotoNONinf22 / numProva) * 100, 3)
print(f'Pro voto superiore a 27: {probVotoSup27}% \
      \n Prov voto non inferiore a 22: {probVotoNONinf22}%')

