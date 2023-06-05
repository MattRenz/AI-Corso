from random import *
from random import seed
import numpy as np 


# distribuzione di Gauss

def EstraiDaUrnaNormale(fMu, fSigma):

    fRet = np.random.normal(fMu, fSigma, 1)

    return fRet