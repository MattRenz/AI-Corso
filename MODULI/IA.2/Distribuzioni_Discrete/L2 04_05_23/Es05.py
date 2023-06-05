# In un urna ci sono 3 palline bianche e 2 nere 
# Calcolare la probabilità che in due estrazioni 
#  
# Calclare la probabilità;: 
# - escanod ude palline ner
# - escano due palline bianche 
# - escano le palline di diverso colore


from random import *
from random import seed

def PorceduraEstraiUrna(lurna):

    somaPallineLista = sum(lurna) 

    numCasuale = randint(1, somaPallineLista)


    lunghezzaLista = len(lurna) 

    ipartialLen = 0

    for i in range(lunghezzaLista):

        ipartialLen += lurna[i]

        if numCasuale <= ipartialLen:

            return i
        

urna = [3,2]
numProve = 1000000

duePnere = 0
duePbianche = 0
duePdiverse = 0

for i in range(numProve):

    estrazione1 = PorceduraEstraiUrna(urna)
    estrazione2 = PorceduraEstraiUrna(urna)


    if estrazione1 == 1 and estrazione1 == 1:

        duePnere+=1

    if estrazione1 == 0 and estrazione1 == 0:
        
        duePbianche+=1

    if estrazione1 != estrazione2:

        duePdiverse+=1


# DATA UN UN URNA CHE CONTIENE 90 PALLINE NUMERATE DA 1 A 90
# SI ESTRAGGONO 2 PALLINE 
# CALCOLARE LA PROBABILITA DI:
# - DUE NUMERI DISPARI
# - UN NUMERO DIVISIBILE PER 5 E UNO NON DIVISIBILE PER 5
# - DUE NUMERI DI QUI LA SOMMA E 50


lnumurna = []

for i in range(90):

    lnumurna.append(1)


dueNUmeriDispari = 0
DivNonDiv5 = 0
Somma50 = 0

for i in range(numProve):

    estrazione1 = PorceduraEstraiUrna(lnumurna)
    estrazione2 = PorceduraEstraiUrna(lnumurna)
    

    if estrazione1 % 2 == 1  and estrazione2 % 2 == 1:
        dueNUmeriDispari +=1
    
    if estrazione1 % 5 == 0 and estrazione2 % 5 != 0 or  estrazione1 % 5 != 0 and estrazione2 % 5 == 0:
        DivNonDiv5 +=1

    if estrazione1 + estrazione2 == 50 or estrazione2 + estrazione1 == 50:
        Somma50 +=1

    
probNumDisp = dueNUmeriDispari / numProve
probDivNonDiv5 = DivNonDiv5 / numProve
probSomma50 = Somma50 / numProve

print(probNumDisp + probSomma50 + probDivNonDiv5)


print(f'Probabilità estrazione due numeri dispari: {probNumDisp} \nProbabilità estrazione numero divisibile e non divisibile per 5: {probDivNonDiv5} \
      \nProbabilità somma 50: {probSomma50}')


import matplotlib.pyplot as plt


x = ["ProbNumDis", "ProbDivNonDiv", "ProbSOm50", "Probmx"]
y = [probNumDisp,probDivNonDiv5, probSomma50, 1]

plt.bar(x,y)
plt.title("Probabilità estrazione numeri")
plt.show()





    






