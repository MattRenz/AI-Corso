# Data una popolazione normale di media 10 e varianza 16 indicare approssimativamente quel 
# valore della X che lascia alla sua destra il 13% dei casi.

import numpy as np
import math

def EstraiDaUrnaNormale(fMu, fSigma):

    fRet = np.random.normal(fMu, fSigma, 1)

    return fRet


media = 10
varianza = math.sqrt(16)

numProve = 1000000

succ1 = 0
succ2 = 0
succ3 = 0
succ4 = 0

for i in range(numProve):

    estrazione = EstraiDaUrnaNormale(media, varianza)


    if estrazione >=14.50:
        succ1 +=1

    if estrazione >= 14.51:
        succ2+=1
    
    if estrazione >= 14.52:
        succ3 +=1

    if estrazione >= 14.53:
        succ4 +=1


print(succ1/numProve) # <0.13034>
print(succ2/numProve) # <0.129808>
print(succ3/numProve) # <0.129296>
print(succ4/numProve) # <0.128801>

# Compresa tra 14.51 e 14.50



