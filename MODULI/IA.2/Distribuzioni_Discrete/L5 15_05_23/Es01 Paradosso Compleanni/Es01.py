
from random import *
from random import seed
import matplotlib.pyplot as plt

def PorceduraEstraiUrna(lurna):

    somaPallineLista = sum(lurna) 

    numCasuale = randint(1, somaPallineLista)

    lunghezzaLista = len(lurna) 

    ipartialLen = 0

    for i in range(lunghezzaLista):

        ipartialLen += lurna[i]

        if numCasuale <= ipartialLen:

            return i
        

def Grafico(x,y, titolo, lListaEtichette, sColor):
    
    fig = plt.figure(figsize=(8,6))

    fig.add_subplot(111)

    plt.title(titolo)
    plt.xlabel(lListaEtichette[0])
    plt.ylabel(lListaEtichette[1])
    plt.scatter(x,y,color = sColor)
    plt.show()

        
# def ProceduraAnalizzaLista(lista):

#     lAppo = [0]*365

#     for i in range(len(lista)):

#         if i > 1:

#             lAppo[i] +=1

#     if max(lAppo) > 1:

#         return 1
    
#     else: 
#         return 0




# Volgiamo calcoalre la probabiliità che data un aula con 
# n persone ci siano almeno 2 persone che fanno il compleanno lo stesso giorno (giorno dell'anno)

# Se n > 365 prob. = 1.0

def Prob(numPersone):

    urna = []

    for i in range(365):
        urna.append(1)

    iNumPersone = numPersone

    numProva = 100000

    Succprob = 0

    for i in range(numProva):

        urnaRisultati = []

        for j in range(iNumPersone):

            estrazione = PorceduraEstraiUrna(urna)

            if estrazione in urnaRisultati:
                Succprob +=1
                break
            else:
                urnaRisultati.append(estrazione)

        
    return Succprob / numProva



listaPersnoe = []

for i in range(91,101):
    listaPersnoe.append(i)

yProb = []

for i in range(len(listaPersnoe)):

    prob = Prob(listaPersnoe[i])
    yProb.append(prob)


print(listaPersnoe)
print(yProb)

# x = [1,2,3,4,5,6,7,8,9,10]
# y = [4,6,7,8,9,12,13,16,19,23]

#Grafico(x,y)


# 2Probabilità 2 Persone

#sucesso2Persone = 0

# for i in range(numProva):
    

#     estrazione1 = PorceduraEstraiUrna(urna)
#     estrazione2 = PorceduraEstraiUrna(urna)

#     if estrazione1 == estrazione2:

#         sucesso2Persone +=1


# prob2Persone = sucesso2Persone / numProva

# print(prob2Persone)




