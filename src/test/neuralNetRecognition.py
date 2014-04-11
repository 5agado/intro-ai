from neural_network.neural_net import NeuralNet
from util import utils
import os

def polinomialFunction():
    net = NeuralNet(1, 2, 1)
    t_model = utils.readTrainModel(os.path.join(utils.getResourcesPath(), 'polinomial_degree1.txt'))
    net.learn(t_model)
    print(net.getOutputs([4]))
    print(net.getOutputs([10]))
    print(net.getOutputs([11]))
    print(net.getOutputs([20]))

def numberRecognition():
    net = NeuralNet(15, 2, 1)
    t_model = utils.readTrainModel(os.path.join(utils.getResourcesPath(), 'number_grids.txt'))
    net.learn(t_model)
    print(net.getOutputs([0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]))
    print(net.getOutputs([1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1]))
    print(net.getOutputs([1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1]))
    print(net.getOutputs([1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]))
    print(net.getOutputs([1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1]))
    print(net.getOutputs([1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0]))
    print(net.getOutputs([1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]))
    
#numberRecognition()
polinomialFunction()