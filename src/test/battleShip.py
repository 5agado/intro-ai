from util import utils
from random import randint
import os
import re

n = 10
HIT = 'h'
MISS = 'm'
SUNK = 'd'
EMPTY = '-'

    
def readGrid(filename):    
    filePath = os.path.join(utils.getResourcesPath(), filename)
    f = open(filePath, 'r')
    global n
    n = int(f.readline().strip())
    
    grid = []
    for _ in range(n):
        grid.append(f.readline().strip())
    return grid

def nextMove(grid):
    for y in range(n):
        line = grid[y]
        #there is one hit cell
        if 'h' in line:
            matches = re.finditer('h+', line)
            for m in matches:
                sp = m.span()
                xS, xF = sp
                if (xS - xF) > 1:
                    if xS > 0 and line[xS-1] == '-':
                        return (y, xS-1)
                    if xF < n and line[xF] == '-':
                        return (y, xF)
                else:
                    if y > 0 and grid[y-1][xS] == '-':
                        return (y-1, xS)
                    if y < n-1 and grid[y+1][xS] == '-':
                        return (y+1, xS)
                
                if xS > 0 and line[xS-1] == '-':
                    return (y, xS-1)
                if xF < n and line[xF] == '-':
                    return (y, xF)
            
    #nothing interesting, then random choice
    while(True):
        move = (randint(0, n-1), randint(0, n-1))
        if grid[move[0]][move[1]] == '-':
            return move
        
grid = readGrid('hackerrank/battleShip.txt')
print(nextMove(grid))