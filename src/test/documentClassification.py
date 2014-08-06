from util import utils
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import HashingVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm.classes import LinearSVC
from sklearn.linear_model.logistic import LogisticRegression

N = None #the number of docs to be categorized.
T = None #the number of training examples.

def readData(filename):    
    filePath = os.path.join(utils.getResourcesPath(), filename)
    f = open(filePath, 'r')
    global N, T
    N = int(f.readline().strip())
    
    docs = []
    for _ in range(0, N):
        docs.append(f.readline().strip())
        
    #training data
    filePath = os.path.join(utils.getResourcesPath(), 'hackerrank/trainingdata.txt')
    f = open(filePath, 'r')
    T = int(f.readline().strip())
    
    t_docs = []
    t_docsCategories = []
    for _ in range(0, T):
        cat, doc = f.readline().strip().split(' ', 1)
        t_docsCategories.append(cat)
        t_docs.append(doc)
        
    return docs, t_docs, t_docsCategories


data = readData('hackerrank/documentClassification.txt')
X_train = np.array(data[1])
y_train = np.array(data[2])
X_test = np.array(data[0])
print("Extracting features from the training dataset using a sparse vectorizer")
#vectorizer = HashingVectorizer(stop_words='english', non_negative=True)
vectorizer = TfidfVectorizer(min_df=2, 
 ngram_range=(1, 2), 
 stop_words='english', 
 strip_accents='unicode', 
 norm='l2')
X_train = vectorizer.fit_transform(X_train)
#vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
#                                 stop_words='english')
#X2_train = vectorizer.fit_transform(data_train.data)
X_test = vectorizer.transform(X_test)

nb_classifier = MultinomialNB().fit(X_train, y_train)
svm_classifier = LinearSVC().fit(X_train, y_train)
maxent_classifier = LogisticRegression().fit(X_train, y_train)

y_nb_predicted = nb_classifier.predict(X_test)
print(y_nb_predicted)
y_nb_predicted = svm_classifier.predict(X_test)
print(y_nb_predicted)
y_nb_predicted = maxent_classifier.predict(X_test)
print(y_nb_predicted)