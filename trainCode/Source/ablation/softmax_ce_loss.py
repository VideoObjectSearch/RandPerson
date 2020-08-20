from __future__ import division

import torch
from torch import nn
from torch.nn import Module
from torch.nn import functional as F


class SoftmaxCELoss(Module):
    def __init__(self, num_classes, num_features, dropout=0.5):
        super(SoftmaxCELoss, self).__init__()
        self.num_classes = num_classes
        self.num_features = num_features
        self.dropout = dropout
        self.classifier = nn.Linear(self.num_features, self.num_classes, bias=False)
        if self.dropout > 0:
            self.drop = nn.Dropout(self.dropout)
        self.reset_parameters()

    def reset_parameters(self):
        self.classifier.reset_parameters()

    def _check_input_dim(self, input):
        if input.dim() != 2:
            raise ValueError('expected 2D input (got {}D input)'
                             .format(input.dim()))

    def forward(self, feature, target):
        self._check_input_dim(feature)

        x = feature
        if self.dropout > 0:
            x = self.drop(x)
        logits = self.classifier(x)

        loss = F.cross_entropy(logits, target, reduction='none')

        with torch.no_grad():
            _, preds = torch.max(logits, 1)
            acc = (preds == target).float()

        return loss, acc
