import socket
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    complete_msg = b''
    new_msg = True
    while True:

        msg = s.recv(16)
        if new_msg:
            # print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        complete_msg += msg

        if len(complete_msg) - HEADERSIZE == msglen:
            print("full msg recvd")
            # print(complete_msg[HEADERSIZE:])

            d = pickle.loads(complete_msg[HEADERSIZE:])
            print(d)

            new_msg = True
            full_msg = b''
    print(complete_msg)

