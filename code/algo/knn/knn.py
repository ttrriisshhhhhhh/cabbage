
"""
This is the main implementation of kNN in Python 3.7 
for the purposes of classifying cabbage leaf diseases
"""

import os

HAS_PATH = "data/original/has/"
NONE_PATH = "data/original/none"

def get_data(path):
	""" Loading list of images into the memory """
	return os.listdir(path)

def load():
	""" For loading data into the kNN algorithm """
	healthy_leaves = get_data(NONE_PATH)
	disease_leaves = get_data(HAS_PATH)

	return [healthy_leaves, disease_leaves]
