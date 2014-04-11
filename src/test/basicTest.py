from neural_network.perceptron import Perceptron
from neural_network.neural_net import NeuralNet
from util import utils
import os
from genetic_algorithm.population import Population

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
    net = NeuralNet(2, 2, 1)
    t_model = utils.readTrainModel(os.path.join(utils.getResourcesPath(), 'logic_gates/AND.txt'))
    net.learn(t_model)
    print(net.getOutputs([0, 0]))
    print(net.getOutputs([0, 1]))
    print(net.getOutputs([1, 0]))
    print(net.getOutputs([1, 1]))
    
def testNeuralNetWithGA():
    net = NeuralNet(2, 2, 1)
    p = Population(70, 9)
    p.randomInitPopulation(21, -200000, 200000)
    t_model = utils.readTrainModel(os.path.join(utils.getResourcesPath(), 'logic_gates/NAND.txt'))
    for _ in range(300):
        for chromo in p.chromos:
            genes = [(a.int)/100000.0 for a in chromo.genes]
            #print(genes)
            net.setWeights(genes)
            perf = net.getError(t_model)
            chromo.fitness = 1/perf
            #print(perf)
        #print(p.getTotalFitness())
        p.newGeneration()
    print(net.getOutputs([0, 0]))
    print(net.getOutputs([0, 1]))
    print(net.getOutputs([1, 0]))
    print(net.getOutputs([1, 1]))
    print(net.getError(t_model))
    
#testPerceptron()
testNeuralNet()
#testNeuralNetWithGA()