import csv
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

file = open('time.csv', 'r')

csvreader = csv.reader(file)
A = []
for i, row in enumerate(csvreader):
    A.append(np.datetime64(datetime.strptime(row[0], '%H:%M:%S:%f')))

plt.plot(np.diff(A))
plt.ylim(0, 10000)
plt.show()


