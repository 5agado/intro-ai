from neural_network.perceptron import Perceptron
from util import utils
import os

p = Perceptron(2)
p.learn(os.path.join(utils.getResourcesPath(), 'logic_gates/AND.txt'))
print(p.getOutput([0, 0]))
print(p.getOutput([0, 1]))
print(p.getOutput([1, 0]))
print(p.getOutput([1, 1]))