from random import *
from random import seed
import numpy as np 


def EstraiDaUrnaNormale(fMu, fSigma):

    fRet = np.random.normal(fMu, fSigma, 1)

    return fRet



numProva = 1000000

succ1 = 0

succ2 = 0
succ3 = 0
succ4 = 0
succ5 = 0
succ6 = 0
succ7 = 0

for i in range(numProva):

    estrazione = EstraiDaUrnaNormale(3.2, 0.6)

    if estrazione > 2.2 and estrazione < 3.5:

        succ1 +=1

    if estrazione >= 3.8:
        succ2 +=1

    if estrazione >= 3.9:
        succ3+=1

    if estrazione >= 4.0:
        succ4+=1

    if estrazione >= 4.1:
        succ5+=1

    if estrazione >= 4.2:
        succ6+=1

    if estrazione >= 4.3:
        succ7+=1





probSucc1 =  round((succ1 / numProva) * 100, 2)

print(f'Prob: {probSucc1}%')

print(succ2 / numProva)
print(succ3 / numProva)
print(succ4 / numProva)
print(succ5 / numProva)
print(succ6 / numProva)
print(succ7 / numProva)