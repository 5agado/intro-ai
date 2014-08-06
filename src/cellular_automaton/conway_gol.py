import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 100
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
    im.set_data(grid)
    return grid
        
fig, ax = plt.subplots()
im = ax.imshow(grid, cmap='Greys', interpolation='nearest')
ani = animation.FuncAnimation(fig, update, interval=100, save_count=50)
plt.show()    