import socket
import struct
import logging
import numpy as np
import threading
import queue

BUFFERSIZE = 1024
hostname = socket.gethostname()
port = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((hostname, port))
s.settimeout(20)

logging.basicConfig(datefmt="%H:%M:%S",
                    filename='data_mp_1024_1x.csv',
                    format='%(message)s',
                    level=logging.INFO,
                    )


def writing_on_buffer(socket_name, q):
    for i in range(int(1e7)):
        msg = socket_name.recvfrom(BUFFERSIZE)
        q.put(msg[0])
        # data = msg[0]
        # data_unpack = struct.unpack('dddd', data)
        # q.put(np.array(data_unpack[0]))


def logging_csv(q):
    while not q.empty():
        data = q.get()
        data_unpack = struct.unpack('d', data)
        logging.info(np.array(data_unpack[0]))
        # logging.info(q.get())


if __name__ == "__main__":
    q = queue.Queue()

    thread1 = threading.Thread(target=writing_on_buffer, args=(s, q,))
    thread2 = threading.Thread(target=logging_csv, args=(q,))
    thread1.start()
    thread1.join()
    thread2.start()
    print("Thread 2")
