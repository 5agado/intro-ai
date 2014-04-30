import os
import random
from util import utils
from numpy import matrix
from bitstring import BitArray
from genetic_algorithm.population import Population
from numpy.lib.function_base import average
from numpy.core.fromnumeric import var

'''
Given a matrix of int numbers from 0 to 9, divide it in N sub-matrixes 
with entire vertical or horizontal slices
such that the "sum" of each matrix is the same as the other ones'
'''

def readMatrix(filename):
    filePath = os.path.join(utils.getResourcesPath(), filename)
    m = matrix(utils.readMatrix(filePath))
    print(m)
    print("------")
    return m

def computeSums(m, col, row):
    numR, numC = m.shape
    sums = []
    cS = 0
    rS = 0
    for i in range(numC-1):
        if col[i]:
            for j in range(numR-1):
                if row[j]:
                    #print(m[rS:j+1, cS:i+1])
                    sums.append(m[rS:j+1, cS:i+1].sum())
                    rS = j+1
            sums.append(m[rS:numR, cS:i+1].sum())
            #print(m[rS:numR, cS:i+1])
            cS = i+1
        rS = 0
    for j in range(numR-1):
        if row[j]:
            sums.append(m[rS:j+1, cS:numC].sum())
            #print(m[rS:j+1, cS:numC])
            rS = j+1
    sums.append(m[rS:numR, cS:numC].sum())
    #print(m[rS:numR, cS:numC])
    return sums

def initPopulation(p, numC, numR):
    cValue = ['0', '1']
    for i in range(len(p.chromos)):
        ran = "".join([random.choice(cValue) for _ in range(numC - 1)])
        p.chromos[i].genes[0] = BitArray("0b" + ran)
        ran = "".join([random.choice(cValue) for _ in range(numR - 1)])
        p.chromos[i].genes[1] = BitArray("0b" + ran)

def evolve(p, m):
    for j in range(200):
        for i in range(len(p.chromos)):
            sums = computeSums(m, p.chromos[i].genes[0], p.chromos[i].genes[1])
            if len(sums) == 1:
                p.chromos[i].fitness = 0.1
            else:
#                 if var(sums) == 0.0:
#                     print('Solution:')
#                     print(sums)
#                     return
                p.chromos[i].fitness = (1/(var(sums) + 0.0001)) #+ (len(sums)/(numR*numC))
        if j%10 == 0:
            best = p.getBestIndividuals()
            sums = computeSums(m, best[0].genes[0], best[0].genes[1])
            print("best")
            print(sums)
            print(var(sums))
            print(best[0].fitness)
        p.newGeneration()


def main():
    m = readMatrix('matrix_games/5x5.txt')
    numR, numC = m.shape
    
    Population.initPopulation = initPopulation
    Population.evolve = evolve
    p = Population(30, 2)
    p.initPopulation(numC, numR)
    p.evolve(m)
    
main()