import os
import random
import pygame
import sys
from util import utils
from time import sleep

square_l = 10
pacman_r, pacman_c = None, None
food_r, food_c = None, None
r,c = None, None
visited = []
fPath = []

def dfs(grid, start, end, path = []):
    #print(start)
    global visited
    global fPath
    fPath.append(start)
    stack = list()
    path = path + [start]
    if start == end:
        #path.append(len(path))
        return path
    up = (start[0]-1, start[1])
    left = (start[0], start[1]-1)
    right = (start[0], start[1]+1)
    down = (start[0]+1, start[1])
    if (grid[up[0]][up[1]] != '%') and (not up in visited):
        stack.append(up)
        visited.append(up)
    if (grid[left[0]][left[1]] != '%') and (not left in visited):
        stack.append(left)
        visited.append(left)
    if (grid[right[0]][right[1]] != '%') and (not right in visited):
        stack.append(right)
        visited.append(right)
    if (grid[down[0]][down[1]] != '%') and (not down in visited):
        stack.append(down)
        visited.append(down)
    while len(stack) > 0:
        node = stack.pop()
        newpath = dfs(grid, node, end, path)
        if newpath:
            return newpath
        
    return None

def bfs(grid, start, end, path = []):
    #print(start)
    global visited
    global fPath
    stack = list()
    stack.append(start)
    while len(stack) > 0:
        node = stack.pop(0)
        fPath.append((node[0], node[1]))
        if (node[0], node[1]) == end:
            while True:
                path.insert(0, node)
                node = node[2]
                #print(node)
                if ((node[0], node[1]) == start):
                    path.insert(0, start)
                    return path
        up = (node[0]-1, node[1])
        left = (node[0], node[1]-1)
        right = (node[0], node[1]+1)
        down = (node[0]+1, node[1])
        if (grid[up[0]][up[1]] != '%') and (not up in visited):
            stack.append((up[0], up[1], node))
            visited.append(up)
        if (grid[left[0]][left[1]] != '%') and (not left in visited):
            stack.append((left[0], left[1], node))
            visited.append(left)
        if (grid[right[0]][right[1]] != '%') and (not right in visited):
            stack.append((right[0], right[1], node))
            visited.append(right)
        if (grid[down[0]][down[1]] != '%') and (not down in visited):
            stack.append((down[0], down[1], node))
            visited.append(down)
        
    return None

def astar(grid, start, end):
    frontier = list()
    costs = {}
    explored = list()
    path = {}
    frontier.append(start)
    costs[start] = manDistance(start, end)
    while len(frontier) > 0:
        #take cheapest one. Implement with priority queue
        index = 0
        minv = costs[frontier[index]]
        for i in range(len(frontier)):
            if costs[frontier[i]] < minv:
                minv = costs[frontier[i]]
                index = i
        node = frontier.pop(index)
        if node == end:
            respath = [node]
            while True:
                respath.insert(0, path[node])
                node = path[node]
                if node == start:
                    return respath  
        explored.append(node)
        stack = []
        up = (node[0]-1, node[1])
        left = (node[0], node[1]-1)
        right = (node[0], node[1]+1)
        down = (node[0]+1, node[1])
        if (grid[up[0]][up[1]] != '%'):
            cost = 1 if (grid[up[0]][up[1]] == '-') else 0
            stack.append(((up[0], up[1]), cost))
        if (grid[left[0]][left[1]] != '%'):
            cost = 1 if (grid[left[0]][left[1]] == '-') else 0
            stack.append(((left[0], left[1]), cost))
        if (grid[right[0]][right[1]] != '%'):
            cost = 1 if (grid[right[0]][right[1]] == '-') else 0
            stack.append(((right[0], right[1]), cost))
        if (grid[down[0]][down[1]] != '%'):
            cost = 1 if (grid[down[0]][down[1]] == '-') else 0
            stack.append(((down[0], down[1]), cost))
        for child in stack:
            if not child[0] in explored or not child[0] in frontier:
                path[child[0]] = node
                frontier.append(child[0])
                costs[child[0]] = (costs[node] + child[1] + 
                abs(manDistance(child[0], end) - manDistance(node, end)))
            elif costs[child[0]] > (costs[node] + child[1] + abs(manDistance(child[0], end) - manDistance(node, end))):
                path[child[0]] = node
                costs[child[0]] = costs[node] + child[1] + abs(manDistance(child[0], end) - manDistance(node, end))
            
            
    return None

def manDistance(node, goal):
    x = abs(node[0] - goal[0])
    y = abs(node[1] - goal[1])
    return x+y

def readMaze(filename):
    global pacman_r, pacman_c
    global food_r, food_c
    global r,c
    
    filePath = os.path.join(utils.getResourcesPath(), filename)
    f = open(filePath, 'r')
    pacman_r, pacman_c = [ int(i) for i in f.readline().strip().split() ]
    food_r, food_c = [ int(i) for i in f.readline().strip().split() ]
    r,c = [ int(i) for i in f.readline().strip().split() ]
    
    grid = []
    for i in range(0, r):
        grid.append(f.readline().strip())
    return grid

def renderMaze(window, m, pos):
    window.fill((255, 255, 255))
    global r, c
    for y in range(r):
        for x in range(c): 
            if m[y][x] == '%':
                box = pygame.Rect(x*square_l, y*square_l, square_l, square_l)
                pygame.draw.rect(window, (0, 0, 0), box, 0)
    
    box = pygame.Rect(pos[1]*square_l, pos[0]*square_l, square_l, square_l)
    pygame.draw.rect(window, (255, 0, 0), box, 0)
    pygame.display.update()
    pygame.time.delay(10)
    
def main():     
    #pygame.init()     
    maze = readMaze('hackerrank\pacman.txt')
    #window = pygame.display.set_mode((c * square_l, r * square_l))
    #visited.append((pacman_r, pacman_c))
    res = dfs(maze, (pacman_r, pacman_c), (food_r, food_c))
    print(len(res))
    #renderMaze(window, maze, (pacman_c, pacman_r))
    for line in res:
        #renderMaze(window, maze, line)
        print(line[0], line[1])
        #sleep(0.5)
#     print(len(fPath))
#     for line in fPath:
#         #renderMaze(window, maze, line)
#         print(line[0], line[1])
#         #sleep(0.5)
    
#     while True: 
#         for event in pygame.event.get(): 
#             if event.type == pygame.QUIT: 
#                 sys.exit(0)

main()