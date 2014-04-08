from neural_network import Perceptron
import math
class NeuralNet(object):
    '''
    A multi-layer neural network with 1 hidden layers and an output layer.
    '''
    t_session = 10000    #max number of training session for learning

    def __init__(self, numInputs, layerSize, numOutputs):
        #TODO: array of hidden layers
        self.numInputs = numInputs
        self.numOutputs = numOutputs
        self.layerSize = layerSize
        self.hiddenLayer = [Perceptron(numInputs) for _ in range(layerSize)]
        self.outputLayer = [Perceptron(layerSize) for _ in range(numOutputs)]
        
    def learn(self, trainingSet):
        for i in range(self.t_session):
            errorCount = 0
            count = 0
            g_error = 0
            for t_inputs, t_outputs in trainingSet:
                l_error = 0.0
                count += 1
                outputs = self.getOutputs(t_inputs)                
                if set(t_outputs) != set(outputs):
                    errorCount += 1
                    for j, output in enumerate(outputs):
                        l_error += t_outputs[j] - output
                    self.adjust(t_inputs, t_outputs)
                g_error += math.pow(l_error, 2) 
            if (i%100 == 0):
                print("Iteration {}: RMSE = {}".format(i, math.sqrt(g_error/count)))
            if errorCount == 0:
                print("Iteration {}, no errors".format(i))
                break
        
    '''
    Neural Net adjustment based on Back Propagation + momentum term
    '''
    def adjust(self,  t_inputs, t_outputs):
        outputs = self.getOutputs(t_inputs)
        if len(t_outputs) != self.numOutputs:
            raise Exception("wrong number of outputs")
            return
        delta_outputs = [0.0] * self.numOutputs
        delta_hidden = [0.0] * self.layerSize
        
        #get delta output
        for i, output in enumerate(outputs):
            delta_outputs[i] = (output * (1.0 - output) * (t_outputs[i] - output))
            
        #get delta hidden
        for i, hidden in enumerate(self.hiddenLayer):
            error = 0.0
            for j, output in enumerate(self.outputLayer):
                error += output.weights[i] * delta_outputs[j]
            h_output = hidden.getOutput(t_inputs)
            delta_hidden[i] = (h_output * (1.0 - h_output) * error)
        
        #update between hidden and output
        for i, output in enumerate(self.outputLayer):
            for j, hiddenLayer in enumerate(self.hiddenLayer):
                output.weights[j] += (output.learningRate * delta_outputs[i] * 
                           hiddenLayer.getOutput(t_inputs))
            output.bias += output.learningRate * delta_outputs[i] * 1.0
        
        #update between input and hidden
        for i, hidden in enumerate(self.hiddenLayer):
            for j, t_input in enumerate(t_inputs):
                hidden.weights[j] += hidden.learningRate * delta_hidden[i] * t_input
            hidden.bias += hidden.learningRate * delta_hidden[i] * 1.0
        
    def getOutputs(self, inputs):
        if len(inputs) != self.numInputs:
            raise Exception("wrong number of inputs")
            return []
        #outputs of the hidden layer
        h_outputs = [p.getOutput(inputs) for p in self.hiddenLayer]
        #final outputs 
        outputs = [p.getOutput(h_outputs) for p in self.outputLayer]
        return list(outputs)