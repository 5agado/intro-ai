from pip._vendor.requests.packages.urllib3.connectionpool import xrange
from util import utils
import random

class Perceptron(object):
    '''
    Basic implementation of a one-layer neural network (perceptron)
    '''
    useStepFunction = False
    learningRate = 0.1
    t_session = 200    #max number of training session for learning
    threshold = 0.5
    '''
    For the bias there exist two different approaches: 
        1. consider it as a weight (and fixed input with value 1)
            1.1 Ask always as an input (with value 1)
            1.2 Make transparent to "user"
        2. use as the bias to compute fire function. 
            learn rule: b = b + error 
    '''
    bias = 0.0

    def __init__(self, numInputs):
        self.numInputs = numInputs
        self.weights = [random.uniform(-2.0, 2.0)] * numInputs 
        
    def learn(self, t_model):
        for _ in xrange(self.t_session):
            errorCount = 0
            for t_inputs, t_outputs in t_model:
                #print(self.weights)
                #print(self.bias)
                res = self.getOutput(t_inputs)
                error = t_outputs[0] - res
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
        bValue = value + (self.bias * 1)
        #return (value + self.bias) > self.threshold
        if self.useStepFunction:
            return bValue > self.threshold
        else:
            return utils.sigmoid(bValue)   
        
        