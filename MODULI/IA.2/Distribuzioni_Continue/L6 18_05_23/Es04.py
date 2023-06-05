from random import *
from random import seed
import numpy as np 

# Media = 5.7 
# Sigma = 1

# Prob che un sogg scelto a caso abbia:
# un livello < di 4.9
# un livello tra 4.9 e 6.2

# trovare valore x per cui l'area alla destra è il 40%


def EstraiDaUrnaNormale(fMu, fSigma):

    fRet = np.random.normal(fMu, fSigma, 1)

    return fRet



numProva = 1000000

livelloMindi4_9 = 0
livellCompresotra4_9__6_2 = 0

succ1 = 0
succ2 = 0
succ3 = 0
succ4 = 0
succ5 = 0
succ6 = 0
succ7 = 0
succ8 = 0
succ9 = 0

for i in range(numProva):

    estrazione = EstraiDaUrnaNormale(5.7, 1)

    # if estrazione < 4.9:

    #     livelloMindi4_9 +=1

    # if estrazione > 4.9 and estrazione < 6.2:
        
    #     livellCompresotra4_9__6_2 +=1


    if estrazione >= 5.8 :

        succ1+=1
    if estrazione >= 5.9 :

        succ2+=1
    if estrazione >= 6.0 :

        succ3+=1
    if estrazione >= 6.1 :

        succ4+=1
    if estrazione >= 6.2 :

        succ5+=1
    if estrazione >= 6.3 :

        succ6+=1
    if estrazione >= 6.4 :

        succ7+=1
    if estrazione >= 6.5 :

        succ8+=1
    if estrazione >= 6.6 :

        succ9+=1


print(succ1 / numProva)
print(succ2 / numProva)
print(succ3 / numProva)
print(succ4 / numProva)
print(succ5 / numProva)
print(succ6 / numProva)
print(succ7 / numProva)
print(succ8 / numProva)
print(succ9 / numProva)


# probLivelloMin =  round((livelloMindi4_9 / numProva) * 100, 2)
# probLIvelloCompreso = round((livellCompresotra4_9__6_2 / numProva) * 100, 2)

# print(f'Prob livello min: {probLivelloMin}% \nProb livello compreso: {probLIvelloCompreso}%')

