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
        


urna = [20,15,20,45]

# 00 - 01 - 10 - 11

numprove = 1000000


seguitoLezioni = 0
esmeSuperatoSeguendoLezioni = 0

esameNonSuperato = 0
LezioneSeguite = 0 



for i in range(numprove):

    estrazione = PorceduraEstraiUrna(urna)

    # Lezioni seguite 
    if estrazione == 2 or estrazione == 3:
        seguitoLezioni +=1
        # Esame superato 
        if estrazione == 3:
            esmeSuperatoSeguendoLezioni +=1

    # Esame non superato
    if estrazione == 0 or estrazione == 2:
        esameNonSuperato+=1
        # Lezioni seguite
        if estrazione == 2:
            LezioneSeguite +=1


probLezineSeguiTeEsameSuperato = esmeSuperatoSeguendoLezioni / seguitoLezioni

probLezioneSeguiteEsameNONSuperato = LezioneSeguite / esameNonSuperato

print(probLezineSeguiTeEsameSuperato, probLezioneSeguiteEsameNONSuperato)


import matplotlib.pyplot as plt

# 00 - 01 - 10 - 11
x = ["L0, E0", "L0, E1", "L1, E0", "L1, E1", "Prob L1, E1", "Prob L1, E0"]
y = [0.20,0.15,0.20,0.45, probLezineSeguiTeEsameSuperato, probLezioneSeguiteEsameNONSuperato]

plt.bar(x,y)
plt.show()