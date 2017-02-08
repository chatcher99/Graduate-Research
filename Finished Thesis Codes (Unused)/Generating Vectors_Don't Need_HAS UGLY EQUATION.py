from __future__ import division
import sys
from math import*
import numpy
from numpy import*
import random
from matplotlib import pyplot as plt

R=2.54  #cm                                             #Radius of Star
T=10                                                    #Opacity 

Lambda=R/T                                              #Mean Free Path

nph=1

for p in range(nph):

    theta=numpy.random.rand()*(2*pi)                    #Random angle of E field of propogation vector #Change to pi?

    E=(0,cos(theta),sin(theta))                         #incoming electric field

    Kx=1 #numpy.random.rand()                           #generating propogation vector components                
    Ky=0 #numpy.random.rand()
    Kz=0 #numpy.random.rand()

    K=(Kx,Ky,Kz)                                        #Propogation Vector
    #print "\nPropagation Vector:"+str(K)

    d=Lambda*(-numpy.log(numpy.random.rand()))          #Random Scattering Distance

    Psi=numpy.arccos((numpy.random.rand()*2)-1)         #angle off of y axis in zy plane
    Phi=(numpy.random.rand())*(2*pi)                    #angle off of y axis XY plane

    Kxx=d*cos(Psi)                                      #generating scatter vector components
    Kyy=d*sin(Psi)*sin(Phi)
    Kzz=d*sin(Psi)*cos(Phi)

    KK=(Kxx,Kyy,Kzz)                                    #Scatter Vector
    print "KK: " +str(KK)
    print "E: " +str(E)
    L=numpy.cross(KK,E)                                 #vector orthoganal to the plane formed by E and KK
    print "L: " +str(L)
    Lx=L[0]
    Ly=L[1]
    Lz=L[2]

    Exx=((1/(1+((-(Kxx-((Lx*Kzz)/Lz))/(Kyy-((Ly*Kzz)/Lz)))**2)+((-Lx/Lz)+((Ly*(Kxx-((Lx*Kzz)/Lz)))/((Lz*Kyy)-(Ly*Kzz))))**2))**(1/2))
    Eyy=Exx*(-(Kx-((Lx*Kzz)/Lz))/(Ky-((Ly*Kzz)/Lz)))
    Ezz=Exx*((-Lx/Lz)+((Ly*(Kxx-((Lx*Kzz)/Lz)))/((Lz*Kyy)-(Ly*Kzz))))

    EE=(Exx,Eyy,Ezz)                                    #E field of propogation
    #print "Scatter Vector: "+str(KK)
    print "Scatter Electric Field: "+str(EE)

                
