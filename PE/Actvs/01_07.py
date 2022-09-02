# -*- coding: utf-8 -*-

import statistics as stt
import numpy as np
import matplotlib.pyplot as plt

lista=[94.1, 86.1, 95.3, 84.9, 88.8, 84.6, 94.4, 84.1, 90.6, 89.1, 97.8, 89.6,
85.1, 85.4, 98.0, 82.9, 91.4, 87.3, 93.1, 90.3, 84.0, 89.7, 85.4, 87.3]

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
