from random import *
from random import seed
import math
import numpy as np 

def EstraiDaUrnaNormale(fMu, fSigma):

    fRet = np.random.normal(fMu, fSigma, 1)

    return fRet


def EstraiDaMediaCampionariaNormale(fMu, fsigma, k):
    
    media = 0

    for i in range(k):

        ret = EstraiDaUrnaNormale(fMu, fsigma)
        media += ret

    return media/k


numProva = 1000000

k = 5

mu = 10
sigma = 4.5

# succ1 = 0
# succ2 = 0
# succ3 = 0


# for i in range(numProva):

#     estrazione = EstraiDaUrnaNormale(mu, sigma)

#     if estrazione >= 5.5 and estrazione <= 14.5:

#         succ1+=1

#     if estrazione >= 1 and estrazione <= 19:

#         succ2+=1
    
#     if estrazione >= -3.5 and estrazione <= 23.5:

#         succ3+=1


# probSucc1 = round((succ1 / numProva) * 100, 2)
# probSucc2 = round((succ2 / numProva) * 100, 2)
# probSucc3 = round((succ3 / numProva) * 100, 2)


# print(probSucc1, probSucc2, probSucc3)

iret = EstraiDaMediaCampionariaNormale(mu,sigma,k)




mu_media = mu

sigma_media = sigma/ math.sqrt(k)


succ1 = 0
succ2 = 0
succ3 = 0

for i in range(numProva):

    estrazione = EstraiDaUrnaNormale(mu_media, sigma_media)

    if estrazione >= (mu_media-sigma_media) and estrazione <= (mu_media + sigma_media):

        succ1+=1

    if estrazione >= (mu_media-(sigma_media*2)) and estrazione <= (mu_media+(sigma_media*2)):

        succ2+=1
    
    if estrazione >= (mu_media-(sigma_media*3)) and estrazione <= (mu_media+(sigma_media*3)):

        succ3+=1


probSucc1 = round((succ1 / numProva) * 100, 2)
probSucc2 = round((succ2 / numProva) * 100, 2)
probSucc3 = round((succ3 / numProva) * 100, 2)


print(probSucc1, probSucc2, probSucc3)



    
