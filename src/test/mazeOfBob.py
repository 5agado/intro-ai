import os
import random
import pygame
import sys
from util import utils
from numpy import matrix
from bitstring import BitArray
from genetic_algorithm.population import Population
import math
from time import sleep

'''
Simple maze game.
The maze is encoded as a matrix of int
'''

square_l = 10
start = None
end = None

def readMaze(filename):
    filePath = os.path.join(utils.getResourcesPath(), filename)
    m = matrix(utils.readMatrix(filePath))
    numR, numC = m.shape
    #find start and end
    for y in range(numR):
        for x in range(numC): 
            if m.item((y, x)) == 5:
                global start
                start = (y, x)
            if m.item((y, x)) == 8:
                global end
                end = (y, x)
    return m

def renderMaze(window, m, path = None):
    window.fill((255, 255, 255))
    numR, numC = m.shape
    for y in range(numR):
        for x in range(numC): 
            if m.item((y, x)) == 1:
                box = pygame.Rect(x*square_l, y*square_l, square_l, square_l)
                pygame.draw.rect(window, (0, 0, 0), box, 0)
    if path:
        for pos in path:
            box = pygame.Rect(pos[1]*square_l, pos[0]*square_l, square_l, square_l)
            pygame.draw.rect(window, (255, 0, 0), box, 0)
    pygame.display.update()
    pygame.time.delay(10)
    
def isValid(p, m):
    numR, numC = m.shape
    if (p[0] < 0 or p[0] >=numR):
        return False
    if (p[1] < 0 or p[1] >=numC):
        return False
    if (m.item(p) == 1 or m.item(p) == 5):
        return False
    return True
    
def walkChromo(genes, m):
    pos = start
    path = []
    for move in genes:
        if move.bin == '00':
            pos = (pos[0], pos[1] +1)
        elif move.bin == '01':
            pos = (pos[0], pos[1] -1)
        elif move.bin == '10':
            pos = (pos[0] - 1, pos[1])
        elif move.bin == '11':
            pos = (pos[0] + 1, pos[1])
        else:
            raise Exception("No such move")
        if not(isValid(pos, m)):
            #return 0, path
            break
        else:
            path.append(pos)
    if pos == end:
        dist = 0.0001
    else:
        dist = math.fabs(pos[0] - end[0]) + math.fabs(pos[1] - end[1])
    fitness = (1/dist) #- len(path)/150
    return fitness, path

#the genes are encoded as moves (R, L, U, D) in the maze    
def initPopulation(p):
    cValue = ['00', '01', '10', '11']
    for i in range(p.size):
        for j in range(p.chromoSize):
            p.chromos[i].genes[j] = BitArray("0b" + random.choice(cValue))

def evolve(p, w, m):
    for _ in range(200):
        for i in range(len(p.chromos)):
            fitness, _ = walkChromo(p.chromos[i].genes, m)
            p.chromos[i].fitness = fitness
        fitness, bestPath = walkChromo(p.getBestIndividuals()[0].genes, m) 
        print(fitness)
        #print(p.generation_num)
        renderMaze(w, m, bestPath)
        p.newGeneration()
    
def main():     
    pygame.init()     
    maze = readMaze('mazes/9x15.txt')
    numR, numC = maze.shape
    window = pygame.display.set_mode((numC * square_l, numR * square_l))
    renderMaze(window, maze)
    
    Population.initPopulation = initPopulation
    Population.evolve = evolve
    p = Population(50, 30)
    p.mutation_rate = 0.1
    p.elites_num = 5
    p.initPopulation()
    p.evolve(window, maze)
    print("done")
    
    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit(0)

main()