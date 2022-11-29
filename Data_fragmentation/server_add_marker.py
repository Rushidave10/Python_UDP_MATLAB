import socket
import struct
import math
import warnings
import numpy as np

data = np.arange(0, 50)
print(data)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
socket_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def fragmentation(packet: np.ndarray, frag_max_size: int):
    num_frags = math.ceil(packet.nbytes / frag_max_size)
    pad_here = packet.nbytes % frag_max_size
    if pad_here != 0:
        warnings.warn("Padding needed")
        pad_in_np = (frag_max_size-pad_here)/4  # One element in np.array is 4 bytes.
        packet = np.pad(packet, (0, int(pad_in_np)), mode='constant', constant_values=np.asarray(0))
    fragments = []
    offset = 0
    count = np.array([0])
    packet_in_bytes = bytes(packet)
    for i, j in enumerate(packet_in_bytes):
        if (i + 1) % frag_max_size == 0:
            fragment = np.frombuffer(bytes(count) + bytes(np.array([num_frags])) + packet_in_bytes[offset:i + 1],
                                     dtype=packet.dtype)
            print(f"Fragment : {fragment}")
            offset = i + 1
            fragments.append(fragment)
            count += 1
    print(f"Number of Fragements: {num_frags}")
    return fragments, num_frags


def send(msg, socket_name, max_size: int, port=None):
    """ msg: The data-packet to be sent.
        port: The port to be used
        max_size: Maximum size(in bytes) of packet before fragmentation"""
    num_of_frag = 0
    msg_bytes = bytes(msg)
    print(f"The message size is {msg.nbytes} bytes")
    # Check the size of msg
    if msg.nbytes > max_size:
        # Convert the message into binary
        print("Fragmentation needed.")
        packet_fragments, num_of_frag = fragmentation(msg, frag_max_size=max_size)
        # raise Exception(f"Packet size {msg.nbytes} bytes is too big.")
    else:
        packet_fragments = msg
    for i in range(num_of_frag):
        socket_name.sendto(packet_fragments[i], (ip_address, port))

    # Print shape of final message
    row = len(packet_fragments)
    if isinstance(packet_fragments[0], np.ndarray):
        col = len(packet_fragments[0])
        print(f"Shape of packet in fragments: {row} x {col}")
        return print(f"Message of size {np.asarray(packet_fragments).nbytes} was sent to port {port} in {num_of_frag} "
                     f"Fragments.")
    return print(f"Message of size {packet_fragments.nbytes} bytes was sent to port {port} without Fragmentation ")


if __name__ == "__main__":
    max_size = 32
    print(f"Maximum size allowed for packet: {max_size} Bytes")
    send(data, socket_name=socket_1, port=1234, max_size=max_size)
