from __future__ import division
from math import*
from numpy import*
import numpy as np
import random
from matplotlib import pyplot as plt

a=3*10**10     #m      semimajor x axis 
b=10**10       #m    semiminor z axis axis
c=b            #m   semininor y axis

alpha = 0.1
Lambda = alpha* a  #R/T #Mean Free Path


nph=10**3
TimeS=np.empty(nph)

for p in range(nph):
    Phi = np.pi/2 #np.arccos((np.random.rand()*2)-1)
    Theta = np.pi/2  #np.random.rand()*2*pi

    #outer radii
    X=a*np.outer(np.cos(Theta),np.sin(Phi))
    Z=b*np.outer(np.sin(Theta),np.sin(Phi))
    Y=c*np.outer(np.ones(np.size(Phi)),np.cos(Phi))

    R=(X**2+Y**2+Z**2)**(1/2)
    
    i=1
    D=0
    x=0
    y=0
    z=0

    
    C=3.0*10**8 #m/s

    Time=0
    TimeT=0

    while D < R:
        Theta=np.random.rand()*2*pi
        Phi=np.arccos((np.random.rand()*2)-1)

        d=Lambda*np.random.rand()

        x=x+d*cos(Theta)*sin(Phi)
        y=y+d*sin(Theta)*sin(Phi)
        z=z+d*cos(Phi)

        D=(x**2+y**2+z**2)**(1/2)

        ThetaC=np.arccos(x/D)
        PhiC= np.arcsin(x/D)
        
        #Radius for comparision
        X=a*np.outer(np.cos(ThetaC),np.sin(PhiC))
        Z=b*np.outer(np.sin(ThetaC),np.sin(PhiC))
        Y=c*np.outer(np.ones(np.size(PhiC)),np.cos(PhiC))

        R=(X**2+Y**2+Z**2)**(1/2)


        Time=(d/C)                                  #Time per scatter displacement
        TimeT=TimeT+Time                            #Total Time of photon motion

        i+=1

    Rd=D-R                                          #Distance traveled after leaving the star 
    TimeS[p]=(TimeT-(Rd/C))                         #Total time of photon motion while in the star   
    #print "Number of Scatters: " +str(i)

        
plt.hist(TimeS,align='mid', bins=100)
plt.ylabel('Number of Photons')
plt.xlabel('Total Scattering Time (s)')
plt.show()

