from util import utils
import math
import random

class Perceptron(object):
    '''
    Basic implementation of a one-layer neural network (perceptron)
    '''
    useStepFunction = False  #basic behavior uses sigmoid 
    learningRate = 0.1
    t_sessions = 200    #max number of training session for learning
    threshold = 0.5
    bias = 0.0

    def __init__(self, numInputs):
        self.numInputs = numInputs
        self.weights = [random.uniform(-0.05, 0.05)] * numInputs #??best values
        #self.weights = [0.0] * numInputs 
        
    def learn(self, t_model):
        #check model validity
        for t_inputs, t_outputs in t_model:
            if len(t_inputs) != self.numInputs:
                raise Exception("t_model, wrong number of inputs")
        
        for _ in range(self.t_sessions):
            errorCount = 0
            #print(self.getError(t_model))
            for t_inputs, t_outputs in t_model:
                #outputs treated as list for reuse of t_models
                error = t_outputs[0] - self.getOutput(t_inputs)
                if error != 0:                    
                    errorCount += 1
                    self.bias += self.learningRate * error #??lr required
                    for i, t_input in enumerate(t_inputs):
                        self.weights[i] += self.learningRate * error * t_input
            if errorCount == 0:
                break

    def getOutput(self, inputs):
        if len(inputs) != self.numInputs:
            raise Exception("Wrong number of inputs")
        
        y = utils.dotProduct(inputs + [1], self.weights + [self.bias])
        if self.useStepFunction:
            return y > self.threshold
        else:
            return utils.sigmoid(y) 
        
    def getError(self, t_model):
        g_error = 0
        for t_inputs, t_outputs in t_model:
            l_error = t_outputs[0] - self.getOutput(t_inputs)
            g_error += math.pow(l_error, 2)
        return (g_error)/2
        
        