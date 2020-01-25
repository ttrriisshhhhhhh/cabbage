""" ================================================================
This is the main ConvNet module containing necessary libraries for
implementing ConvNet.
================================================================="""

from matplotlib import pyplot as plt
from PIL import Image

import cv2
import torch
import torch.nn as nets
import numpy as np


# Device configuration
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


class CabbageNet(nets.Module):
    """ 
		ConvNet implementation for classifying diseases in
		cabbage leaves
	"""

    def __init__(self, classes):
        super(CabbageNet, self).__init__()
        """ ===========================================================
			2D Convolutional Layers that utilize Same padding
			ReLU Activations
			2D Max Pooling
		=========================================================== """
        """ Layer 1 input image shape (3 x 500 x 500)
		"""
        self.conv_layer1 = nets.Sequential(
            nets.Conv2D(3, 16, kernel_size=3, stride=1, padding=2),
            nets.ReLU(),
            nets.MaxPool2D(kernel_size=2),
        )
        """ Layer 2 input shape (16 x 250 x 250)
		"""
        self.conv_layer2 = nets.Sequential(
            nets.Conv2D(16, 32, kernel_size=3, stride=1, padding=2),
            nets.ReLU(),
            nets.MaxPool2D(kernel_size=2),
        )
        """ Layer 3 input shape (32 x 125 x 125)
		"""
        self.conv_layer3 = nets.Sequential(
            nets.Conv2D(32, 64, kernel_size=3, stride=1, padding=2),
            nets.ReLU(),
            nets.MaxPool2D(kernel_size=2),
        )
        """ ===========================================================
			Multilayer Perceptron Fully-connected NN
			Softargmax algorithm for Classification
		=========================================================== """
        self.fc_layer4 = nets.Linear(64 * 65 * 65, classes)

    def forward(self, x):
        out = self.conv_layer1(x)
        return out
