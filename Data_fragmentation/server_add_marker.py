import socket
import struct
import math
import numpy as np

data = np.arange(0, 15)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
socket_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def fragmentation(packet: np.ndarray, frag_max_size: int):
    num_frags = math.ceil(packet.nbytes / frag_max_size)
    if packet.nbytes % frag_max_size != 0:
        raise Exception("Padding needed")
    fragments = []
    offset = 0
    count = np.array([0])
    packet_in_bytes = bytes(packet)
    for i, j in enumerate(packet_in_bytes):
        if (i+1) % frag_max_size == 0:
            fragment = np.frombuffer(bytes(count) + bytes(np.array([num_frags])) + packet_in_bytes[offset:i+1],
                                     dtype=packet.dtype)
            print(f"Fragment : {fragment}")
            offset = i + 1
            fragments.append(fragment)
            count += 1
    print(f"Number of Fragements: {num_frags}")
    return fragments, num_frags


def send(msg, socket_name, port=None, max_size: int = 10):
    """ msg: The data-packet to be sent.
        port: The port to be used
        max_size: Maximum size(in bytes) of packet before fragmentation"""
    num_of_frag = 0
    msg_bytes = bytes(msg)
    print(f"The message size is {msg.nbytes} bytes and maximum size of packet is {max_size}")
    # Check the size of msg
    if msg.nbytes > max_size:
        # Convert the message into binary
        print("Fragmentation needed.")
        packet_fragments, num_of_frag = fragmentation(msg, frag_max_size=16)
        # raise Exception(f"Packet size {msg.nbytes} bytes is too big.")
    else:
        packet_fragments = msg

    # Todo: Print shape of final message
    row = len(packet_fragments)
    if isinstance(packet_fragments[0], np.ndarray):
        col = len(packet_fragments[0])
        print(f"Shape of packet in fragments: {row} x {col}")
        return print(f"Message of size {msg.nbytes} was sent to port {port} in {num_of_frag} "
                     f"Fragments.")
    return print(f"Message of size {msg.nbytes} was sent to port {port} without Fragmentation ")


if __name__ == "__main__":
    print(send(data, socket_name=socket_1, port=1234, max_size=16))
