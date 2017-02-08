from __future__ import division
import sys
from math import*
import numpy
from numpy import*
import random
from matplotlib import pyplot as plt

def Psi(num_pts):
    XX=[]
    for i in range(num_pts):                        #generate random x values for sine graph and scatter
        x=numpy.random.rand()*numpy.pi              #same x values for both sine scatter allows for easier comparison because we can now just focus on the discrpancies in Y values
        XX.append(x)
    Xsine=sort(XX)                                  #sort random values so that when plotting sin it will be correct
    Ysine=numpy.sin(Xsine)**3                       #generates y values for sin^3 graph
    #plt.scatter(Xsine,Ysine,color='r',zorder=1)    #plots sin^3

    YY=[]
    for t in range(len(Xsine)):                     #generates random y value for random scatter, for every X value. 
        y=numpy.random.rand()                   
        YY.append(y)

    Xscat=[]        
    Yscat=[]
    for i in range(len(YY)):                        #compares y values of scatter to y values of sin at cooresponding x values
        if YY[i]<= Ysine[i]:
            Yscat.append(YY[i])
            Xscat.append(Xsine[i])

    '''T=numpy.arange(0,numpy.pi,0.01)                 #create x vaules for sine plot

    plt.subplot(211)
    plt.scatter(Xsine,Ysine,color='r',zorder=1,s=0.1)
    plt.scatter(Xscat,Yscat,s=0.5)
    plt.plot(T,numpy.sin(T)**3)                 #plots sine graph
    plt.subplot(212)
    plt.hist(Xscat, bins=25)
    plt.show()'''

    Psi=numpy.random.choice(Xscat,1)
    print "Psi: "+str(Psi)
    return Psi
#Psi(5)

def Scatter_Vectors(R,Tau,nph,Psi):
    for p in range(nph):
        Lambda=R/Tau                                          #Mean Free Path
                
        Kx=1 #numpy.random.rand()                           #generating propogation vector components                
        Ky=0 #numpy.random.rand()
        Kz=0 #numpy.random.rand()
        K=(Kx,Ky,Kz)                                        #Propogation Vector

        d=Lambda*(-numpy.log(numpy.random.rand()))          #Random Scattering Distance

        #Psi=numpy.arccos((numpy.random.rand()*2)-1)        #angle off of y axis in zy plane
        Phi=(numpy.random.rand())*(2*pi)                    #angle off of y axis XY plane

        Kxx=d*cos(Psi)                                      #generating scatter vector components
        Kyy=d*sin(Psi)*sin(Phi)
        Kzz=d*sin(Psi)*cos(Phi)
    
        KK=(Kxx,Kyy,Kzz)                                    #Scatter Vector
        print "Scatter Vector: "+str(KK)
    return KK
                    
Scatter_Vectors(2.54,10,10, Psi(5))


theta=numpy.random.rand()*(pi)                          #generating random angle of E prop. 
def Rotation(E,theta):
    Rotate=numpy.matrix([[1,0,0],[0,numpy.cos(theta),numpy.sin(theta)],[0,-numpy.sin(theta),numpy.cos(theta)]])
    EE=E*Rotate
    print 'Propogation E Field'+str(EE)
    return EE

Rotation((0,cos(theta),sin(theta)))

'''def L_Vector(KK,EE):
    L=numpy.cross(KK,E)
    print L
    return L

L_Vector(KK,EE)'''





    
