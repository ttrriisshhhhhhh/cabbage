
"""
— Initialize the parameters (weights: w, bias: b)
— Optimize the loss iteratively to learn parameters (w,b)
— Compute the loss function and its gradients
— Update parameters using an optimization algorithm (e,g, Adam)
— Use the learned parameters to predict the label for a given input image
"""

import logging
import torch.optim as opt
import torch.nn as nets

from matplotlib import pyplot as plt

from .cnn import CabbageNet
from ..disease.types import Disease

logger = logging.getLogger(__name__)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


# following function (plot_with_labels) is for visualization, can be
# ignored if not interested
from matplotlib import cm
try:
    from sklearn.manifold import TSNE
    HAS_SK = True
except:
    HAS_SK = False
    print('Please install sklearn for layer visualization')


def plot_with_labels(lowDWeights, labels):
    plt.cla()
    X, Y = lowDWeights[:, 0], lowDWeights[:, 1]
    for x, y, s in zip(X, Y, labels):
        c = cm.rainbow(int(255 * s / 9))
        plt.text(x, y, s, backgroundcolor=c, fontsize=9)
    plt.xlim(X.min(), X.max())
    plt.ylim(Y.min(), Y.max())
    plt.title('Visualize last layer')
    plt.show()
    plt.pause(0.01)

plt.ion()


def net_train(train_data, learning_rate=0.001,
              criterion=nets.CrossEntropyLoss()
              ):
    """ For training the ConvNet """

    classes = Disease()
    cab_net = CabbageNet(len(classess.__list__())).to(device)
    optimizer = opt.Adam(cab_net.parameters(), lr=learning_rate)
