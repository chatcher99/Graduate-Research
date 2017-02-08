from __future__ import division
import sys
from math import *
from numpy import *
import numpy as np
from Thesis_lib import *
from Scattering_Code import *

kx,ky,kz=loadtxt('Final_Scatter_Vectors.dat',unpack=True)
Ex,Ey,Ez=loadtxt('Final_E_Fields.dat',unpack=True)
outfile_SV=open('Selected_Vectors.dat','w')
outfile_SE=open('Selected_EFields.dat','w')

#set detector to be at Phi=pi/4 and theta=pi/4
#Dector vector components D1x=1 D1y=1 D1z=1
# 1 degree= 0.0174533 radians

Detect=np.array([1,1,1])
DetLength=np.linalg.norm(Detect)
#print DetLength

DFD=5                  #degrees off of detector vector that are accepted
i=0

while i < nph:
    vect=np.array([kx[i],ky[i],kz[i]])
    VectLength=np.linalg.norm(vect)
    a=(np.dot(vect,Detect))/(DetLength*VectLength)
    omega=np.arccos(a)
    if omega <= np.deg2rad(DFD):
        writestring_SV=str(kx[i])+'\t'+str(ky[i])+'\t'+str(kz[i])+'\n'
        outfile_SV.write(writestring_SV)
        writestring_SE=str(Ex[i])+'\t'+str(Ey[i])+'\t'+str(Ez[i])+'\n'
        outfile_SE.write(writestring_SE)
    i+=1

outfile_SV.close()
outfile_SE.close()










