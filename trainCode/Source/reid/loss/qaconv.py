from __future__ import division

import torch
from torch.nn import Module
from torch.nn import functional as F


class QAConv(Module):
    def __init__(self, gal_fea, loss_layer, ker_batch_size=4096, prob_batch_size=16):
        super(QAConv, self).__init__()
        self.ker_batch_size = ker_batch_size
        self.prob_batch_size = prob_batch_size
        self.num_gals = gal_fea.size(0)
        self.hw = gal_fea.size(2) * gal_fea.size(3)
        self.fea_dims = gal_fea.size(1)
        self.bn = loss_layer.bn
        self.fc = loss_layer.fc
        self.logit_bn = loss_layer.logit_bn
        kernel = F.normalize(gal_fea)  # [g, d, h, w]
        kernel = kernel.permute([0, 2, 3, 1])  # [g, h, w, d]
        kernel = kernel.contiguous().view(self.num_gals, self.hw, self.fea_dims, 1, 1)
        self.register_buffer('kernel', kernel)  # [g, hw, d, 1, 1]

    def forward(self, prob_fea):
        num_probs = prob_fea.size(0)
        prob_f = F.normalize(prob_fea).contiguous()  # [p, d, h, w]
        score = torch.zeros(num_probs, self.num_gals).to(prob_fea.device)

        for i in range(0, num_probs, self.prob_batch_size):
            j = min(i + self.prob_batch_size, num_probs)
            if self.ker_batch_size < self.num_gals:
                score_ = torch.zeros(j - i, self.num_gals, 2 * self.hw).to(prob_fea.device)
                for k in range(0, self.num_gals, self.ker_batch_size):
                    k2 = min(k + self.ker_batch_size, self.num_gals)
                    kernel = self.kernel[k: k2]
                    kernel = kernel.view(-1, self.fea_dims, 1, 1)
                    s = F.conv2d(prob_f[i: j, :, :, :], kernel)  # [j - i, (k2-k)*hw, h, w]
                    s = s.view(j - i, k2 - k, self.hw, self.hw)
                    score_[:, k: k2, :] = torch.cat((s.max(dim=2)[0], s.max(dim=3)[0]), dim=-1)  # [j - i, k2 - k, 2 * hw]
            else:
                score_ = F.conv2d(prob_f[i: j, :, :, :], self.kernel.view(-1, self.fea_dims, 1, 1))  # [j - i, ghw, h, w]
                score_ = score_.view(j - i, self.num_gals, self.hw, self.hw)
                score_ = torch.cat((score_.max(dim=2)[0], score_.max(dim=3)[0]), dim=-1)
            score_ = score_.view(-1, 1, self.num_gals * 2 * self.hw)
            score_ = self.bn(score_).view(-1, 2 * self.hw)
            score[i: j, :] = self.fc(score_).view(-1, self.num_gals)

        score = self.logit_bn(score.unsqueeze(1)).view(num_probs, self.num_gals)
        score = torch.sigmoid(score / 10.)

        return score
