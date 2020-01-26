
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

logger = logging.getLogger(__name__)


def net_train(train_data, learning_rate=0.001,
              optimizer="Adam",
              criterion=nets.CrossEntropyLoss()
              ):
    """ For training the ConvNet """

    training_cost = []
    training_accuracy = []
    batch_size = 10
    training_epochs = 10
    batch_count = len(train_data) // batch_size

    print(f"Size of training data: {train_data.size}")
    print(f"Batch size is: {batch_size}")
    print(f"Total number of batches: {batch_count}")
    print(f"\nEpochs: {training_epochs}")
