# CALCOLA LA BROPABILITA CHE LANCINADO DUE DADI 
# LA SOMMA SIA 5 
# E LA PROBABILITÀ CHE ESCANO DUE 1


from random import *
from random import seed
import prova

def PorceduraEstraiUrna(lurna):

    somaPallineLista = sum(lurna) 

    numCasuale = randint(1, somaPallineLista)


    lunghezzaLista = len(lurna) 

    ipartialLen = 0

    for i in range(lunghezzaLista):

        ipartialLen += lurna[i]

        if numCasuale <= ipartialLen:

            return i
        


def Condozione(estrazione1, estrazione2): 

    if (estrazione1 + 1) + (estrazione2 + 1) == 5:

        return 1
    
    return 0

    
urna = [1,1,1,1,1,1]

numProve = 1000000

Somma5 = 0
NumUgualiA1 = 0
DadiPARI = 0
DadiDISPARI = 0
DadiParoEDisparo = 0
DadiMinoreDi5 = 0
DdiMaggdi5 = 0

for i in range(numProve):

    estrazioneDado1 = PorceduraEstraiUrna(urna)
    estrazioneDado2 = PorceduraEstraiUrna(urna)

    if (estrazioneDado1 + 1) % 2 == 0 and (estrazioneDado2 + 1) %2 == 0:
        DadiPARI +=1

    if (estrazioneDado1 + 1) % 2 == 1 and (estrazioneDado2 + 1) %2 == 1:
            DadiDISPARI +=1

    if (estrazioneDado1 + 1) %2 == 0 and (estrazioneDado2 + 1) %2 == 1 or (estrazioneDado1 + 1) %2 == 1 and (estrazioneDado2 + 1) %2 == 0:
        DadiParoEDisparo +=1

    if (estrazioneDado1 + 1) < 5 and (estrazioneDado2 + 1) < 5:
        DadiMinoreDi5 +=1
    


    if Condozione(estrazioneDado1, estrazioneDado2) == 1:

        Somma5 +=1

    if (estrazioneDado1 + 1) == 1 and (estrazioneDado2 + 1) == 1:

        NumUgualiA1+=1


probSomma5 = Somma5 / numProve
probNumUgualiA1 = NumUgualiA1 / numProve
probDadiPARI = DadiPARI / numProve
probDadiDispari = DadiDISPARI / numProve
probDadiParoEDispari = DadiParoEDisparo / numProve
probDadiMin5 = DadiMinoreDi5 / numProve


print(f'Probabilità Dadi somma = 5: {probSomma5} \n Probabilità dadi = a 1: {probNumUgualiA1} \
      \n Probabilità dadi pari: {probDadiPARI} \n Probabilità dadi dispairi {probDadiDispari} \
      \n Probabilità dadi pari e dispari: {probDadiParoEDispari} \
      \n Probabilita dadi minori di 5: {probDadiMin5}')


import matplotlib.pyplot as plt

x = ["Prob dadi sum 5", "Prob lanci = 1", "dadi PARI", "dadi DISPARI", "Pari e Dispari", "Dadi < 5", "Probmax"]
y = [probSomma5, probNumUgualiA1, probDadiPARI, probDadiDispari, probDadiParoEDispari, probDadiMin5, 1]

prova.Grafico(x,y)

# plt.bar(x,y)
# plt.title("Probabilità lancio dadi")
# plt.show()




