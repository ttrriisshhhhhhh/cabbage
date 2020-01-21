"""
Implementation of available distance functions for kNN which are:
	- Euclidean Distance: for getting distance between two points in 
			a euclidean space
	- Manhattan Distance: distance between two points measured along
			axes at right angles
	- Minkowski Distance: distance between two points in the normed 
			vector space
"""

import logging
import sys

import numpy as np
from scipy.spatial import distance as dist


logger = logging.getLogger(__name__)


def euclidean_distance(pt1, pt2):
    """
    Returns euclidean distance between two points
    """
    logger.info("Calculating using Euclidean distance")
    # return np.linalg.norm(pt1 - pt2)
    return dist.euclidean(pt1, pt2)


def manhattan_distance(pt1, pt2):
    """
    Returns manhattan distance between two points
    """
    logger.info("Calculating using Manhattan distance")
    # return np.abs(r1-r2) + np.abs(c1-c2)
    return dist.manhattan(pt1, pt2)


def minkowski_distance(pt1, pt2):
    """
	Returns the Minkowski distance of the two points
	"""
    logger.info("Calculating using Minkowski distance")
    return dist.minkowski(pt1, pt2)
