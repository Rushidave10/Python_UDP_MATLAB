import logging
import socket
import struct
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print('Error')
    sys.exit()

hostname = socket.gethostname()
port = 6666
SIZE = 8
s.bind(('localhost', port))
s.settimeout(5)
s.listen(5)
conn, addr = s.accept()

logging.basicConfig(datefmt="%H:%M:%S",
                    filename='mt_1x_8_byte.csv',
                    format='%(message)s',
                    level=logging.INFO
                    )
#
# def writing_on_buffer(conn_name, q_name):
#     while True:
#         msg = conn_name.recv(SIZE)
while True:
    msg = conn.recv(SIZE)
    print(struct.unpack('d', msg))
