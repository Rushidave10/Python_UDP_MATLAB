import sys, struct
import socket
import pickle
import numpy as np

SIZE = 1500
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
port = 1111
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((hostname, 1111))
# print(socket_1.gettimeout())
# socket_1.settimeout(5.0)
# print(socket_1.gettimeout())

counter = 0

while True:
    input("Press Enter to continue")
    print('Sending data')
    update = np.array([counter], dtype=np.double)
    s.sendto(update, ('131.234.124.101', 1112))
    print(counter)

    print('Waiting for message-----')
    msg_from_simulink = s.recvfrom(SIZE)
    data_simulink = msg_from_simulink[0]
    ip_address_simulink = msg_from_simulink[1]
    data_from_simulink = struct.unpack('d', data_simulink)
    print(data_from_simulink)
    print("Got it")

    update = np.squeeze(data_from_simulink)
    if update:
        print('True')
    counter += 1


