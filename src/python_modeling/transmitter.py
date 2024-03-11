import random
import matplotlib.pyplot as plt
import numpy as np
from math import ceil
import komm

numBits = int(1e3)
bits = []
for i in range(numBits):
    bits.append(ceil(random.uniform(0,1) - 0.5))

plt.stem(bits)
plt.show()

QPSK = PSKModulation(order=2)

print('Done')
