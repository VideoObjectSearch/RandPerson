from __future__ import print_function, absolute_import
import time
import sys

import torch
from torch.autograd import Variable
from .utils.meters import AverageMeter


class BaseTrainer(object):
    def __init__(self, model, criterion):
        super(BaseTrainer, self).__init__()
        self.model = model
        self.criterion = criterion

    def train(self, epoch, endepoch, output_dir, data_loader, optimizer, print_freq=1):
        self.model.train()

        batch_time = AverageMeter()
        data_time = AverageMeter()
        losses = AverageMeter()
        precisions = AverageMeter()
        end = time.time()
        for i, inputs in enumerate(data_loader):
            data_time.update(time.time() - end)
            inputs, targets, piclist = self._parse_data(inputs)

            loss, prec1, acc = self._forward(inputs, targets)
            losses.update(loss.item(), targets.size(0))
            precisions.update(prec1, targets.size(0))
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            batch_time.update(time.time() - end)
            end = time.time()
            if (i + 1) % print_freq == 0:
                print('Epoch: [{}][{}/{}]\t'
                      'Time {:.3f} ({:.3f})\t'
                      'Data {:.3f} ({:.3f})\t'
                      'Loss {:.3f} ({:.3f})\t'
                      'Prec {:.2%} ({:.2%})\t'
                      .format(epoch, i + 1, len(data_loader),
                              batch_time.val, batch_time.avg,
                              data_time.val, data_time.avg,
                              losses.val, losses.avg,
                              precisions.val, precisions.avg), end='\r', file=sys.stdout.console)
            if epoch >= endepoch -1:
                f = open(sys.path[0].replace('Source/ablation',"")+ output_dir.replace('../../','') + '/pic.txt', 'a')
                for i in range(0, 32):
                    if not acc[i]:
                        f.write(piclist[i]+'\n')
                        # print(piclist[i])
        return losses.avg, precisions.avg

    def _parse_data(self, inputs):
        raise NotImplementedError

    def _forward(self, inputs, targets):
        raise NotImplementedError


class Trainer(BaseTrainer):
    def _parse_data(self, inputs):
        imgs, piclist, pids, _ = inputs
        inputs = [Variable(imgs)]
        targets = Variable(pids.cuda())
        return inputs, targets, piclist

    def _forward(self, inputs, targets):
        feature = self.model(*inputs)
        loss, acc = self.criterion(feature, targets)
        loss = torch.mean(loss)
        prec = torch.mean(acc)
        return loss, prec, acc
