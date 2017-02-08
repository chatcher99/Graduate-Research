from __future__ import division
import sys
from math import*
import numpy
from numpy import*
import random
from matplotlib import pyplot as plt

R=2.54 #cm 
T=10 #Opacity ????

Lambda=R/T #Mean Free Path

nph=10

for p in range(nph):

    theta=numpy.random.rand()*(pi)                    #Random angle of E field of propogation vector

    E=(0,cos(theta),sin(theta))                         #incoming electric field

    Kx=1 #numpy.random.rand()                           #generating propogation vector components                
    Ky=0 #numpy.random.rand()
    Kz=0 #numpy.random.rand()

    K=(Kx,Ky,Kz)                                        #Propogation Vector

    d=Lambda*(-numpy.log(numpy.random.rand()))          #Random Scattering Distance

    Phi=numpy.arccos((numpy.random.rand()*2)-1)       #Random Scattering Angles
    Psi=(numpy.random.rand())*(2*pi)

    Kxx=d*cos(Phi)                                    #generating scatter vector components
    Kyy=d*sin(Phi)*sin(Psi)
    Kzz=d*sin(Phi)*cos(Psi)

    KK=(Kxx,Kyy,Kzz)                                    #Scatter Vector

    L=numpy.cross(KK,E)                                 #vector orthoganal to te plane formed by E and KK

    Lx=L[0]
    Ly=L[1]
    Lz=L[2]

    Rotate=numpy.matrix([[1,0,0],[0,numpy.cos(theta),numpy.sin(theta)],[0,-numpy.sin(theta),numpy.cos(theta)]])
    EE=E*Rotate
    print EE

    #print "Scatter Vector: "+str(KK)
    #print "Scatter Electric Field: "+str(EE)
