
from asyncio.windows_events import NULL
from email.mime import image
from tkinter import W
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.modules import linear
from torch.utils import data
import torchmetrics
from torch.utils.data import Dataset, DataLoader
from torch import optim

import numpy as np

import torchvision.transforms as transforms
from torchvision import datasets
import matplotlib.pyplot as plt


def FashionTest() :
    
    labels_map = {
        0 : "T-shirt"    ,
        1 : "Trouser"    ,
        2 : "Pullover"    ,
        3 : "Dress"    ,
        4 : "Coat"    ,
        5 : "Sandal"    ,
        6 : "Shirt"    ,
        7 : "Sneaker"    ,
        8 : "Bag"    ,
        9 : "Ankle Boot"    ,
    }


    batch_size = 128
    def DataSetting () : 
        #Ʈ������
        transform = transforms.Compose([transforms.ToTensor(),
                                        transforms.Normalize((0.5, ), (0.5, ))])
    
        #�����ͼ� �ٿ�
        trainset = datasets.FashionMNIST(root = '/content/',
                                         train=True, download = True,
                                         transform=transform)
        testset = datasets.FashionMNIST(root = '/content/',
                                         train=False, download = True,
                                         transform=transform)
    
        #������ �δ�
        train_loader = DataLoader(trainset, batch_size = batch_size, shuffle =True, num_workers=10)
        test_loader = DataLoader(testset, batch_size = batch_size, shuffle =False, num_workers=10)

        images, labels = next(iter(train_loader))
        print(images.shape, labels.shape)
    
        # figure = plt.figure(figsize=(12,12))
        # cols, rows = 4, 4
        # for i in range(1, cols * rows+1) :
        #     image =images[i].squeeze()
        #     label_idx = labels[i].item()
        #     label = labels_map[label_idx]
        
        #     figure.add_subplot(rows, cols, i)
        #     plt.title(label)
        #     plt.axis('off')
        #     plt.imshow(image, cmap = 'gray')
        # plt.show()
        
        return train_loader, test_loader
    train_ds, test_ds = DataSetting()
    
    class FashionModel (nn.Module) :
        def __init__(self) :
            super(FashionModel, self).__init__()
            self.layers =  nn.Sequential(
                nn.Conv2d(
		            in_channels = 1,
	                out_channels = 10,
	                kernel_size=5,
	                stride=1,
		            padding=5),
                nn.Flatten(3, 1), # 10 28 28
                nn.Linear(7840, 1),
                )
        def forward(self, x) :
            x = self.layers(x)
            return x    
    model = FashionModel()

    def LossAndOpti(model) :
        loss_fn = nn.MSELoss()
        optimizer = optim.SGD(model.parameters(), lr = 1e-4)
        return loss_fn, optimizer
    loss_fn, optimizer = LossAndOpti(model)
    


    epochs = 5000
    losses = []
    for epoch in range(epochs) :
        for batch in train_ds:
            inputs, labels = batch
            
            for inputV in inputs :
            
                y_pred = model(inputV) # ����
                loss = loss_fn(y_pred, inputs) # �ս� �Լ�
                losses.append(loss.item()) # �սǰ� ����Ʈ
                loss.backward() # ������
                
                print(f"Epoch {epoch} / {epochs} Loss : {loss}")
                optimizer.step() # ���� ��������
                
                
                optimizer.zero_grad() # ��Ƽ�������� ���� 0����
                
                y_pred = model(inputV) # ����
                loss = loss_fn(y_pred, inputs) # �ս� �Լ�
                losses.append(loss.item()) # �սǰ� ����Ʈ
                loss.backward() # ������
                
                print(f"Epoch {epoch} / {epochs} Loss : {loss}")
                optimizer.step() # ���� ��������
    
    
        
    















