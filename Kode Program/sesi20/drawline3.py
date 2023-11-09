#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 3, 4, 5, 8])
ypoints = np.array([3, 4, 5, 6, 7, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
