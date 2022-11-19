import numpy as np


def calculate_size_in_bytes(a):
    return a.nbytes


A = np.arange(1, 625)
print(calculate_size_in_bytes(A))
