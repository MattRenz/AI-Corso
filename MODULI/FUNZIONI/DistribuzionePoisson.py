
from random import *
import numpy as np 


# distribuzione Poisson

def poisson_distribution(lam, size):
    return np.random.poisson(lam, size)
