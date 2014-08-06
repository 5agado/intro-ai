from util import utils
import os
import numpy as np
from mpl_toolkits.mplot3d import *
from sklearn import linear_model

F = None #num of features
N = None #num of training samples
T = None #num of test samples
    
def readData(filename):    
    filePath = os.path.join(utils.getResourcesPath(), filename)
    f = open(filePath, 'r')
    global F, N, T
    F, N = map(int, f.readline().strip().split())
    
    data = []
    for _ in range(0, N):
        line = list(map(float, f.readline().strip().split()))
        data.append((line[:-1], line[-1]))
        
    T = int(f.readline().strip())    
    test = []
    for _ in range(0, T):
        line = list(map(float, f.readline().strip().split()))
        test.append(line)
    return data, test

def gradientDescent(features, values, nIter = 500, lRate = 0.001):
    X = np.append(features, np.ones((len(features),1)), axis=1) #dummy column for intercept weight
    weights = np.random.random(X.shape[1]) #consider intercept weight
    history = []
    for _ in range(nIter):
        pred = X.dot(weights).flatten()
        for i in range(F+1):
            #errors2 = [(values[i]-np.dot(weights,X[i]))*X[i] for i in range(N)]
            errors = (values - pred)* X[:, i]
            weights[i] += lRate * errors.sum()
            
            #necessary 1/n factor??
        e = sum([(values[i]-np.dot(weights,X[i]))**2 for i in range(N)])
        history.append(e)
        #history.append(weights)
    return weights, history

data, test = readData('hackerrank\\housePricing.txt')
features = np.array([[row[0][x] for x in range(F)] for row in data])
values = np.array([row[1] for row in data])

weights, history = gradientDescent(features, values)

test = np.array([[row[x] for x in range(F)] for row in test])
mTest = np.append(test, np.ones((T, 1)), axis=1)
for v in mTest.dot(weights):
    print("{0:.2f}".format(float(v)))
    
#Using sklearn
# Create linear regression object
regr = linear_model.LinearRegression()
# Train the model using the training sets
regr.fit(features, values)
for v in test.dot(regr.coef_):
    print("{0:.2f}".format(float(v)))