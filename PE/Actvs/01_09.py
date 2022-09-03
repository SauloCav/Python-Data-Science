# -*- coding: utf-8 -*-

import statistics as stt
import numpy as np
import matplotlib.pyplot as plt

lista=[46, 46, 53, 30, 62, 50, 69, 49, 58, 65, 62, 52, 44, 38, 33, 60, 50, 39, 53,
50, 64, 53, 45, 38, 31, 41, 56, 54, 38, 42, 31, 38, 66, 29, 41, 55, 43, 50, 40, 45]

lista.sort()

me=stt.mean(lista)
med=stt.median(lista)
dep=stt.stdev(lista)

print(lista)

fig, ax=plt.subplots(ncols=1, figsize=(8, 4))
numBins=5
ax.hist(lista, numBins, histtype='bar', rwidth=.75, facecolor='black', alpha=0.8)
ax.set_title('Histograma')
plt.show()
