import sys, struct
import socket
import pickle
import numpy as np
import matplotlib.pyplot as plt

SIZE = 1500
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
port = 1111
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((hostname, 1111))
# print(socket_send.gettimeout())
# socket_send.settimeout(5.0)
# print(socket_send.gettimeout())
s.settimeout(10)
counter = 0

for i in range(1000):
    msg_from_simulink = s.recvfrom(SIZE)
    data_simulink = msg_from_simulink[0]
    ip_address_simulink = msg_from_simulink[1]
    data_from_simulink = struct.unpack('d', data_simulink)
    plt.scatter(i, data_from_simulink)
    plt.pause(0.001)
plt.show()
