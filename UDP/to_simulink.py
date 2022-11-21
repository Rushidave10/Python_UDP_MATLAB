import socket
import struct
import sched, time
import numpy as np
from sys import getsizeof
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


'''Need when acting as server'''
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

address_port_1021 = (f'{ip_address}', 1021)
address_port_1022 = (f'{ip_address}', 1022)
address_port_1023 = (f'{ip_address}', 1023)

'''Need when receiving'''
buffer_size = 650000

socket_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_update = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_update.bind((hostname, 1020))
counter = 0

"""Actual Neural Networks weights from pytorch based model"""
msg_port1021 = weights_and_bias('layer1').numpy().astype('longdouble')
msg_port1022 = weights_and_bias('layer2').numpy().astype('longdouble')
msg_port1023 = weights_and_bias('layer3').numpy().astype('longdouble')

""" To check the sequence of the data that is delivered"""
# msg_port1021 = np.arange(0, 572, dtype=np.double).reshape(22, 26)
# msg_port1022 = np.arange(0, 650, dtype=np.double).reshape(26, 25)
# msg_port1023 = np.arange(0, 78, dtype=np.double).reshape(26, 3)


for i in range(11):
    # input('Press Enter to continue')
    print('Sending Data....to simulink ---->')
    socket_1.sendto(msg_port1021, address_port_1021)
    socket_2.sendto(msg_port1022, address_port_1022)
    socket_3.sendto(msg_port1023, address_port_1023)

    print(f'The size of message to port 1021 is {getsizeof(msg_port1021)} Bytes')
    print(f'The size of message to port 1022 is {getsizeof(msg_port1022)} Bytes')
    print(f'The size of message to port 1023 is {getsizeof(msg_port1023)} Bytes')
    print("\n +++++++++++++++++ \n ")

    msg_from_simulink = socket_update.recvfrom(buffer_size)
    update_flag = struct.unpack('d', msg_from_simulink[0])
    print(type(update_flag))
    print('The Update flag is :', update_flag)
    counter += 1
    print('Counter:', counter)
    ip_address_simulink = msg_from_simulink[1]

