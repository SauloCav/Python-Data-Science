# -*- coding: utf-8 -*-

import statistics as stt
import numpy as np
import matplotlib.pyplot as plt

lista=[43, 45, 49, 47, 52, 45, 51, 46, 44, 48, 51, 50, 52, 44, 48, 50, 49, 50, 46, 46, 49, 49, 51, 50]

lista.sort();

me=stt.mean(lista)
med=stt.median(lista)
var=stt.variance(lista)
dep=stt.stdev(lista)
q1=np.quantile(lista, [0.25,0.5,0.75])

print(lista)

print("Media:", me)
print("Mediana:", med)
print("Variância:",var)
print("Desvio Padrão:",dep)
print("Quartis:", q1)

plt.title("Box-Plot")

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.boxplot(lista)
plt.show()

fig, ax=plt.subplots(ncols=1, figsize=(8, 4))
numBins=5
ax.hist(lista, numBins, histtype='bar', rwidth=.75, facecolor='black', alpha=0.8)
ax.set_title('Histograma')
plt.show()
