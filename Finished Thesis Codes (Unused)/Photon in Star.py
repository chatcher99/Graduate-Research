from __future__ import division
import sys
from math import*
import numpy
from numpy import*
import random
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


nph=10000
TimeS=numpy.empty(nph)

for p in range(nph):

    R=10**12 #cm Radius
    T=10 #Opacity

    Lambda=R/T #Mean Free Path

    i=1
    D=0
    X=0
    Y=0
    Z=0

    C=3.0*10**8 #m/s

    Time=0
    TimeT=0
    
    while D<R:
        Theta=numpy.arccos((numpy.random.rand()*2)-1)
        Phi=(numpy.random.rand())*(2*pi)
    
        d=Lambda*(-numpy.log(numpy.random.rand()))

        X=X+d*sin(Theta)*cos(Phi)
        Y=Y+d*sin(Theta)*sin(Phi)
        Z=Z+d*cos(Theta)

        D=(X**2+Y**2+Z**2)**(1/2)
        Time=(d/C)                                  #Time per scatter displacement
        TimeT=TimeT+Time                            #Total Time of photon motion
    
        i+=1
        
    Rd=D-R                                          #Distance traveled after leaving the star
    #print "Number of Scatters: " +str(i-1)
    TimeS[p]=(TimeT-(Rd/C))                         #Total time of photon motion while in the star   
    
    
plt.hist(TimeS,align='mid', bins=100)
plt.ylabel('Quantity')
plt.xlabel('Total Scattering Time (s)')
plt.show()
