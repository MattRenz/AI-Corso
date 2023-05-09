"""
Preso il file holmes.txt
1) contare quante parole diverse ci sono
2) graficizzare il risultato (un grafico a barre, o 
come volete, che mostra per ogni parola la sua 
frequenza nel testo)
"""

"""
NB:
1) Che cosa è una parola?
    - come la posso distinguere in un testo?
2) C'è differenza tra maiuscolo e minuscolo?
3) E i numeri?
4) E le righe vuote?
5) Ho bisogno di un "dizionario?"
6) quali sono le parole "più importanti"?
    - le meno frequenti?
    - le più frequenti?
"""

import re
import matplotlib.pyplot as plt
import numpy as np

linee=[]
file = input("Path file: ")
with open(file, "r") as file:
    linee=file.readlines()

## Mi sono accorto chde ci sono i fine linea
## Come li tolgo? con strip

## é più "elegante", da "hacker"
linee = [linea.strip() for linea in linee]

## è normale, da sviluppatori che conoscono 
# più linguaggi e quindi non si perdono
# a eseguire strutture sintattiche specifiche
# del linguaggio utilizzato
nuovelinee=[]
for linea in linee:
    nuovelinee.append(linea.strip())
linee=nuovelinee

#Splittiamo la linee usando la re.split
parole=[]
for linea in linee:
    #Split su tutti i caratteri che non sono 0-9, a-z e A-Z
    linea=re.split("[\x00-\x2F]|[\x3A-\x40]|[\x5B-\x60]|[\x7B-\xFF]|[\u0100-\uffff]", linea)
    parole.append(linea)

#metodo cristiano
elencoParole=[]
for listaParole in parole:
    for parola in listaParole:
        elencoParole.append(parola)

#metodo complicatino
elencoParole=[]
for listaParole in parole:
    elencoParole.extend(listaParole)

#metodo indiano
elencoParole=[parola for lista in parole for parola in lista]

#metodo hacker
elencoParole=list(filter(lambda x: x != '', elencoParole))

#Oppure, metodo cristiano esteso
elencoParole=[]
for listaParole in parole:
    for parola in listaParole:
        if len(parola) != 0 and not parola[0].isdigit():
            elencoParole.append(parola.lower())
# print(elencoParole)

paroleUniche={}
for parola in elencoParole:
    if parola in paroleUniche:
        paroleUniche[parola] += 1
    else:
        paroleUniche[parola] = 1
# print("ParoleUniche: ", paroleUniche)

parole = list(paroleUniche.keys())
conta = [paroleUniche[parola] for parola in parole]

plt.bar(parole[:30], conta[:30])
plt.xlabel('parole')
plt.ylabel('conta')
plt.title('frequenza parole in holmes.txt')
plt.show()
