from __future__ import division

import torch
from torch import nn
from torch.nn import Module
from torch.nn import functional as F


class QAConvLoss(Module):
    def __init__(self, num_classes, num_features, height, width, mem_batch_size=1000):
        super(QAConvLoss, self).__init__()
        self.num_classes = num_classes
        self.num_features = num_features
        self.height = height
        self.width = width
        self.mem_batch_size = mem_batch_size
        self.register_buffer('class_memory', torch.zeros(num_classes, num_features, height, width))
        self.bn = nn.BatchNorm1d(1)
        self.fc = nn.Linear(self.height * self.width * 2, 1)
        self.logit_bn = nn.BatchNorm1d(1)
        self.reset_parameters()

    def reset_running_stats(self):
        self.class_memory.zero_()

    def reset_parameters(self):
        self.reset_running_stats()

    def _check_input_dim(self, input):
        if input.dim() != 4:
            raise ValueError('expected 4D input (got {}D input)'.format(input.dim()))

    def forward(self, feature, target):
        self._check_input_dim(feature)

        fea = F.normalize(feature)
        fea = fea.permute([0, 2, 3, 1])  # [b, h, w, d]
        kernel = fea.contiguous().view(-1, self.num_features, 1, 1)  # [bhw, d, 1, 1]
        class_memory = F.normalize(self.class_memory)  # [c, d, h, w]

        hw = self.height * self.width
        batch_size = target.size(0)

        if self.mem_batch_size < self.num_classes:
            score = torch.zeros(self.num_classes, batch_size, 2 * hw).to(feature.device)
            for i in range(0, self.num_classes, self.mem_batch_size):
                j = min(i + self.mem_batch_size, self.num_classes)
                s = F.conv2d(class_memory[i: j, :, :, :], kernel)  # [m, bhw, h, w]
                s = s.view(-1, batch_size, hw, hw)
                score[i: j, :, :] = torch.cat((s.max(dim=2)[0], s.max(dim=3)[0]), dim=-1)  # [m, b, 2 * hw]
        else:
            score = F.conv2d(class_memory, kernel)  # [c, bhw, h, w]
            score = score.view(self.num_classes, batch_size, hw, hw)
            score = torch.cat((score.max(dim=2)[0], score.max(dim=3)[0]), dim=-1)

        score = score.view(self.num_classes, 1, batch_size * 2 * hw)
        score = self.bn(score).view(self.num_classes * batch_size, 2 * hw)
        score = self.fc(score).view(self.num_classes, batch_size).t()
        score = self.logit_bn(score.unsqueeze(1)).squeeze()

        target1 = target.unsqueeze(1)
        onehot_labels = torch.zeros_like(score).scatter(1, target1, 1)
        loss = F.binary_cross_entropy_with_logits(score, onehot_labels, reduction='none')
        prob = score.sigmoid()
        weight = torch.pow(torch.where(onehot_labels.byte(), 1. - prob, prob), 2.)
        loss = loss * weight
        loss = loss.sum(-1)

        with torch.no_grad():
            _, preds = torch.max(score, 1)
            acc = (preds == target).float()
            self.class_memory[target] = feature

        return loss, acc
