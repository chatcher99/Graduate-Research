from __future__ import division
import sys
from math import *
from numpy import *
import numpy as np
from Thesis_lib import *
from Selecting_Scatter_Angles import *


x,y,z=loadtxt('Selected_Vectors.dat',unpack=True)
Ex,Ey,Ez=loadtxt('Selected_EFields.dat',unpack=True)

#print len('Selected_Vectors.dat')

Detect=Detect



i=0
while i<len('Selected_Vectors.dat'):
    xp=(Detect[i],Detect[i],Detect[i])                 #direction of photons=xaxis of detector reference frame=line through back of detector
    alpha=(xp[0]**2,xp[1]**2,xp[2]**2)

    B=(1/(alpha+(alpha**2/xp[1]**2)-2*alpha))**(1/2)
    A=-(B*alpha)/xp[1]

    yp=(B*xp[0],(A+B*xp[1]),B*xp[2])    #is the yaxis of the detector reference frame
    zp=(xp[0],0,xp[2])
    i+=1

    
