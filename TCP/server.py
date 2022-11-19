import socket
import pickle
import numpy as np

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
hostname = socket.gethostname()
IPaddress = socket.gethostbyname(hostname)
# it specifies the number of unaccepted connections that the system will allow
# before refusing new connections.
s.listen(5)

while True:
    client_socket, client_address = s.accept()
    print(f"Connection from {client_socket} is established!")

    obj = np.arange(0, 100).reshape(10, 10)
    msg = pickle.dumps(obj)

    #  The length of biggest message should not be longer than 1 billion characters
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", "utf-8") + msg

    client_socket.send(msg)
