import matplotlib.pyplot as plt

def Grafico(x,y, titolo, lListaEtichette, sColor):
    
    fig = plt.figure(figsize=(8,6))
    fig.add_subplot(111)

    plt.title(titolo)
    plt.xlabel(lListaEtichette[0])
    plt.ylabel(lListaEtichette[1])
    plt.scatter(x,y,color = sColor)
    plt.show()


import matplotlib.pyplot as plt
def Grafico(x,y):
    
    fig = plt.figure(figsize=(8,6))
    fig.add_subplot(111)

    plt.scatter(x,y)
    plt.show()

