""" GESTIONE FILE
Programma python che conta le rige di un file
e gli attributi presenti nella prma riga
"""

import csv

def ContaAttributi(file):

    with open(file, "r") as file:

        reader = csv.reader(file)

        primariga = next(reader)

        return primariga
    

def ProgrammaContaRigheFile(file):

    with open(file, "r") as file:

        linea = file.readlines()

        lRigheFile = len(linea)

    return lRigheFile



# inserire il path del file iris.csv
file = input("Path: ")


rispRighe = ProgrammaContaRigheFile(file)
risAtt = ContaAttributi(file)

att = 1
for i in risAtt:
    att+=1
print(f'\n Nm attributi: {att})')


print(f'\n Nm Righe file: {rispRighe}')

            



            

