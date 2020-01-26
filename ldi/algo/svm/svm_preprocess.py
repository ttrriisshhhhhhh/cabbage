import numpy as np
import cv2
import pandas as pd
from sklearn import svm
from matplotlib import pyplot as plt

def feature_mapping():
	# Importing of CSV file
	data = np.genfromtxt("cabbage/ldi/algo/knn/dummy_data.csv", names=True,
						dtype="float", delimiter=",")
	

	cat1_list = list(data["category_1"])
	cat2_list = list(data["category_2"])
	#print(cat1_list)
	#print(cat2_list)
	#plt.plot(data["category_1"], data["category_2"],"o")
	plt.xlabel("category_1")
	plt.ylabel("category_2")

	X = np.column_stack((cat1_list,cat2_list))

	print(X)
	y = list (data["class"])
	print(y)
	clf = svm.SVC(kernel='linear', C=1)
	clf.fit(X,y)
	plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
	ax = plt.gca()
	xlim = ax.get_xlim()
	ylim = ax.get_ylim()
	xx = np.linspace(xlim[0], xlim[1], 30)
	yy = np.linspace(ylim[0], ylim[1], 30)
	YY, XX = np.meshgrid(yy, xx)
	xy = np.vstack([XX.ravel(), YY.ravel()]).T
	Z = clf.decision_function(xy).reshape(XX.shape)

	ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])

	ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100,
           linewidth=1, facecolors='none', edgecolors='k')

	plt.show()

feature_mapping()