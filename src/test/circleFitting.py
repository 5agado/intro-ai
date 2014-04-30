import pygame
import random
import sys
import math
from genetic_algorithm.population import Population
from bitstring import BitArray

'''
idea from http://www.ai-junkie.com/
Given an area that has a number of non overlapping circles scattered about its surface
find the disk of largest radius which may be placed amongst these disks without 
overlapping any of them
'''

d_width = 640
d_height = 480
min_r = 5 #minimal radius
max_r = 50

def intersect(c1, c2):
    x = math.pow(c1[0][0] - c2[0][0], 2) 
    y = math.pow(c1[0][1] - c2[0][1], 2)
    res = math.sqrt(x+y)
    return (res < (c1[1]+c2[1]) or res< math.fabs(c1[1]-c2[1]));

def isValid(c):
    if c[1] < min_r:
        return False    
    if (c[0][0] + c[1] > d_width) or (c[0][0] - c[1] < 0):
        return False
    if (c[0][1] + c[1] > d_height) or (c[0][1] - c[1] < 0):
        return False
    return True;

def getCircles():    
    numCircles = 10
    circles = []
    fail = False
    while (len(circles) < numCircles):
        x = random.randint(min_r, d_width - min_r)
        y = random.randint(min_r, d_height - min_r)
        if fail:
            r = random.randint(min_r, max_r//2)
        else:
            r = random.randint(min_r, max_r)
        new = [(x, y), r]
        valid = True
        for circle in circles:
            if intersect(circle, new):
                valid = False
                break
        if valid and isValid(new):
            circles.append(new)
            fail = False
        else:
            fail = True
    return circles  

def initPopulation(p):
    uint_l = 10 #uint bitarray representation length
        
    for i in range(len(p.chromos)):
        p.chromos[i].genes[0] = (BitArray(uint=random.randint(min_r, d_width - min_r), length=uint_l))
        p.chromos[i].genes[1] = (BitArray(uint=random.randint(min_r, d_width - min_r), length=uint_l))
        p.chromos[i].genes[2] = (BitArray(uint=random.randint(min_r, max_r), length=uint_l))

def evolve(p, window, circles):
    for _ in range(200):
        for i in range(len(p.chromos)):
            c = [(p.chromos[i].genes[0].uint, p.chromos[i].genes[1].uint), p.chromos[i].genes[2].uint]
            valid = True
            for circle in circles:
                if intersect(circle, c):
                    valid = False
                    break
            if valid and isValid(c):
                p.chromos[i].fitness = p.chromos[i].genes[2].uint
            else:
                p.chromos[i].fitness = 0
            #print(p.chromos[i].fitness)
        best = p.getBestIndividuals()[0]
        c = [(best.genes[0].uint, best.genes[1].uint), best.genes[2].uint]
        #print(c)
        window.fill((0, 0, 0))
        for circle in circles: 
            pygame.draw.circle(window, (255, 255, 255), circle[0], circle[1], 1)
        pygame.draw.circle(window, (255, 0, 0), c[0], c[1])
        p.newGeneration()
        pygame.display.update()
        pygame.time.delay(10)

def main():     
    pygame.init() 
    window = pygame.display.set_mode((d_width, d_height)) 
    
    circles = getCircles()
    for circle in circles: 
        pygame.draw.circle(window, (255, 255, 255), circle[0], circle[1], 1)
        
    Population.initPopulation = initPopulation
    Population.evolve = evolve
    p = Population(80, 3)
    p.initPopulation()
    p.evolve(window, circles)
        
    #pygame.display.flip()
    
    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit(0)

main()