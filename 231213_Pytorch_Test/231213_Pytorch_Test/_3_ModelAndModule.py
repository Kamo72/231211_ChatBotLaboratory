from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms
from torchvision import datasets
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchmetrics


def TestModelView() :
    model = MyModel();
    print(list(model.children()))
    
    print(list(model.modules()))


class MyModel(nn.Module) :
	def __init__(self) :
		super(MyModel, self).__init__()
		self.layer1 = nn.Sequential(
			nn.Conv2d(3, 64, 5),
			nn.ReLU(True),
			nn.MaxPool2d(2),
		)
		self.layer2 = nn.Sequential(
			nn.Conv2d(64, 30, 5),
			nn.ReLU(True),
			nn.MaxPool2d(2),
		)
		self.layer3 = nn.Sequential(
			nn.Linear(30 * 5 * 5, 10, True),
			nn.ReLU(True)
		)
	def forwar(self, x) :
		x = self.layer1(x)
		x = self.layer2(x)
		x = x.view(x.shape[0], -1)
		x = self.layer3(x)
		return x


def TestMetrics():
	preds = torch.randn(10, 5).softmax(dim =-1)
	target = torch.randint(5, (10, ))
	print(preds, target)
	
	acc = torchmetrics.functional.accuracy(preds, target, task="multiclass", num_classes=5)
	print(acc)
	
def TestMetricsMultiple() :
	metric = torchmetrics.Accuracy(task='multiclass', num_classes=5)

	n_batches = 10
	for i in range(n_batches):
		preds = torch.randn(10, 5).softmax(dim = 1)
		target = torch.randint(5 , (10, ))

		acc =metric(preds, target)
		print(acc)

	acc = metric.compute()
	print(acc)