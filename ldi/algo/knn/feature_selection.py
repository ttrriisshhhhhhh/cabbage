
"""
This is for feature seletion and extraction from the input leaf data
Goal is to extract the following:
	- Gray Level Co-occurance 
	- Color Histogram
	- """

import numpy as np
import matplotlib.pyplot as plt

x0 = np.random.rand(500) - 0.5
x1 = np.random.rand(500) - 0.5
X = np.array(list(zip(x0, x1)))
y = np.array([1 if i0 * i1 > 0 else 0 for (i0, i1)  in list(zip(x0, x1))])

plt.scatter(X[:,0], X[:,1], c=y)

from knnFeat import knnExtract

import time
start = time.time()
newX = knnExtract(X, y, k=1, folds = 5)
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

plt.scatter(newX[:,0], newX[:,1], c=y)

from sklearn import datasets
iris = datasets.load_iris()
y = iris.target
X = iris.data

plt.scatter(X[:,0], X[:,1], c=y)

newX = knnExtract(X, y, k=1, folds = 5)

plt.scatter(newX[:,0], newX[:,1], c=y)