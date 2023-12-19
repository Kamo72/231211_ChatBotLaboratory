import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.modules import linear
from torch.utils import data
import torchmetrics
from torch.utils.data import Dataset, DataLoader
from torch import optim

import transformers
from transformers import pipeline


def Test ():
    classifier = pipeline("sentiment-analysis")
    print(classifier(
        [
            "I've been waiting for a HuggingFace course my whole life.",
            "I hate this so much!",
        ]
    ))