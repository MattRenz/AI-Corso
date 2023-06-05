
from random import *
import numpy as np 

# distribuzione Chi-Quadro

def chi_square_distribution(df, size):
    return np.random.chisquare(df, size)
