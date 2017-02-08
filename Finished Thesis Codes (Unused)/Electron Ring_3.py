from __future__ import division
import sys
from math import*
import numpy
from numpy import*
import random
from matplotlib import pyplot as plt

#Electron Ring
theta=0 #radians
charge=1.60217662*10**-19 #Coulombs

NE=(numpy.random.randint(1,100)) #number of electrons
print "Number of Electrons in Cloud:"+str(NE)

EE=['ee']*NE #electrons

RR=(numpy.random.rand())*(2*pi) #radian value

Radius=numpy.random.rand()#m

X=[]
Y=[]

for ee in EE:
    Radius=numpy.random.rand()
    x=[Radius*cos(theta)]
    y=[Radius*sin(theta)]
    RR=(numpy.random.rand())*(2*pi)
    theta = theta+(RR)
    X.append(x)
    Y.append(y)
plt.plot(X,Y,'ro')
plt.axis([-1.1,1.1,-1.1,1.1])
plt.show()
