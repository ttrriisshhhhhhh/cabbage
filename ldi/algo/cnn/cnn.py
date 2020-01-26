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


class CabbageNet(nets.Module):
    """ ConvNet implementation for classifying diseases in
        cabbage leaves
    """

    def __init__(self, classes):
        super(CabbageNet, self).__init__()

        """ ===========================================================
            2d Convolutional Layers that utilize Same padding
            ReLU Activations
            2d Max Pooling
        =========================================================== """

        """ Layer 1 input image shape (3 x 400 x 400) """
        self.conv_layer1 = nets.Sequential(
            nets.Conv2d(1, 16, kernel_size=3, stride=1),
            nets.ReLU(),
            nets.MaxPool2d(kernel_size=2, stride=1),
        )

        """ Layer 2 input shape (32 x 200 x 200) """
        self.conv_layer2 = nets.Sequential(
            nets.Conv2d(16, 32, kernel_size=3, stride=1),
            nets.ReLU(),
            nets.MaxPool2d(kernel_size=2, stride=1),
        )

        """ Layer 3 input shape (64 x 100 x 100) """
        self.conv_layer3 = nets.Sequential(
            nets.Conv2d(32, 64, kernel_size=3, stride=1),
            nets.ReLU(),
            nets.MaxPool2d(kernel_size=2, stride=1),
        )

        """ ===========================================================
            Multilayer Perceptron Fully-connected NN
            Softargmax algorithm for Classification
        =========================================================== """

        """ Layer 4 FC neurons """
        self.fc_layer1 = nets.Linear(64 * 50 * 50, classes, bias=True)
        nets.init.xavier_uniform_(self.fc_layer1.weight)
        self.conv_layer4 = nets.Sequential(self.fc_layer1, nets.ReLU())

        """ Layer 5 FC neurons """
        self.fc_layer2 = nets.Linear(150000, classes, bias=True)
        nets.init.xavier_uniform_(self.fc_layer2.weight)

    def forward(self, _input_):
        """ Process the image in convolutional layers + pooling layers """
        out_cl1 = self.conv_layer1(_input_)
        out_cl2 = self.conv_layer2(out_l1)
        out_cl3 = self.conv_layer3(out_l2)

        """ Convert the output into a single column vector """
        out_flat = out_cl3.view(out_cl3.size(0), -1)

        """ Feed to the Feed forward network """
        out_fl4 = self.fc_layer1(flat)
        out_fl5 = self.fc_layer2(out_fl4)

        return out_fl5, input

    def relu(value):
        """ Rectified Learning Unit 
            Converts all negative pixel values to 0
        """
        return max(0, value)
