"""
Preso il file contare quante parole diverse ci sono
e graficizzare il risultato, che mostra per ogni parola la sua 
frequenza nel testo.

1) C'è differenza tra maiuscolo e minuscolo ? 
2) E i numeri ?
3) Ho bisogno di un dizionario ?
4) Quali sono le parole più importatni ?

"""

import matplotlib.pyplot as plt
import re

file = input("Path del file: ")

with open(file, 'r') as file:
    lines = file.readlines()

paroleCont = {}
paroleCont = list(paroleCont)

numeri = {}
numeri = list(numeri)


for line in lines:

    newLinee = line.strip()

    parole = re.split("[\x00-\x2F]|[\x3A-\x40]|[\x5B-\x60]|[\x7B-\xFF]|[\u0100-\uffff]", newLinee)

    for singpar in parole:

        if singpar == '':

            parole.remove(singpar)


    for singParola in parole:
        
        singParola = singParola.lower()

        paroleCont.append(singParola)

        if singParola == '':

            paroleCont.remove(singParola)
            

paroleUniche = {}

for parola in paroleCont:

    if parola in paroleUniche:
        paroleUniche[parola] += 1

    else:

        paroleUniche[parola] = 1

print(len(paroleUniche))




print(set(paroleCont))

print(len(set(paroleCont)))

# print(set(numeri))


            
parole = list(paroleUniche.keys())
conta = [paroleUniche[parola] for parola in parole]

plt.bar(parole[:30], conta[:30])
plt.xlabel('parole')
plt.ylabel('conta')
plt.title('frequenza parole in holmes.txt')
plt.show()
