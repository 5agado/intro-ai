from neural_network.perceptron import Perceptron
from neural_network.neural_net import NeuralNet
from util import utils
import os

def testPerceptron():
    p = Perceptron(2)
    p.useStepFunction = True
    t_model = utils.readTrainModel(os.path.join(utils.getResourcesPath(), 'logic_gates/XOR.txt'))
    p.learn(t_model)
    print(p.getOutput([0, 0]))
    print(p.getOutput([0, 1]))
    print(p.getOutput([1, 0]))
    print(p.getOutput([1, 1]))

def testNeuralNet():
    net = NeuralNet(2, 4, 1)
    t_model = utils.readTrainModel(os.path.join(utils.getResourcesPath(), 'logic_gates/AND.txt'))
    net.learn(t_model)
    print(net.getOutputs([0, 0]))
    print(net.getOutputs([0, 1]))
    print(net.getOutputs([1, 0]))
    print(net.getOutputs([1, 1]))
    
#testPerceptron()
testNeuralNet()