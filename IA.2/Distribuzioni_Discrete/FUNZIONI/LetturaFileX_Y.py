import pandas 
from pandas import DataFrame

def ReturnX_prob(filePath):

    file = pandas.read_csv(filePath, sep=",")

    x = list(file['x'])

    return x

def ReturnY_prob(filePath):

    file = pandas.read_csv(filePath, sep=",")

    x = list(file['y'])

    return x

