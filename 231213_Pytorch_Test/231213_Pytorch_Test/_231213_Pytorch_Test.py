import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

import _0_Prologue
import _1_TestModel
import _2_Visualize
import _3_ModelAndModule
import _4_LinearRegressionModel

if __name__ == '__main__':
    #_0_Prologue.TestWhole()
    #_1_TestModel.TestWhole()
    #_2_Visualize.TestMaxPool2dDisplay()
    #_3_ModelAndModule.TestModelView()
    # _3_ModelAndModule.TestMetrics()
    # _3_ModelAndModule.TestMetricsMultiple()
    _4_LinearRegressionModel.TestLinear()