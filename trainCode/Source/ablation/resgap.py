from __future__ import absolute_import

import torch
from torch import nn
from torch.nn import functional as F
import torchvision

fea_dims = {'layer2': 512, 'layer3': 1024, 'layer4': 2048}


class ResNet(nn.Module):
    __factory = {
        18: torchvision.models.resnet18,
        34: torchvision.models.resnet34,
        50: torchvision.models.resnet50,
        101: torchvision.models.resnet101,
        152: torchvision.models.resnet152,
    }

    def __init__(self, depth, final_layer='layer3', neck=128, pretrained=True):
        super(ResNet, self).__init__()

        self.depth = depth
        self.final_layer = final_layer
        self.neck = neck
        self.pretrained = pretrained

        # Construct base (pretrained) resnet
        if depth not in ResNet.__factory:
            raise KeyError("Unsupported depth:", depth)
        self.base = ResNet.__factory[depth](pretrained=pretrained)

        out_planes = fea_dims[final_layer]

        if neck > 0:
            self.neck_conv = nn.Conv2d(out_planes, neck, kernel_size=1)
            out_planes = neck
            self.neck_bn = nn.BatchNorm2d(out_planes)

        self.global_avg_pool = nn.AdaptiveAvgPool2d((1, 1))
        self.pool_bn = nn.BatchNorm1d(out_planes)

        self.num_features = out_planes

    def forward(self, inputs, do_test=False):
        x = inputs
        for name, module in self.base._modules.items():
            x = module(x)
            if name == self.final_layer:
                break

        if self.neck > 0:
            x = self.neck_conv(x)
            x = self.neck_bn(x)

        x = self.global_avg_pool(x)
        x.squeeze_()
        x = self.pool_bn(x)

        if do_test:
            x = F.normalize(x)

        return x


def resnet18(**kwargs):
    return ResNet(18, **kwargs)


def resnet34(**kwargs):
    return ResNet(34, **kwargs)


def resnet50(**kwargs):
    return ResNet(50, **kwargs)


def resnet101(**kwargs):
    return ResNet(101, **kwargs)


def resnet152(**kwargs):
    return ResNet(152, **kwargs)


__factory = {
    'resnet18': resnet18,
    'resnet34': resnet34,
    'resnet50': resnet50,
    'resnet101': resnet101,
    'resnet152': resnet152,
}


def names():
    return sorted(__factory.keys())


def create(name, *args, **kwargs):
    """
    Create a model instance.

    Parameters
    ----------
    name : str
        Model name. Can be one of 'inception', 'resnet18', 'resnet34',
        'resnet50', 'resnet101', and 'resnet152'.
    pretrained : bool, optional
        Only applied for 'resnet*' models. If True, will use ImageNet pretrained
        model. Default: True
    cut_at_pooling : bool, optional
        If True, will cut the model before the last global pooling layer and
        ignore the remaining kwargs. Default: False
    num_features : int, optional
        If positive, will append a Linear layer after the global pooling layer,
        with this number of output units, followed by a BatchNorm layer.
        Otherwise these layers will not be appended. Default: 256 for
        'inception', 0 for 'resnet*'
    norm : bool, optional
        If True, will normalize the feature to be unit L2-norm for each sample.
        Otherwise will append a ReLU layer after the above Linear layer if
        num_features > 0. Default: False
    dropout : float, optional
        If positive, will append a Dropout layer with this dropout rate.
        Default: 0
    num_classes : int, optional
        If positive, will append a Linear layer at the end as the classifier
        with this number of output units. Default: 0
    """
    if name not in __factory:
        raise KeyError("Unknown model:", name)
    return __factory[name](*args, **kwargs)
