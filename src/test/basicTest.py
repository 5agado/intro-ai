from neural_network.perceptron import Perceptron
from neural_network.neural_net import NeuralNet
from util import utils
import os
from bitstring import BitArray
import random
from genetic_algorithm.population import Population

def testPerceptron():
    p = Perceptron(2)
    #p.useStepFunction = True
    p.t_sessions = 2000
    t_model = utils.readTrainModel(os.path.join(utils.getResourcesPath(), 'logic_gates/NAND.txt'))
    p.learn(t_model)
    print(p.getOutput([0, 0]))
    print(p.getOutput([0, 1]))
    print(p.getOutput([1, 0]))
    print(p.getOutput([1, 1]))

def testNeuralNet():
    net = NeuralNet(2, 2, 1)
    net.t_sessions = 20000
    t_model = utils.readTrainModel(os.path.join(utils.getResourcesPath(), 'logic_gates/XOR.txt'))
    net.learn(t_model)
    print(net.getOutputs([0, 0]))
    print(net.getOutputs([0, 1]))
    print(net.getOutputs([1, 0]))
    print(net.getOutputs([1, 1]))
    
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
    
def initPopulation(p):
    for i in range(len(p.chromos)):
        for j in range(p.chromoSize):
            p.chromos[i].genes[j] = (
                BitArray(int=random.randint(-200000, 200000), length=21))

def evolve(p, net, t_model):
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
    
def testNeuralNetWithGA():
    net = NeuralNet(2, 2, 1)
    t_model = utils.readTrainModel(os.path.join(utils.getResourcesPath(), 'logic_gates/NAND.txt'))
    Population.initPopulation = initPopulation
    Population.evolve = evolve
    p = Population(70, 9)
    p.initPopulation()
    p.evolve(net, t_model)
    

    print(net.getOutputs([0, 0]))
    print(net.getOutputs([0, 1]))
    print(net.getOutputs([1, 0]))
    print(net.getOutputs([1, 1]))
    print(net.getError(t_model))
    
#testPerceptron()
#testNeuralNet()
#testNeuralNetWithGA()
#numberRecognition()