# 5 Carte da un mazzo e mi sono venute 3 carte dispari Mi chiedo:

# carte napoletane o da poker ? 

# 1 a 10 napoletane

# 1 a 13 poker

from random import *
from random import seed
import matplotlib.pyplot as plt
import math
import scipy

def PorceduraEstraiUrna(lurna):

    somaPallineLista = sum(lurna) 

    numCasuale = randint(1, somaPallineLista)

    lunghezzaLista = len(lurna) 

    ipartialLen = 0

    for i in range(lunghezzaLista):

        ipartialLen += lurna[i]

        if numCasuale <= ipartialLen:

            return i
        

def Grafico(x,y):
    
    fig = plt.figure(figsize=(8,6))
    fig.add_subplot(111)


    plt.bar(x,y)
    plt.title("maxLikehood 3 Carte dispari")
    plt.show()


def CalcolaEntropia(lProb):

    entropia = scipy.stats.entropy(lProb)

    max_entropia = math.log(len(lProb))

    entropia_relativa = entropia / max_entropia

    print("\n Entropia: " + str(entropia)+ "\n ENtropia relativa: " + str(entropia_relativa))


        

numProve = 1000000

numSucc1 = 0
numSucc2 = 0

urna1 = []
urna2 = []

urna0 = [0,0]

urnaRis = []

for i in range(40):
    urna1.append(1)
for i in range(52):
    urna2.append(1)


maxLikehood = [2,3]


for i in range(numProve):

    for i in range(5):

        estrazione = PorceduraEstraiUrna(urna1)

        if estrazione %2 == 0:

            urna0[0] +=1

        if estrazione %2 != 0:

            urna0[1] +=1

    urnaRis.append(urna0)
    urna0 = [0,0]   


for i in range(len(urnaRis)):

    if urnaRis[i] == maxLikehood:

        numSucc1 +=1


urnaRis = []
urna0 = [0,0]  

for i in range(numProve):

    for i in range(5):

        estrazione = PorceduraEstraiUrna(urna2)

        if estrazione %2 == 0:

            urna0[0] +=1

        if estrazione %2 != 0:

            urna0[1] +=1

    urnaRis.append(urna0)
    urna0 = [0,0]   


for i in range(len(urnaRis)):

    if urnaRis[i] == maxLikehood:

        numSucc2 +=1

    


y = [numSucc1 / numProve, numSucc2 / numProve]
x = ["Carte Napoletane", "Carte Poker"]

# Grafico 
Grafico(x,y)


# Prob massima verosomiglianza
print(numSucc1 / numProve) # 0.312329
print(numSucc2 / numProve) # 0.311712

probmaxLikehood = max(y)

print(f'\n Massima verosomiglianza: {probmaxLikehood}') # Massima verosomiglianza: 0.029928


# Prob. Urne
numSucc1 = (numSucc1 / numProve) * numProve 
numSucc2 = (numSucc2 / numProve) * numProve

l = [numSucc1, numSucc2]

Sum = sum(l)

probUrna1 = numSucc1 / Sum

probUrna2 = numSucc2 / Sum

print("\n Prob Urna1: ", probUrna1) # 0.5004943585437496
print("\n Prob Urna2: ", probUrna2) # 0.4995056414562505

print("\n Somma prob. ", probUrna1 + probUrna2)


#calcolo Entropia

lProb = [probUrna1,probUrna2]

CalcolaEntropia(lProb) # Entropia: 0.6931466917791261 // Etropia relativa: 0.9999992948383362




