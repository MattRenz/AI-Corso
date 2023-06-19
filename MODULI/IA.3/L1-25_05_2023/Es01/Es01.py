from random import *
from random import seed
import matplotlib.pyplot as plt
import scipy
import math


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
    plt.title("maxLikehood [6,8,5]")
    plt.show()



urna1 = [20,32,12]
urna2 = [32,32,32]
urna3 = [20,20,21]

numProve = 1000000

maxLikehood = [6,8,5]

succUrna1 = 0
succUrna2 = 0
succUrna3 = 0


urna0 = [0,0,0]
risUrne = []


# PROB 1

for i in range(numProve):

    for i in range(sum(maxLikehood)):

        estrazione = PorceduraEstraiUrna(urna1)

        if estrazione == 0:
            urna0[estrazione]+=1
        if estrazione == 1:
            urna0[estrazione]+=1
        if estrazione == 2:
            urna0[estrazione]+=1
        
    risUrne.append(urna0)
    urna0 = [0,0,0]


for i in range(len(risUrne)):

    if risUrne[i] == maxLikehood:

        succUrna1 +=1


urna0 = [0,0,0]
risUrne = []

# PROB 2

for i in range(numProve):

    for i in range(sum(maxLikehood)):

        estrazione = PorceduraEstraiUrna(urna2)

        if estrazione == 0:
            urna0[estrazione]+=1
        if estrazione == 1:
            urna0[estrazione]+=1
        if estrazione == 2:
            urna0[estrazione]+=1
        
    risUrne.append(urna0)
    urna0 = [0,0,0]

for i in range(len(risUrne)):

    if risUrne[i] == maxLikehood:

        succUrna2 +=1


urna0 = [0,0,0]
risUrne = []

# PROB 3

for i in range(numProve):

    for i in range(sum(maxLikehood)):

        estrazione = PorceduraEstraiUrna(urna3)

        if estrazione == 0:
            urna0[estrazione]+=1
        if estrazione == 1:
            urna0[estrazione]+=1
        if estrazione == 2:
            urna0[estrazione]+=1
        
    risUrne.append(urna0)
    urna0 = [0,0,0]


for i in range(len(risUrne)):

    if risUrne[i] == maxLikehood:

        succUrna3 +=1


# prob1 = 0.029387 / numProve
# prob2 = 0.029866 / numProve
# prob3 = 0.028062 / numProve

y = [succUrna1 / numProve, succUrna2 / numProve, succUrna3 / numProve]
x = ["[20,32,12]", "[32,32,32]", "[20,20,21]"]

# Grafico 
Grafico(x,y)


# Prob massima verosomiglianza
print(succUrna1 / numProve) # 0.029387
print(succUrna2 / numProve) # 0.029866
print(succUrna3 / numProve) # 0.028062

probmaxLikehood = max(y)

print(f'Massima verosomiglianza: {probmaxLikehood}') # Massima verosomiglianza: 0.029928


# Probabilità

numSucc1 = 0.029387 * 1000000

numSucc2 = 0.029866 * 1000000

numSucc3 = 0.028062 * 1000000

l = [numSucc1, numSucc2, numSucc3]

Sum = sum(l)

probUrna1 = numSucc1 / Sum

probUrna2 = numSucc2 / Sum

probUrna3 = numSucc3 / Sum

print("\n Prob Urna1: ", probUrna1)
print("\n Prob Urna2: ", probUrna2)
print("\n Prob Urna3: ", probUrna3)

print("\n Somma prob. ", probUrna1 + probUrna2 + probUrna3)


lProb = [probUrna1, probUrna2, probUrna3]
entropia = scipy.stats.entropy(lProb)

max_entropia = math.log(len(lProb))

entropia_relativa = entropia / max_entropia

print("\n Entropia: " + str(entropia)+ " relativa: " + str(entropia_relativa))











    






    

            





