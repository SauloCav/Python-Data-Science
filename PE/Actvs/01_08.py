# -*- coding: utf-8 -*-

import statistics as stt
import numpy as np
import matplotlib.pyplot as plt

lista=[53.0, 53.4, 95.4, 53.5, 72.3, 70.2, 82.5, 51.1, 64.3, 59.5, 84.3, 67.3, 74.4, 82.7, 55.3,
69.5, 54.1, 55.7, 78.5, 73.0, 77.8, 70.5, 63.5, 55.7, 52.4, 87.5, 71.4, 85.8, 69.1, 50.7]

lista.sort()

me=stt.mean(lista)
med=stt.median(lista)
q1=np.quantile(lista, [0.25,0.5,0.75])

print(lista)

print("Media:", me)
print("Mediana:", med)
print("Quartis:", q1)

plt.title("Box-Plot")

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.boxplot(lista)
plt.show()

fig, ax=plt.subplots(ncols=1, figsize=(8, 4))
numBins=6
ax.hist(lista, numBins, histtype='bar', rwidth=.75, facecolor='black', alpha=0.8)
ax.set_title('Histograma')
plt.show()

