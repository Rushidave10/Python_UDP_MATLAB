import socket
import struct
import math
import numpy as np

data = np.arange(0, 64)


def fragmentation(packet: np.ndarray, frag_max_size: int = 64):
    num_frags = math.ceil(packet.nbytes / frag_max_size)
    fragments = []
    offset = 0
    count = np.array([0])
    packet_in_bytes = bytes(packet)
    # print(packet_in_bytes)
    for i, j in enumerate(packet_in_bytes):
        if i % frag_max_size == frag_max_size - 1:
            print(packet_in_bytes[offset:i+1])
            fragment = np.frombuffer(bytes(count) + packet_in_bytes[offset:i+1], dtype=packet.dtype)
            print(f"Fragment : {fragment}")
            offset = i+1
            fragments.append(fragment)
            count += 1
    print(f"Number of Fragements: {num_frags}")
    return fragments


def send(msg, port=None, max_size: int = 10):
    """ msg: The data-packet to be sent.
        port: The port to be used
        max_size: Maximum size(in bytes) of packet before fragmentation"""
    msg_bytes = bytes(msg)
    print(f"The message size is {msg.nbytes} bytes")
    # Check the size of msg
    if msg.nbytes > max_size:
        # Convert the message into binary
        packet_fragments = fragmentation(msg)
        # raise Exception(f"Packet size {msg.nbytes} bytes is too big.")
    else:
        packet_fragments = msg
    return packet_fragments


if __name__ == "__main__":
    print(send(data, 8))
