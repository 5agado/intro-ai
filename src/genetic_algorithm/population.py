import random
from bitstring import BitArray

class Population(object):
    '''
    A population of chromosome with genetic-algorithm related
    methods
    '''
    crossover_rate = 0.7
    mutation_rate = 0.001
    generation_num = 0

    def __init__(self, size = 0, chromoSize = 0):
        self.chromoSize = chromoSize
        self.chromos = [self.Chromo(chromoSize) for _ in range(size)]
        
    def randomInitPopulation(self, geneLength, mivVal, maxVal):
        for i in range(len(self.chromos)):
            for j in range(self.chromoSize):
                self.chromos[i].genes[j] = (
                    BitArray(int=random.randint(mivVal, maxVal), length=geneLength))
             
    def newGeneration(self):
        newGen = []
        
        for _ in range(len(self.chromos)//2):
            #trasform to single bit array
            c1 = self.rouletteSelection()
            offspring1 = BitArray()
            for gene in c1.genes:
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
            for i in range(self.chromoSize):
                newC1genes.append(offspring1[(i*21):((i+1)*21)])
            newC1.genes = newC1genes
            
            newC2 = self.Chromo(self.chromoSize)
            newC2genes = []
            for i in range(self.chromoSize):
                newC2genes.append(offspring2[(i*21):((i+1)*21)])
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
            #print(p)
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
    
    class Chromo(object):
        '''
        The basic unit of the genetic population.
        '''

        def __init__(self, size):
            self.genes = [None] * size
            self.fitness = 0.0