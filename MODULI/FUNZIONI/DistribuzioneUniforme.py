
from random import *
from random import seed
import numpy as np 

# distribuzione Uniforme

def uniform_distribution(min_value, max_value, size):
    return [random.uniform(min_value, max_value) for _ in range(size)]
