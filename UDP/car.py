from utility.NN_weights import weights_and_bias
import torch
import numpy as np


w = weights_and_bias('layer1').numpy()

print(w.shape)
w1 = np.transpose(w)
print(w1.shape)

