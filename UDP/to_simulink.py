import socket
import struct
import numpy as np
import codecs
import pickle
from sys import getsizeof
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


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

address_port_1021 = (f'{ip_address}', 1021)
address_port_1022 = (f'{ip_address}', 1022)
address_port_1023 = (f'{ip_address}', 1023)

socket_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# socket_1.bind((hostname, 1234))
counter = 0
# while counter <= 0:

# msg_port1021 = weights_and_bias('layer1').numpy()
# msg_port1022 = weights_and_bias('layer2').numpy()
msg_port1023 = weights_and_bias('layer3').numpy()

msg_port1021 = np.arange(0, 572).reshape(22, 26)
msg_port1022 = np.arange(0, 650).reshape(26, 25)
# msg_port1023 = np.arange(0, 78).reshape(26, 3)

# msg = bytes('Hello! Welcome to my server', "utf-8")
# msg = bytes('Hello! ', "utf-8")
# msg = bytes('bye', 'utf-8')

socket_1.sendto(msg_port1021, address_port_1021)
socket_2.sendto(msg_port1022, address_port_1022)
socket_3.sendto(msg_port1023, address_port_1023)

print(f'The size of message to port 1021 is {getsizeof(msg_port1021)} Bytes')
print(f'The size of message to port 1022 is {getsizeof(msg_port1022)} Bytes')
print(f'The size of message to port 1023 is {getsizeof(msg_port1023)} Bytes')
print("\n +++++++++++++++++ \n ")

counter += 1
# socket_1.sendto(msg, ('131.234.124.101', 25000))
