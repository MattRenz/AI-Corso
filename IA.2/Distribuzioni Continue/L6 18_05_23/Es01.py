from random import *
from random import seed
import numpy as np 

# Dato un paese la grandezza media delle case 50mq, prendendo a caso una casa
# quant è la prob. che presa a caso una casa è compresa tra 30 e 60 mq


def EstraiDaUrnaNormale(fMu, fSigma):

    fRet = np.random.normal(fMu, fSigma, 1)

    return fRet


numProva = 1000000

numSuccessi = 0

for i in range(numProva):

    estrazione = EstraiDaUrnaNormale(50, 8)

    if estrazione < 60 and estrazione > 30:

        numSuccessi +=1


prob = numSuccessi / numProva



print(prob)






