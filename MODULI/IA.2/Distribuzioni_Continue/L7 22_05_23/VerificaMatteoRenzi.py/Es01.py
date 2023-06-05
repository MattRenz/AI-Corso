# Un'urna è composta da 10 palline bianche, 20 palline rosse,
# 30 palline azzurre e 38 palline gialle. In 4 estrazioni,
# rimettendo ogni volta la pallina estratta, calcolare:

# - la probabilità di estrarre 2 palline gialle e 2 azzurre
# - la probabilità di estrarre almeno 3 palline gialle
# - la probabilità che, dato che almeno una pallina è gialla, 
#   ve ne siano almeno 2 di colore diverso

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

urna = [10,20,30,38]
#              0        1          2        3
labels = ["bianche", "rosse", "azzurre", "gialle"]

numProve = 1000000

Succ1 = 0 # 2 gialle 2 azzurre
Succ2 = 0 # 3 Palline gialle
Succ3 = 0 # Almeno 2 di colore diverso considerando che una è gialla


for i in range(numProve):

 
    estrazione1 = ProceduraEstraiUrna(urna)
    estrazione2 = ProceduraEstraiUrna(urna)
    estrazione3 = ProceduraEstraiUrna(urna)
    estrazione4 = ProceduraEstraiUrna(urna) 

    # PROB 1
   
    # due gialle due azzurre
    if estrazione1 == 3 and estrazione2 == 3 and estrazione3 == 2 and estrazione4 == 2:

        Succ1 +=1
    
    # due azzurrre due gialle
    elif estrazione1 == 2 and estrazione2 == 2 and estrazione3 == 3 and estrazione4 == 3:

        Succ1 +=1

    # una azzurra una gialla (X2)
    elif estrazione1 == 2 and estrazione2 == 3 and estrazione3 == 2 and estrazione4 == 3:

        Succ1 +=1

    # una gialla una azzurra (X2)
    elif estrazione1 == 3 and estrazione2 == 2 and estrazione3 == 3 and estrazione4 == 2:

        Succ1 +=1


    # PROB 2 

    # 3 iniziali gialle (escluoso l'ultimo)
    if estrazione1 == 3 and estrazione2 == 3 and estrazione3 == 3:

        Succ2 +=1

    # 3 finali gialle (escluso il primo)
    elif estrazione2 == 3 and estrazione3 == 3 and estrazione4 == 3 :

        Succ2 +=1  

    # (escluso 2)
    elif estrazione1 == 3 and estrazione3 == 3 and estrazione4 == 3 :

        Succ2 +=1  

    # (escluso 3)
    elif estrazione1 == 3 and estrazione2 == 3 and estrazione4 == 3 :

        Succ2 +=1  

    # tutte giale
    elif estrazione1 == 3 and estrazione2 == 3 and estrazione3 == 3 and estrazione4 == 3:
        Succ2 +=1


    # PROB 3

    # almeno una pallina gialla
    if estrazione1 == 3 or estrazione2 == 3 or estrazione3 == 3 or estrazione4 == 3:

                                                                                                                                        
        # 1 != 2
        # 1 != 3
        # 1 != 4
        # 2 != 1
        # 2 != 3
        # 2 != 4
        # 3 != 1
        # 3 != 2
        # 3 != 4
        # 4 != 1
        # 4 != 2
        # 4 != 3
       
        if estrazione1 != estrazione2 or estrazione1 != estrazione3 or estrazione1 != estrazione4 or estrazione2 != estrazione1 or estrazione2 != estrazione3 or estrazione2 != estrazione4 or estrazione3 != estrazione1 or estrazione3 != estrazione2 or estrazione3 != estrazione4 or estrazione4 != estrazione1 or estrazione4 != estrazione2 or estrazione4 != estrazione3:

            Succ3 +=1



probSucc1 = Succ1 / numProve # <0.056243>
probSucc2 = Succ2 / numProve # <0.256114>
probSucc3 = Succ3 / numProve # <0.837124>

print(probSucc1, probSucc2, probSucc3)





    
