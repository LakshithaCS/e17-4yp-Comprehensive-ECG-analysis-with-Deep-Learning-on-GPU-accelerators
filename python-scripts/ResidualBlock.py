import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset # wraps an iterable around the dataset
from torchvision import datasets    # stores the samples and their corresponding labels
from torchvision.transforms import transforms  # transformations we can perform on our dataset
from torchvision.transforms import ToTensor
import pandas as pd
import numpy as np
import os
import wandb
import matplotlib.pyplot as plt

# Residual Block
class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(ResidualBlock, self).__init__()
        # First convolutional layer of the residual block
        self.conv1 = nn.Conv1d(in_channels, out_channels, kernel_size=3, stride=1, padding=1)
        self.relu = nn.ReLU()
        # Second convolutional layer of the residual block
        self.conv2 = nn.Conv1d(out_channels, out_channels, kernel_size=3, stride=1, padding=1)

    def forward(self, x):
        residual = x
        # Pass input through the first convolutional layer
        out = self.conv1(x)
        out = self.relu(out)
        # Pass the output of the first convolutional layer through the second convolutional layer
        out = self.conv2(out)
        # Add the residual connection
        out += residual
        out = self.relu(out)
        return out