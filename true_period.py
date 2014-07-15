import numpy as np
from itertools import groupby

import math
import matplotlib.pyplot as plt
import glob

read_files = glob.glob("text/*.txt")

with open("star.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

data = np.loadtxt('star.txt')

f = data[:,0]
power = data[:,1]

est_f = np.round(f, 2)
data = [est_f, power]


inp = [['a', 'b', 2], ['a', 'c', 1], ['a', 'b', 1]]
[k[:2] + [sum(v[2] for v in g)] for k,g in groupby(sorted(data), key=lambda x: x[:2])]






result = collections.defaultdict(int) # new keys are auto-added and initialized as 0
for item in data:
    est_f, value = item
    result[(est_f)] += value

print result
print dict(result)
print [[est_f, total] for (est_f), total in result.items()]





