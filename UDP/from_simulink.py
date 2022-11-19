import sys, struct
import socket
import pickle

SIZE = 1500
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((hostname, 1234))
# print(socket_1.gettimeout())
# socket_1.settimeout(5.0)
# print(socket_1.gettimeout())

counter = 0
while counter <= 10:
    msg_from_simulink = s.recvfrom(SIZE)
    data_simulink = msg_from_simulink[0]
    ip_address_simulink = msg_from_simulink[1]
    data_from_simulink = struct.unpack('d', data_simulink)
    print(data_from_simulink)
    # counter += 1

print(counter)