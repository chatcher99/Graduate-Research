from __future__ import division
from math import *
from numpy import *
import numpy as np
from Two_EField_Comps import *


def Stokes(EFieldComps):
    #Calculate componets of Efields on each axis
    Ecx,Ecy,Ecz=loadtxt('EField_Comps.dat', unpack=True)
    outfile_P=open('Polarization.dat','w')
        
    a=array([sqrt(2),sqrt(2)])          #rotates axes
    b=array([sqrt(2),-sqrt(2)])

    EZ=np.zeros([Ecx.size])
    EY=np.zeros([Ecx.size])
    Ea=np.zeros([Ecx.size])
    Eb=np.zeros([Ecx.size])
        
    for i in range(Ecx.size):
        Ec=array([Ecy[i], Ecz[i]])

        EZ[i]=Ecz[i]
        EY[i]=Ecy[i]

        Ea[i]=np.dot(Ec,a)
        Eb[i]=np.dot(Ec,b)

    #Compute Stokes Parameters
    EZ2=EZ**2
    EY2=EY**2
    Ea2=Ea**2
    Eb2=Eb**2

    I=sum(EZ2)/Ecx.size + sum(EY2)/Ecx.size
    Q=sum(EZ2)/Ecx.size - sum(EY2)/Ecx.size
    U=sum(Ea2)/Ecx.size - sum(Eb2)/Ecx.size
    P=np.sqrt(Q**2+U**2)/I

    outfile_P.write(str(P))
    outfile_P.close()

    return P

#print Stokes(EField_Comps(Detect))


