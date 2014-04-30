import os
import math

def dotProduct(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))
    
def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))
    
def getResourcesPath():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir, 'resources'))

def readTrainModel(filePath, numOutputs = 1):
    f = open(filePath, 'r')
    res = []
    for line in f:
        sLine = list(map(float, line.strip().split(" ")))
        res.append(((sLine[:-numOutputs]), sLine[-numOutputs:]))
    return res

def readMatrix(filePath):
    f = open(filePath, 'r')
    res = []
    for line in f:
        res.append(list(map(float, line.strip().split(" "))))
    return res