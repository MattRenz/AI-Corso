
import matplotlib.pyplot as plt
import pandas 


def Grafico(x,y, titolo, lListaEtichette, sColor):
    
    fig = plt.figure(figsize=(8,6))

    fig.add_subplot(111)

    plt.title(titolo)
    plt.xlabel(lListaEtichette[0])
    plt.ylabel(lListaEtichette[1])
    plt.scatter(x,y,color = sColor)
    plt.show()


def ReturnX_prob(filePath):

    file = pandas.read_csv(filePath, sep=",")

    x = list(file['x'])

    return x

def ReturnY_prob(filePath):

    file = pandas.read_csv(filePath, sep=",")

    x = list(file['y'])

    return x


x = ReturnX_prob("/home/studente15/Desktop/IA/MODULI/IA.2/Distribuzioni_Discrete/L5 15_05_23/Es01 Paradosso Compleanni_versione2/prob.csv")
y = ReturnY_prob("/home/studente15/Desktop/IA/MODULI/IA.2/Distribuzioni_Discrete/L5 15_05_23/Es01 Paradosso Compleanni_versione2/prob.csv")


Grafico(x,y, "Paradosso Compleanni", ["Numero Persone", "Probabilità"], "red")


