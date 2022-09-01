# -*- coding: utf-8 -*-

import statistics as stt
import numpy as np
import matplotlib.pyplot as plt

pos=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
lista=[96, 96, 102, 102, 102, 104, 104, 108, 126, 126, 128, 128, 140, 156, 160, 160, 164, 170]

me=stt.mean(lista)
dep=stt.stdev(lista)

print(lista)

print("Media:", me)
print("Desvio Padrão:",dep)

plt.scatter(pos, lista)
plt.show()
