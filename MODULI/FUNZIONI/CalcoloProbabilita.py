
from random import *
from random import seed

def ProceduraEstraiUrna(lurna):

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

        iret = ProceduraEstraiUrna.PorceduraEstraiUrna(lurna)

        if leventi[iret] == 1:

            fprobabilita+=1

    return fprobabilita / tentativi
