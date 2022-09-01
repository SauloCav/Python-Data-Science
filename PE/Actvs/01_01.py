# -*- coding: utf-8 -*-

import statistics as stt
import numpy as np
import matplotlib.pyplot as plt

a=[9.2, 10.8, 10.6, 11.1, 12.1, 9.6, 11.2, 8.4, 12.9, 12.1, 14.4, 11.1, 11.1, 9.7, 8.4, 12.3, 10.7, 12.9, 9.1, 12.8]
b=[12.5, 18.5, 21.3, 14.3, 18.5, 19.0, 10.8, 23.1, 17.4, 10.7, 14.3, 16.3, 18.0, 7.1, 12.8, 14.7, 11.3, 8.2, 13.8]
c=[21.3, 28.7, 15.8, 24.0, 13.7, 18.1, 12.6, 14.6, 6.1, 19.8, 22.3, 15.7, 16.3, 18.2, 15.7, 6.6, 9.3, 1.3, 19.0]
d=[13.7, 8.6, 14.9, 10.2, 14.0, 10.5, 15.0, 5.2, 10.0, 11.7, 18.7, 9.3, 7.9, 6.5, 11.5, 12.0, 8.3, 8.3, 9.8, 4.7]

a.sort()
b.sort()
c.sort()
d.sort()

mea=stt.mean(a)
meda=stt.median(a)
moda=stt.mode(a)

meb=stt.mean(b)
medb=stt.median(b)
modb=stt.mode(b)

mec=stt.mean(c)
medc=stt.median(c)
modc=stt.mode(c)

med=stt.mean(d)
medd=stt.median(d)
modd=stt.mode(d)

print("A:")
print(a)
print("Media:", mea)
print("Mediana:", meda)
print("Moda:",moda)
print("\n")

print("B:")
print(b)
print("Media:", meb)
print("Mediana:", medb)
print("Moda:",modb)
print("\n")

print("C:")
print(c)
print("Media:", mec)
print("Mediana:", medc)
print("Moda:",modc)
print("\n")

print("D:")
print(d)
print("Media:", med)
print("Mediana:", medd)
print("Moda:",modd)