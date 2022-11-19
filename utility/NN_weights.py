import torch
import torch.nn as nn


class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()

        self.layer1 = nn.Linear(22, 26)
        self.layer2 = nn.Linear(26, 25)
        self.layer3 = nn.Linear(25, 3)

    def forward(self, x):
        output = self.layer1(x)
        output = self.layer2(output)
        output = self.layer3(output)

        return output


model = NeuralNet()


#
# for name, param in model.named_parameters():
#     print('name:', name)
#     print(type(param))
#     print('param.shape:', param.shape)
#     print('param.requires_grad', param.requires_grad)
#     print('=====')
# print(model.state_dict()['layer1.weight'].size())
def weights_and_bias(layer, bias=False):
    """ Get weights of the layer and bias"""
    if bias:
        return model.state_dict()[f'{layer}.bias']
    return model.state_dict()[f'{layer}.weight']
