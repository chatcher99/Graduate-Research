from __future__ import division
import sys
from math import*
import numpy
from numpy import*
import random
from matplotlib import pyplot as plt

R=10**12 #cm Radius
Tau=10 #Opacity

Lambda=R/Tau #Mean Free Path

c=3.0*10**9 #cm/s

nph=10000
TimeS=numpy.empty(nph)

for p in range(nph):

    i=1
    D=0                     #Net Vector of total distance traveled
    X=0                     #X component of vector
    Y=0                     #Y component of vector
    Z=0                     #Z component of vector

    Time=0                  #time of one scatter
    TimeT=0                 #total time of all scatters
    
    while D<R:              
        Theta=numpy.arccos((numpy.random.rand()*2)-1)       #generate random angle off of y axis zy plane
        Phi=(numpy.random.rand())*(2*pi)                    #angle off of y axis xy plane
    
        d=Lambda*(-numpy.log(numpy.random.rand()))          #net vector of one scatter

        X=X+d*sin(Theta)*cos(Phi)                           #generate X component of scatter vector
        Y=Y+d*sin(Theta)*sin(Phi)                           #generate Y component of scatter vector
        Z=Z+d*cos(Theta)                                    #generate Z component of scatter vector

        D=(X**2+Y**2+Z**2)**(1/2)
        Time=(d/C)                                  #Time per scatter displacement
        TimeT=TimeT+Time                            #Total Time of photon motion
    
        i+=1
        
    D_Out=D-R                                          #Distance traveled after leaving the star
    #print "Number of Scatters: " +str(i-1)
    TimeS[p]=(TimeT-(D_Out/c))                         #Total time of photon motion while in the star   
    
    
plt.hist(TimeS,align='mid', bins=100)
plt.ylabel('Quantity')
plt.xlabel('Total Scattering Time (s)')
plt.show()
