
import os

from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
from sklearn.model_selection import train_test_split
from skimage import io, transform

import matplotlib.pyplot as plt
import numpy as np
import torch
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

BASE_PATH = "data/original"
SICK_PATH = f"{BASE_PATH}/has"
HEALTHY_PATH = f"{BASE_PATH}/none"


def get_data_list(restrict):
    """ For returning list of images for input """
    if restrict == 1:
        return sorted(os.listdir(SICK_PATH))
    elif restrict == 2:
        return sorted(os.listdir(HEALTHY_PATH))
    elif restrict == 0:
        return sorted(os.listdir(SICK_PATH) + os.listdir(HEALTHY_PATH))
    else:
        raise ValueError("Invalid parameter")
