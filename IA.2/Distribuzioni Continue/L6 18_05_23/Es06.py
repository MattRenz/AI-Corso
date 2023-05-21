from random import seed
from random import *
import numpy as np


def EstraiDaUrnaNormale(fMu,fSigma):
    fRet= np.random.normal(fMu,fSigma,1)
    return fRet

numProve = 1000000
NumSuccessi1 = 0
NumSuccessi2 = 0
for i in range (numProve):
    
    estrazione = EstraiDaUrnaNormale(7.6,0.9)

    if estrazione >=9.4 and estrazione <= 9.6:
        NumSuccessi1+= 1

    if estrazione >= 7.6 and estrazione <= 9.4:
        NumSuccessi2 +=1


print(NumSuccessi1/numProve)
print(NumSuccessi2/numProve)