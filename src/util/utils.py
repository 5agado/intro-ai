import os

def dotProduct(values1, values2):
        return sum(value1 * value2 for value1, value2 in zip(values1, values2))
    
def getResourcesPath():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir, 'resources'))