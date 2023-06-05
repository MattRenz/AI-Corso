
import FUNZIONI.ProceduraEstraiUrna as ProceduraEstraiUrna

def CalcolaProbabilita(lurna,tentativi,leventi):

    fprobabilita = 0

    for i in range(tentativi):

        iret = ProceduraEstraiUrna.PorceduraEstraiUrna(lurna)

        if leventi[iret] == 1:

            fprobabilita+=1

    return fprobabilita / tentativi
