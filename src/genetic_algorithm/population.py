import random
import operator
from bitstring import BitArray

class Population(object):
    '''
    A population of chromosome with genetic-algorithm related
    methods
    '''
    crossover_rate = 0.7
    mutation_rate = 0.01
    generation_num = 0
    elites_num = 2 #best if even for the newGeneration process

    def __init__(self, size = 0, chromoSize = 0):
        self.chromoSize = chromoSize
        self.size = size
        self.chromos = [self.Chromo(chromoSize) for _ in range(size)]
    
    def initPopulation(self):
        raise NotImplementedError()
    
    '''
    Should define the evaluation of each hypothesis and relative
    fitness assignment. The newGeneration method can then be called
    '''
    def evolve(self):
        raise NotImplementedError()
             
    def newGeneration(self):
        #elitarism
        newGen = self.getBestIndividuals(self.elites_num)
        
        while len(newGen) < self.size:
            g_len = [None] * self.chromoSize #lengths of a chromo genes
            
            #trasform to single bit array
            c1 = self.rouletteSelection()
            offspring1 = BitArray()
            for i, gene in enumerate(c1.genes):
                g_len[i] = len(gene)
                offspring1.append(gene)
                
            c2 = self.rouletteSelection()
            offspring2 = BitArray()
            for gene in c2.genes:
                offspring2.append(gene)
                
            self.crossover(offspring1, offspring2)
            self.mutate(offspring1)
            self.mutate(offspring2)
            
            #return to array of bit arrays            
            newC1 = self.Chromo(self.chromoSize)
            newC1genes = []
            lim = 0
            for i in range(self.chromoSize):
                newC1genes.append(offspring1[(lim):(lim + g_len[i])])
                lim += g_len[i]
            newC1.genes = newC1genes
            
            newC2 = self.Chromo(self.chromoSize)
            newC2genes = []
            lim = 0
            for i in range(self.chromoSize):
                newC2genes.append(offspring2[(lim):(lim + g_len[i])])
                lim += g_len[i]
            newC2.genes = newC2genes
                
            
            newGen.append(newC1)
            newGen.append(newC2)
            
            
        self.chromos = newGen
        self.generation_num += 1
        
        
    def rouletteSelection(self):
        totalFitness = self.getTotalFitness()
        if (totalFitness == 0.0):
            return random.choice(self.chromos)
        
        rSlice = random.uniform(0, 1) * totalFitness
        fitnessSoFar = 0.0        
        
        for chromo in self.chromos:
            fitnessSoFar += chromo.fitness
            if (fitnessSoFar >= rSlice):
                return chromo
            
    def crossover(self, offspring1, offspring2):
        if random.uniform(0, 1) < self.crossover_rate:
            p = random.choice(range(len(offspring1)))
            for i in range(p, len(offspring1)):
                offspring1[i], offspring2[i] = offspring2[i], offspring1[i]  
                
    def mutate(self, genes):
        for i in range(len(genes)):
            if (random.uniform(0, 1) <= self.mutation_rate):
                genes.invert(i)                     
        
    def getTotalFitness(self):
        total = 0.0
        for chromo in self.chromos:
            total += chromo.fitness
        return total
    
    def getBestIndividuals(self, numIndividuals = 1):
        sorted_pop = sorted(self.chromos, key=operator.attrgetter('fitness'), reverse=True)
        return sorted_pop[:numIndividuals]
    
    class Chromo(object):
        '''
        The basic unit of the genetic population.
        A chromo is composed by different genes that together 
        encode a possible solution to the problem
        '''

        def __init__(self, size):
            self.genes = [None] * size
            self.fitness = 0.0