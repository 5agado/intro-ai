from genetic_algorithm.population import Population
import numpy as np
from bitstring import BitArray
import matplotlib.pyplot as plt
from matplotlib import cm

fitnessHistory = []
history = []

def initPopulation(p):
    for i in range(p.size):
        randomVector = np.random.randint(0, 2, 50)
        p.chromos[i].genes[0] = BitArray(bin=''.join(list(map(str, randomVector))))

def evolve(p):
    for _ in range(100):
        popFitness = []
        for i in range(p.size):
            gene = p.chromos[i].genes[0].bin
            v = [int(gene[i:i+1]) for i in range(len(gene))]
            p.chromos[i].fitness = np.mean(v)
            popFitness.append(p.chromos[i].fitness)
        best = p.getBestIndividuals()[0]
        fitnessHistory.append(best.fitness)
        history.append(popFitness)
        if best.fitness == 1:
            break
        #print(best.fitness)
        p.newGeneration()

def main(): 
    global fitnessHistory  
    Population.initPopulation = initPopulation
    Population.evolve = evolve
    p = Population(30, 1)
    #fig = plt.figure()
    
    for i in range(1):
        colors = ['b', 'r', 'g']
        p.initPopulation()
        p.evolve()
        
        #ax = fig.add_subplot(111)
        #ax.plot(np.arange(len(fitnessHistory)), fitnessHistory, c=colors[i])
        fitnessHistory = []
    
    h = np.array(history)
    h = np.rot90(h, 1)
    print(h)
    plt.imshow(h, cmap='Greys', aspect='auto', interpolation='nearest')
    plt.show()

main()