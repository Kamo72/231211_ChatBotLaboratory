
from tkinter import W
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.modules import linear
import torchmetrics
from torch.utils.data import Dataset, DataLoader
from torch import optim

import numpy as np

import torchvision.transforms as transforms
from torchvision import datasets
import matplotlib.pyplot as plt

def TestLinear():
    X, y = DataSetting()
    model = LinearRegressionModel()

    w, b = model.parameters()
    # ����ġ�� ������ �����´�.

    #w1, b1 = w[0][0].item(), b[0][0].item()
    w1, b1 = w.item(), b.item()
    x1 = np.array([-30, 30])
    y1 = w1 * x1 + b1
    # ����ġ�� ������ �����´�.
    # -30�� 30�� �Է����� ���� �������� �����ͼ� �� ���� ������ ���� �׸��� ��?

    # plt.plot(x1, y1, 'r')
    # plt.scatter(X, y)
    # plt.grid()
    # plt.show()

    loss_fn, optimizer = LossAndOpt(model)
    #�ս� �Լ�, ��Ƽ������

    #���� �н�
    epochs = 100
    losses = []
    for epoch in 










def DataSetting() :
    #�ҽ��� �� ����
    X = torch.randn(200, 1) * 10
    y = X + 3 * torch.randn(200, 1)

    #�ð�ȭ
    # plt.scatter(X.numpy(), y.numpy())
    # plt.ylabel('y')
    # plt.xlabel('x')
    # plt.grid()
    # plt.show()
    return X, y

def LossAndOpt (model):
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.Parameters(), lr = 1e-3)
    return criterion, optimizer

class LinearRegressionModel (nn.Module) :
    def __init__(self) :
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1,1)
        
    def forward(self, x) :
        x = linear(x)
        return x