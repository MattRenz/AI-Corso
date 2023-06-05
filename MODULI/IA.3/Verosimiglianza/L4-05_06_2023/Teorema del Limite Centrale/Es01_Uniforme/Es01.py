
from random import *
from random import seed
import numpy as np 
import random




# distribuzione Uniforme

def uniform_distribution(min_value, max_value):
    return random.uniform(min_value, max_value) 


k = 1000

def Media(l):

    media = sum(l) / len(l)

    return media


unra_uniforme = []

for i in range(k):

    l = []

    for i in range(k):

        Uniforme = uniform_distribution(5,12)

        l.append(Uniforme)


    media = Media(l)
    unra_uniforme.append(media)
    l = []



import matplotlib.pyplot as plt

def plot_histogram(data, bins=10):
    plt.hist(data, bins=bins)
    plt.xlabel('Valore')
    plt.ylabel('Frequenza')
    plt.title('Istogramma')
    plt.show()


plot_histogram(unra_uniforme, bins=5)


