from util import utils
import os
from queue import PriorityQueue

k = None

def readGrid(filename):    
    filePath = os.path.join(utils.getResourcesPath(), filename)
    f = open(filePath, 'r')
    global k
    k = int(f.readline().strip())
    
    grid = []
    for i in range(0, k):
        grid.append([])
        for _ in range(0, k):
            grid[i].append(f.readline().strip())
    return grid

def getValidNextConfigs(grid):
    k = len(grid)
    validNextConfigs = []
    moves = []
    for y in range(0, k):
        if '0' in grid[y]:
            x = grid[y].index('0')
            if y != 0:
                validNextConfigs.append(getResConfig(grid, 'UP'))
                moves.append('UP')
            if y != k-1:
                validNextConfigs.append(getResConfig(grid, 'DOWN'))
                moves.append('DOWN')
            if x != 0:
                validNextConfigs.append(getResConfig(grid, 'LEFT'))
                moves.append('LEFT')
            if x != k-1:
                validNextConfigs.append(getResConfig(grid, 'RIGHT'))
                moves.append('RIGHT')
    return validNextConfigs, moves
  
def getResConfig(grid, move = 'UP'):
    k = len(grid)
    x = None
    y = None
    resConfig = []
    for i in range(0, k):
        resConfig.append([])
        if '0' in grid[i]:
            y = i
            x = grid[y].index('0')
        for j in range(0, k):
            resConfig[i].append(grid[i][j])
    if move == 'UP':
        resConfig[y][x] = resConfig[y-1][x]
        resConfig[y-1][x] = '0'
    elif move == 'DOWN':
        resConfig[y][x] = resConfig[y+1][x]
        resConfig[y+1][x] = '0'
    elif move == 'LEFT':
        resConfig[y][x] = resConfig[y][x-1]
        resConfig[y][x-1] = '0'
    elif move == 'RIGHT':
        resConfig[y][x] = resConfig[y][x+1]
        resConfig[y][x+1] = '0'
    return resConfig 

#hFunction = ['misplaces', 'manhattan']
def getHeuristicCost(grid, hFunction = 'manhattan'):
    k = len(grid)
    cost = 0
    for i in range(0, k):
        for j in range(0, k):
            if grid[i][j] != '0' and grid[i][j] != str(j + (k*i)):
                if (hFunction == 'misplaced'):
                    cost += 1
                elif (hFunction == 'manhattan'):
                    value = int(grid[i][j])
                    cost +=  abs(value//k - i) + abs(value%k - j)
    return cost

def ucs(grid, start, end):
    frontier = PriorityQueue()
    costs = {}
    explored = list()
    path = {}
    moves = {}
    costs[start] = getHeuristicCost(grid)
    frontier.put((costs[start], start))
    while not frontier.empty():
        conf = frontier.get()[1]
        #found solution. Building path via backward visit
        gridConf = stringToGrid(conf, k)
        if getHeuristicCost(gridConf) == 0:
            resmove = []
            respath = [conf]
            while True:
                resmove.insert(0, moves[conf])
                respath.insert(0, path[conf])
                conf = path[conf]
                if conf == start:
                    return resmove 
        explored.append(conf)
        validNextConfigs, nextMoves = getValidNextConfigs(gridConf)
        for i in range(len(validNextConfigs)):
            nextConf = validNextConfigs[i]
            move = gridToString(nextConf)
            if not move in explored: #or not move in frontier:
                path[move] = conf
                moves[move] = nextMoves[i]
                costs[move] = costs[conf] + (getHeuristicCost(nextConf) - getHeuristicCost(gridConf)) + 1
                frontier.put((costs[move], move))
            elif ((costs[move] > (costs[conf] + (getHeuristicCost(nextConf) - getHeuristicCost(gridConf)) + 1))):
                path[move] = conf
                moves[move] = nextMoves[i]
                costs[move] = (costs[conf] + (getHeuristicCost(nextConf) - getHeuristicCost(gridConf)) + 1)            
            
    return None

def stringToGrid(value, k):
    grid = []
    for i in range(0, k):
        grid.append([])
        for j in range(0, k):
            grid[i].append(value[i*k + j])
    return grid

def gridToString(grid):
    k = len(grid)
    value = ''
    for i in range(0, k):
        for j in range(0, k):
            value += grid[i][j]
    return value

grid = readGrid("hackerrank/8Puzzle.txt") 
end = readGrid("hackerrank/8PuzzleEnd.txt") 
print('-'*10)
path = ucs(grid, gridToString(grid), gridToString(end))
print(len(path))
# for res in path: 
#     grid = stringToGrid(res, k)   
#     for row in grid:
#         print(row)
#    print('-'*10)