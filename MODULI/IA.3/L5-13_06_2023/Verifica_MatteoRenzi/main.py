from random import *
from random import seed
import random
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt



# distribuzione uniforme
def uniform_distribution(min_value, max_value):
    return random.uniform(min_value, max_value) 

# distribuzione chi_quadro
def chi_square_distribution(df):
    return np.random.chisquare(df)

# distribuzione Poisson
def poisson_distribution(lam):
    return np.random.poisson(lam)

# distribuzione normale
def EstraiDaUrnaNormale(fMu, fSigma):

    fRet = np.random.normal(fMu, fSigma, 1)

    return fRet


# curtosi
def CalcoloCurtosi(data):
    
    kurtosis_value = stats.kurtosis(data)
    return kurtosis_value

# simmetira
def CalcoloSimmetria(l):

    df = pd.DataFrame(l)

    simmetia = df[0].skew()

    return simmetia

# intervalli sqm
def CalcoloIntervalloDi_sqm(l):

    # df = pd.DataFrame(l, columns=['l'])
    # confidence_level = 0.95

    # mean = df['l'].mean()
    # standard_error = df['l'].sem()
    # degrees_of_freedom = len(df) - 1

    # confidence_interval = stats.t.interval(confidence_level, degrees_of_freedom, loc=mean, scale=standard_error)
    # return confidence_interval
  
    df = pd.DataFrame(l, columns=['medie'])
    confidence_level = 0.95

    mean = df['medie'].mean()
    standard_deviation = np.std(l)
    standard_error = standard_deviation / np.sqrt(len(l))

    degrees_of_freedom = len(l) - 1
    t_value = stats.t.ppf(confidence_level, degrees_of_freedom)

    lower_bound = mean - t_value * standard_error
    upper_bound = mean + t_value * standard_error

    return lower_bound, mean, upper_bound



k = 1000

medieNormale = []
medieUniforme = []
mediePoisson = []
mediechiQuadro = []

for i in range(k):

    l_uniforme = []
    l_poisson = []
    l_chi_quadro = []
    l_normlae = []

    for i in range(20):

        uniforme = uniform_distribution(5,12)
        poisson = poisson_distribution(8)
        chi_quadro = chi_square_distribution(4)
        normale = EstraiDaUrnaNormale(1.80, 0.75)

        l_uniforme.append(uniforme)
        l_poisson.append(poisson)
        l_chi_quadro.append(chi_quadro)
        l_normlae.append(normale)

    
    media_Uniforme = np.mean(l_uniforme)
    medieUniforme.append(media_Uniforme)

    media_poisson = np.mean(l_poisson)
    mediePoisson.append(media_poisson)

    media_chi_quado = np.mean(l_chi_quadro)
    mediechiQuadro.append(media_chi_quado)

    media_nomrlae = np.mean(l_normlae)
    medieNormale.append(media_nomrlae)



plt.hist(medieNormale, bins=10, alpha=0.5, label='Normale')
plt.hist(medieUniforme, bins=10, alpha=0.5, label='Uniforme')
plt.hist(mediePoisson, bins=10, alpha=0.5, label='Poisson')
plt.hist(mediechiQuadro, bins=10, alpha=0.5, label='ChiQuadro')

plt.xlabel('Media')
plt.ylabel('Frequenza')
plt.title('Istogramma delle medie')
plt.legend()
plt.show()

# CALCOLO CURTOSI 
print(F'Curtosi uniforme: {CalcoloCurtosi(medieUniforme)}')
print(F'Curtosi poisson: {CalcoloCurtosi(mediePoisson)}')
print(F'Curtosi chi_quadro: {CalcoloCurtosi(mediechiQuadro)}')
print(F'Curtosi normale: {CalcoloCurtosi(medieNormale)} \n \n ')

# CALOCLO SIMMETRIA
print(F'Simmetira uniforme: {CalcoloSimmetria(medieUniforme)}')
print(F'Simmetira poisson: {CalcoloSimmetria(mediePoisson)}')
print(F'Simmetira chi_quadro: {CalcoloSimmetria(mediechiQuadro)}')
print(F'Simmetira normale: {CalcoloSimmetria(medieNormale)} \n \n ')

# CALCOLO INTERVALO SQM
print(F'Intervallo sqm uniforme: {CalcoloIntervalloDi_sqm(medieUniforme)}')
print(F'Intervallo sqm poisson: {CalcoloIntervalloDi_sqm(mediePoisson)}')
print(F'Intervallo sqm chi_quadro: {CalcoloIntervalloDi_sqm(mediechiQuadro)}')
print(F'Intervallo sqm normale: {CalcoloIntervalloDi_sqm(medieNormale)}')