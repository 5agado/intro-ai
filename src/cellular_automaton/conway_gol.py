import numpy as np
import pygame
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import sleep

N = 100
square_l = 2
grid = np.random.choice(2, N*N, p=[0.5, 0.5]).reshape(N, N)

def update(data):
    global grid
    tmpGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            neighbours = (grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])
            if grid[i][j] == 1:
                if neighbours > 3 or neighbours < 2:
                    tmpGrid[i][j] = 0
            else:
                if neighbours == 3:
                    tmpGrid[i][j] = 1
    grid = tmpGrid
    #im.set_data(grid)
    return grid

def renderGrid(window):
    global grid
    window.fill((255, 255, 255))
    tmpGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            box = pygame.Rect(i*square_l, j*square_l, square_l, square_l)
            neighbours = (grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])
            if grid[i][j] == 1:
                if neighbours > 3 or neighbours < 2:
                    tmpGrid[i][j] = 0
                else:
                    pygame.draw.rect(window, (255, 0, 0), box, 0)
            else:
                if neighbours == 3:
                    tmpGrid[i][j] = 1
                    pygame.draw.rect(window, (255, 0, 0), box, 0)
    grid = tmpGrid

    pygame.display.update()
    pygame.time.delay(10)
        
def runWithMatPlot():
    fig, ax = plt.subplots()
    im = ax.imshow(grid, cmap='Greys', interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, interval=100, save_count=50)
    plt.show()
    
def runWithPyGame():
    pygame.init()     
    window = pygame.display.set_mode((N * square_l, N * square_l))
    
    while True:
        renderGrid(window)
        sleep(0.003)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit(0)
                
runWithPyGame()
        