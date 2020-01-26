
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


def show_image(image, tag):
    """ Show image with tag and infection type """
    plt.imshow(image)
    plt.title(tag)
    plt.pause(0.001)


class CabbageLeafDataSet(Dataset):
    """ This will help describe the cabbage leaf data for easier
        loading into memory of training and testing data """

    def __init__(self, csv, root_dir, transform=None):
        """ csv: holds the annotation for every training data
            root_dir: directory holding the images
            transform: optional, a callable, to be applied on images
        """
        self.leaf_data = pd.read_csv(csv)
        self.root_dir = root_dir
        self.transform = transform

    def __length__(self):
        return len(self.leaf_data)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        img_name = os.path.join(self.root_dir, self.leaf_data.iloc[idx, 0])
        image = io.imread(img_name)
        leaf = self.leaf.iloc[idx, 1:]
        leaf = np.array([leaf])
        leaf = leaf.astype('float').reshape(-1, 2)
        sample = {'leaf': image, 'tag': leaf}

        if self.transform:
            sample = self.transform(sample)

        return sample
