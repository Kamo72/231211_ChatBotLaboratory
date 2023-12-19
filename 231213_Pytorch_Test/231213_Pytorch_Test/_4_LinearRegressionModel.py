
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
    # 가중치와 편향을 가져온다.

    #w1, b1 = w[0][0].item(), b[0][0].item()
    w1, b1 = w.item(), b.item()
    x1 = np.array([-30, 30])
    y1 = w1 * x1 + b1
    # 가중치와 편향을 가져온다.
    # -30과 30을 입력했을 때의 예측값을 가져와서 두 값을 지나는 선을 그리는 듯?

    # plt.plot(x1, y1, 'r')
    # plt.scatter(X, y)
    # plt.grid()
    # plt.show()

    loss_fn, optimizer = LossAndOpt(model)
    #손실 함수, 옵티마이저
    
    #실제 학습
    epochs = 5000
    losses = []
    for epoch in range(epochs) :
        optimizer.zero_grad() # 옵티마이저의 기울기 0으로
        
        y_pred = model(X) # 전파
        loss = loss_fn(y_pred, y) # 손실 함수
        losses.append(loss.item()) # 손실값 리스트
        loss.backward() # 역전파
        
        print(f"Epoch {epoch} / {epochs} Loss : {loss}")
        optimizer.step() # 다음 스텝으로
    
    plt.plot(range(epochs), losses)
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.show()
    

def DataSetting() :
    #소스와 라벨 생성
    X = torch.randn(200, 1) * 10
    y = X + 3 * torch.randn(200, 1)

    #시각화
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
    #소스와 라벨 생성
    X = torch.randn(200, 1) * 10
    y = X + 3 * torch.randn(200, 1)

    #시각화
    plt.scatter(X.numpy(), y.numpy())
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid()
    plt.show()
    return X, y