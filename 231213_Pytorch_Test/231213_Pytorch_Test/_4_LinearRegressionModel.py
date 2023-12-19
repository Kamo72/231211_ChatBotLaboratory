
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
    epochs = 5000
    losses = []
    for epoch in range(epochs) :
        optimizer.zero_grad() # ��Ƽ�������� ���� 0����
        
        y_pred = model(X) # ����
        loss = loss_fn(y_pred, y) # �ս� �Լ�
        losses.append(loss.item()) # �սǰ� ����Ʈ
        loss.backward() # ������
        
        print(f"Epoch {epoch} / {epochs} Loss : {loss}")
        optimizer.step() # ���� ��������
    
    plt.plot(range(epochs), losses)
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.show()
    

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
    optimizer = optim.Adadelta(model.parameters(), lr = 1e-2)
    return criterion, optimizer

class LinearRegressionModel (nn.Module) :
    def __init__(self) :
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1,1)
        
    def forward(self, x) :
        x = self.linear(x)
        return x
    


def DataSettingVisual() :
    #�ҽ��� �� ����
    X = torch.randn(200, 1) * 10
    y = X + 3 * torch.randn(200, 1)

    #�ð�ȭ
    plt.scatter(X.numpy(), y.numpy())
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid()
    plt.show()
    return X, y