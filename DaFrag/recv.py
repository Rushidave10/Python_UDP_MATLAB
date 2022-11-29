import socket
import warnings
from itertools import chain
import numpy as np
import time
import sys

host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

local_port = 1234
buffer_size = int(10e+6)

socket_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_recv.bind((ip_address, local_port))

print("Up and listening")
data_buffer = []
save = False

def unpad(packet):
    for k, i in enumerate(packet):
        if (i[0]+1) == i[1]:
            last_frag = i
            x = slice(0, last_frag[2] - 1)
            unpadded_array = last_frag[x]
            packet[k] = unpadded_array
    return packet


def check(packet, nfrag):
    # Check if no. of rows equal no. of fragments.
    if len(packet) == nfrag:
        print("Complete message recvd")
        packet = unpad(packet)
        return packet
    else:
        warnings.warn("Data Lost")
        pass


def reassemble(packet):
    new_packet = []
    seq_register = [i[0] for i in packet]
    sort_seq_regr = np.sort(seq_register)
    for k in sort_seq_regr:
        for i, j in enumerate(packet):
            if j[0] == k:
                new_packet[i] = j

    return new_packet


def extract_raw(packet):
    for k, i in enumerate(packet):
        x = slice(3, len(i))
        raw_data = i[x]
        packet[k] = raw_data
    return packet


while True:
    recv_msg = socket_recv.recvfrom(buffer_size)
    data = recv_msg[0]
    data_decoded = np.frombuffer(data, dtype=np.int32)
    seq_byte, nfrag_byte = data_decoded[0], data_decoded[1]
    data_buffer.append(data_decoded)
    if (seq_byte + 1) == nfrag_byte and len(data_buffer) == nfrag_byte:
        #  un-padding and checking for data loss.
        og_msg = check(data_buffer, nfrag=nfrag_byte)

        #  Extract original data
        og_msg = extract_raw(og_msg)


        #  Converting into 1D vector.
        oneD_msg = np.asarray(list(chain.from_iterable([j for j in og_msg])))
        print(oneD_msg)
        print(f"The length of message is {oneD_msg.size} and size is {oneD_msg.nbytes} Bytes")

        if save:
            t = time.localtime()
            timestamp = time.strftime('%b-%d-%Y_%H%M', t)
            BACKUP_NAME = ("backup-" + timestamp)
            np.save(BACKUP_NAME, oneD_msg)
        data_buffer.clear()
        sys.exit()
