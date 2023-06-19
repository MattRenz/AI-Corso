
from random import *
import numpy as np 

# distribuzione Poisson

def poisson_distribution(lam):
    return np.random.poisson(lam)


k = 1000

def Media(l):

    media = sum(l) / len(l)

    return media


unra_poisson = []

for i in range(k):

    l = []

    for i in range(k):

        Uniforme = poisson_distribution(8)

        l.append(Uniforme)


    media = Media(l)
    unra_poisson.append(media)
    l = []



import matplotlib.pyplot as plt

def plot_histogram(data, bins=10):
    plt.hist(data, bins=bins)
    plt.xlabel('Valore')
    plt.ylabel('Frequenza')
    plt.title('Istogramma')
    plt.show()


plot_histogram(unra_poisson, bins=5)


