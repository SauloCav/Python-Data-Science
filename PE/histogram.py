# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = [43, 45, 49, 47, 52, 45, 51, 46, 44, 48, 51, 50, 52, 44, 48, 50, 49, 50, 46, 46, 49, 49, 51, 50]

fig, ax = plt.subplots(ncols=1, figsize=(8, 4))
numBins=5
ax.hist(x, numBins, histtype='bar', rwidth=.75, facecolor='black', alpha=0.8)
ax.set_title('Histogram')
plt.show()
