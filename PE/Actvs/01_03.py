# -*- coding: utf-8 -*-

import statistics as stt
import numpy as np
import matplotlib.pyplot as plt

lista=[1, 3, 5, 3, 2, 0, 1, 2, 6, 3, 4, 2, 1, 4, 6, 11, 9, 10, 18, 4]

me=stt.mean(lista)
med=stt.median(lista)
var=stt.variance(lista)
dep=stt.stdev(lista)

print(lista)

print("Media:", me)
print("Mediana:", med)
print("Variância:",var)
print("Desvio Padrão:",dep)

plt.title("Box-Plot")

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.boxplot(lista)
plt.show()
