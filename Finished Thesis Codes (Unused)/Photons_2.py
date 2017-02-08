from __future__ import division
import sys
from math import*
import numpy
from numpy import*
import random
from matplotlib import pyplot as plt

nph=1000   #nph= number of photons
y=numpy.empty(nph)

Lambda=5

for i in range(nph):
    x=numpy.random.rand()
    y[i]=Lambda*(-numpy.log(x))

plt.hist(y,align='mid', bins=100)
plt.show()


