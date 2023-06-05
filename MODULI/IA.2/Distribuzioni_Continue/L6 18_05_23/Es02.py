from random import *
from random import seed
import numpy as np 

# Altezza media di un gruppo di 20.000 individui è distibuita normalmente 
# con media = 170cm e con deviazione standard = 10cm

# A) Qual è la probabilità che l'altezza sia compresa fra tra 155 e 180cm ?
# B) Quante persone sono alte almeno 2 metri ?
# C) Quante persone sono alte non più di 1 metro e 60cm ?


def EstraiDaUrnaNormale(fMu, fSigma):

    fRet = np.random.normal(fMu, fSigma, 1)

    return fRet



numProva = 1000000

altezzaCompresa = 0

altezzaSuperiore200 = 0

altezzaNONSUperiore160 = 0


for i in range(numProva):

    estrazione = EstraiDaUrnaNormale(170, 10)

    if estrazione < 180 and estrazione > 155:

        altezzaCompresa +=1

    if estrazione >= 200:
        
        altezzaSuperiore200 +=1

    if estrazione <= 160:

        altezzaNONSUperiore160+=1


probAltezzaCompresa = (altezzaCompresa / numProva) * 100
personeAlteAlmeno200 = (altezzaSuperiore200 / numProva)* 20000
personealtezzaNONSUperiore160 = (altezzaNONSUperiore160 / numProva)* 20000

print(f'Prob Altezza compresa tra 155 e 180: {probAltezzaCompresa} \
      \n Persone alte almeno 200cm: {personeAlteAlmeno200} \
      \n Persone altezza non superiore 160cm: {personealtezzaNONSUperiore160}')
