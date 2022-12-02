import socket
import struct
import logging
import matplotlib.pyplot as plt
import numpy as np
import time

SIZE = 1500
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
port = 1111
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((hostname, 1111))
# print(socket_send.gettimeout())
# socket_send.settimeout(5.0)
# print(socket_send.gettimeout())
s.settimeout(20)
counter = 0
# logging.basicConfig(datefmt="%H:%M:%S",
#                     filename='data.log',
#                     format='%(asctime)s:%(msecs)05d %(message)s',
#                     level=logging.INFO,
#                     )

logging.basicConfig(datefmt="%H:%M:%S",
                    filename='time.csv',
                    format='%(asctime)s:%(msecs)03d',
                    level=logging.INFO,
                    )

for i in range(int(1e6)):
    msg_from_simulink = s.recvfrom(SIZE)
    data_simulink = msg_from_simulink[0]
    ip_address_simulink = msg_from_simulink[1]
    data_from_simulink = struct.unpack('d', data_simulink)
    data_from_simulink = np.array(data_from_simulink)
    logging.info(data_from_simulink)
