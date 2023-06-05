# Nel 1970 i Beatles vennero a Genova in incognito e pernottarono 
# all’albergo Nicolas Bourbaki (ora distrutto per costruire 
# l’attuale dipartimento di matematica). L’albergo aveva 10 camere 
# di lusso disposte dallo stesso lato di un corridoio rettilineo 
# dell’ultimo piano. A ciascuno dei cantanti venne assegnata 
# a caso una camera: 
# qual è la probabilità che che almeno 2 di loro avessero camere contigue ? (vicine)


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
        

urna = [0,1,2,3,4,5,6,7,8,9]

numProve = 1000000

Succ = 0

for i in range(numProve):

#2 di loro avessero camere contigue ? (vicine)
 
    persona1 = ProceduraEstraiUrna(urna)
    urna.remove(urna[persona1])
    persona2 = ProceduraEstraiUrna(urna)
    urna.remove(urna[persona2])
    persona3 = ProceduraEstraiUrna(urna)
    urna.remove(urna[persona3])
    persona4 = ProceduraEstraiUrna(urna)

    # persona1 = 5    # 5+1 = 6 == OK // 5-1 = 6 == OK
    # persona2 = 6   
    # persona3 = 9
    # persona4 = 0
    


    #                   P1 V P2                                         P1 V P3                                                     P1 V P4                                     P2 V P3                                                                 P2 V P4                           P3 V P4
    if persona1 == persona2 + 1 or persona1 == persona2 -1 or persona1 == persona3+1 or persona1 == persona3-1 or persona1 == persona4+1 or persona1 == persona4-1 or persona2 == persona3+1 or persona2 == persona3-1 or persona2 == persona4+1 or persona2 == persona4-1 or persona3 == persona4+1 or persona3 == persona4-1: 
        Succ +=1

        # P1 v P2 - 
        # P2 V P1

        # P1 V P3 -
        # P3 V P1

        # P1 V P4 -
        # P4 V P1

        # P2 V P3 -
        # P3 V P2

        # P2 V P4 -
        # P4 V P2

        # P3 V P4 - 
        # P4 V P3
    
    urna = [0,1,2,3,4,5,6,7,8,9]


probSucc = Succ / numProve # <0.755858>  (prob troppo alta..)

print(probSucc)







    
    

    