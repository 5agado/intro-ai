from util import utils
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.preprocessing import normalize
import math

M = None #the amount of money you could spend that day.
K = None #the number of different stocks available for buying or selling.
D = None #the number of remaining days for trading stocks.

def readData(filename):    
    filePath = os.path.join(utils.getResourcesPath(), filename)
    f = open(filePath, 'r')
    global M, K, D
    initValues =  f.readline().strip().split()
    M = float(initValues[0])
    K = int(initValues[1])
    D = int(initValues[2])
    
    data = []
    names = []
    owned = []
    for _ in range(0, K):
        line = f.readline().strip().split()
        names.append(line[0])
        owned.append(int(line[1]))
        data.append(list(map(float, line[2:])))
        
    return names, owned, data

def movingAverage(values, windowSize):
    #weigths = np.repeat(1.0, windowSize)/windowSize
    weigths = np.ones(int(windowSize))/float(windowSize)
    #including valid will REQUIRE there to be enough datapoints.
    #for example, if you take out valid, it will start @ point one,
    #not having any prior points, so it'll be 1+0+0 = 1 /3 = .3333
    return np.convolve(values, weigths, 'same')

names, owned, data = readData("hackerrank/stocksComplete.txt")
print(names)
print(data)

smas = []
for i in range(K):
    smas.append(movingAverage(data[i], 3)) 

#Dumb first try
#consider the distance of the last point from the SMA1
dists = [0]*K
psum = 0
maxVal = -100
maxIndex = None
count = 0
for i in range(K):
    dists[i] = data[i][-1] - smas[i][-2]
    if dists[i] > -30:
        psum += dists[i]
        if ((not maxIndex) or dists[i] > maxVal) and (data[i][-1]<M):
            maxVal = dists[i]
            maxIndex = i
    elif dists[i]<-30 and owned[i] > 2:
        count += 1

if maxIndex:
    count += 1
print(count)
if maxIndex:
    print('{} {} {}'.format(names[maxIndex], 'BUY', int(M/data[maxIndex][-1])))
for i in range(K):
    action = None
    amount = None
    if dists[i]<-30 and owned[i] > 2:
        amount = int(owned[i]/2)
        print('{} {} {}'.format(names[i], 'SELL', max(int(owned[i]/2),1)))

#plotting
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = fig.add_subplot(111)
ax1.scatter(np.arange(len(data[0])), data[0], marker='x', c='b')
ax1.plot(np.arange(len(smas[0])), smas[0], 'g-')
ax2.scatter(np.arange(len(data[1])), data[1], marker='o', c='r')
ax2.plot(np.arange(len(smas[1])), smas[1], 'b--')
plt.show()