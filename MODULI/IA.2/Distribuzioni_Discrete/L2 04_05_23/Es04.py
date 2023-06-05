
# Data una popolazione di 100 m,aschi e 128 femmine 
# tenendo conto che un terzo dei maschi ha scelto il liceo ed i restanti
# hannoscelto tecnico, e tenendo presente che la meta delle femmine ha scelto il liceo 
# e le restanti il tecnico, qual è la probabilità di incontrare una persona che scelto il 
# tecnico oppure una donna che ha scelto il tecnico o è una donna ?

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
        

def CalcolaProbabilita(lurna,tentativi,leventi):

    fprobabilita = 0

    for i in range(tentativi):

        iret = PorceduraEstraiUrna(lurna)

        if leventi[iret] == 1:

            fprobabilita+=1

    return fprobabilita / tentativi


m_t = 67
m_l = 33
f_t = 64
f_l = 64

urna = [m_t, m_l, f_t, f_l]

leventi = [1,0,1,1]


iret = CalcolaProbabilita(urna, 1000000, leventi)

print(iret)



