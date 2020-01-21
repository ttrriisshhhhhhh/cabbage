
""" 
Utility functions for k-Nearest Neighbors algorithm

- loading data 
"""
import os

HAS_PATH = "data/original/has/"
NONE_PATH = "data/original/none"

def get_data(path):
	""" Loading list of images into the memory 
	"""
	return os.listdir(path)


def load(tagged=True):
	""" For loading data into the kNN algorithm 
	"""
	healthy = get_data(NONE_PATH)
	disease = get_data(HAS_PATH)
	hleaves = [(leaf, "healthy") for leaf in healthy]
	dleaves = [(ill, "disease") for ill in disease]
	return hleaves + dleaves
