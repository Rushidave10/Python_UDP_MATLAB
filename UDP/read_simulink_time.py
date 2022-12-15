import matplotlib.pyplot as plt
import numpy as np
import ast
import csv

x, x_1, x_2, x_3, x_4 = ([], [], [], [], [])
y, y_1, y_2, y_3, y_4 = ([], [], [], [], [])
A = np.arange(0, 20, 0.0001)
B = np.arange(0, 20, 0.001)
with open('data_mp_1024_1x.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(plots):
        x.append(i)
        y.append(ast.literal_eval(row[0]))

with open('data_mp_1024_2x.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(plots):
        x_2.append(i)
        y_2.append(ast.literal_eval(row[0]))

with open('data_mp_1024_3x.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(plots):
        x_3.append(i)
        y_3.append(ast.literal_eval(row[0]))

with open('data_mp_1024_4x.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(plots):
        x_4.append(i)
        y_4.append(ast.literal_eval(row[0]))

plt.step(x, y, where='pre', label='1024_bytes_1x')
plt.step(x_2, y_2, where='pre', label='1024_bytes_2x')
plt.step(x_3, y_3, where='pre', label='1024_bytes_3x')
plt.step(x_4, y_4, where='pre', label='1024_bytes_4x')
plt.plot(A, color='grey', alpha=0.3, label='True_10KHz')

# plt.xscale('log')
# plt.yscale('log')
plt.xlabel('nth sample')
plt.ylabel('sample time(sec)')
plt.grid(True)
# plt.xlim(2000, 20000)
plt.legend()
plt.show()
