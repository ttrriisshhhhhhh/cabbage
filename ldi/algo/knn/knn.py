
"""
This is the main implementation of kNN in Python 3.7 
for the purposes of classifying cabbage leaf diseases
"""

from collections import Counter

import os

from skimage.color import rgb2lab, deltaE_cie76
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

import numpy as np 
import cv2


def compute_glcm(image):
	""" This return the grey level co-occurence matrix (glcm) of the 
	input image that serves as one of the features for kNN
	"""

