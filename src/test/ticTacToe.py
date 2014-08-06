from util import utils
import os

n= 3

player = None
against = None
    
def readMaze(filename):    
    filePath = os.path.join(utils.getResourcesPath(), filename)
    f = open(filePath, 'r')
    global player, against
    player = f.readline().strip()
    against = 'X' if player != 'X' else 'O'
    
    grid = []
    for _ in range(0, n):
        grid.append(f.readline().strip())
    return grid

def getResultState(cState, move, player):
    if (cState[move[0]][move[1]] != '_'):
        raise Exception("not valid move")
    grid = list(cState)
    line = list(grid[move[0]])
    line[move[1]] = player
    grid[move[0]] = "".join(line)
    return grid

def getValidMoves(grid):
    validMoves = []
    for i in range(0, n):
        for j in range(0, n):
            if grid[i][j] == '_':
                validMoves.append((i, j))
    return validMoves

def getWinner(grid):
    winner = None
    
    #Rows
    for i in range(0, n):
        if grid[i] == 'XXX':
            winner = 'X'
        if grid[i] == 'OOO':
            winner = 'O'
    
    #Columns
    for i in range(0, n):
        if (grid[0][i] != '_' and
            grid[0][i] == grid[1][i] and
            grid[1][i] == grid[2][i]): 
                winner = grid[0][i]
    
    #Diagonal
    if (grid[0][0] != '_' and
        grid[0][0] == grid[1][1] and
            grid[1][1] == grid[2][2]): 
                winner = grid[0][0]
    
    #Antidiagonal
    if (grid[0][2] != '_' and
        grid[0][2] == grid[1][1] and
            grid[1][1] == grid[2][0]): 
                winner = grid[0][2]
    
    return winner
    
def getMinValue(grid):
    winner = getWinner(grid)
    utility = 2
    if winner == player:
        return 1
    if winner == against:
        return -1
    validMoves = getValidMoves(grid)
    if not validMoves:
        return 0
    for move in validMoves:
        utility = min(utility, getMaxValue(getResultState(grid, move, against)))
    return utility
    
def getMaxValue(grid):
    winner = getWinner(grid)
    utility = -2
    if winner == player:
        return 1
    if winner == against:
        return -1
    validMoves = getValidMoves(grid)
    if not validMoves:
        return 0
    for move in validMoves:
        utility = max(utility, getMinValue(getResultState(grid, move, player)))
    return utility
    

def getNextMove(grid):
    validMoves = getValidMoves(grid)
    maxVal = -2
    bestMove = None
    for move in validMoves:
        val = getMinValue(getResultState(grid, move, player))
        if val > maxVal:
            maxVal = val
            bestMove = move
    return bestMove

grid = readMaze('hackerrank/ticTacToe.txt')
print(grid)
print(getNextMove(grid))