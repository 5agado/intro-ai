from pip._vendor.requests.packages.urllib3.connectionpool import xrange
from util import utils

class Perceptron(object):
    '''
    Basic implementation of a one-layer neural network (perceptron)
    '''
    learningRate = 0.1
    t_session = 20    #max number of training session for learning
    threshold = 0.5
    '''
    For the bias there exist two different approaches: 
        1. consider it as a weight (and fixed input with value 1)
        2. use as the bias to compute fire function. 
            learn rule: b = b + error 
    '''
    bias = 0.0

    def __init__(self, numInputs):
        self.numInputs = numInputs
        self.weights = [0.0] * numInputs
        
    def readTrainModel(self, filePath = None):
        if filePath == None:
            filePath = self.t_modelPath
        f = open(filePath, 'r')
        res = []
        for line in f:
            sLine = list(map(float, line.strip().split(" ")))
            res.append(((sLine[:-1]), sLine[-1]))
        return res 
        
    def learn(self, t_modelPath):
        self.t_modelPath = t_modelPath
        for _ in xrange(self.t_session):
            errorCount = 0
            for t_inputs, t_ouputs in self.readTrainModel():
                #print(self.weights)
                #print(self.bias)
                res = self.getOutput(t_inputs)
                error = t_ouputs - res
                if error != 0:
                    errorCount += 1
                    #self.bias += error
                    self.bias += self.learningRate * error * 1
                    for i, t_input in enumerate(t_inputs):
                        if i >= self.numInputs:
                            break
                        self.weights[i] += self.learningRate * error * t_input
            if errorCount == 0:
                break

    def getOutput(self, inputs):
        value = utils.dotProduct(inputs, self.weights)
        #return (value + self.bias) > self.threshold
        return (value + (self.bias * 1)) > self.threshold
            
        
        