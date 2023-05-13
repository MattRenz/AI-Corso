import pandas as pd
import os
from numpy import dtype
from pandas import DataFrame, read_csv
import sys


pathFIle = os.getcwd() + "/MODULI/IA.2/Distribuzioni_Discrete/L4 11_05_23/Probabilità Condizionata/Es04/iris.csv"


#Passaggio parametri di input
fileCsv = input("\n Inserisci path completo file CSV: ")        
header_si_no = input("\n La prima riga è l'header(Si/No)?")
separator = input("\n Inserisci il separatore:")


labels = []
f = pathFIle

header_flag_ok = 0

# header si
if (header_si_no.lower() == 'si'):
    df = read_csv(f, sep=separator)
    labels = df.columns.tolist()
    header_flag_ok = 1

# header no
if (header_si_no.lower() == 'no'):
    df = read_csv(f, header=None, sep=separator)
    header_flag_ok = 1
    iCounter = 0
    num_cols = len(df.columns)
    
    # creazione header
    while iCounter < num_cols:
        sStringToPrint = "Inserisci label " + str(iCounter + 1)
        labels.append(input(sStringToPrint))
        iCounter = iCounter + 1
        
# controllo header
if (header_flag_ok != 1):
    print("header nel file non letto correttamente")
    sys.exit(0)

print(df.mean())

for i in range(1, len(df.columns)):

    if (df.dtypes[i] == dtype('float64')):

        mean = (df.iloc[:,i]).mean()
        print("\n La media della colonna " + str(i) + "Vale: " + str(mean))

    

#    Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
# 0   1            5.1           3.5            1.4           0.2  Iris-setosa