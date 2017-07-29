from __future__ import division
from math import*
from numpy import*
import numpy as np
from Thesis_lib_2 import*



a=3*10**10              #m semimajor x axis 
b=10**10                #m semiminor z axis axis
c=b                     #m semininor y axis

Cloud_Scatter(nph,a,b,c

alpha = 1
Lambda = alpha*a   
#Select Vectors in Direction of Detector 
    kx,ky,kz=loadtxt('Exit_Vectors.dat',unpack=True)
    Ex,Ey,Ez=loadtxt('Exit_EFields.dat',unpack=True)
    outfile_SV=open('Selected_Exit_Vectors.dat','w')
    outfile_SE=open('Selected_Exit_EFields.dat','w')
    
    #Detect=np.array([0.001,0.001,1])
    #print "Detector: " +str(Detect)
    DetLength=np.linalg.norm(Detect)

    DFD=5                  #degrees off of detector vector that are accepted

    i=0
    while i < nph:      
        vect=np.array([kx[i],ky[i],kz[i]])          #takes vector
        VectLength=np.linalg.norm(vect)             #norm of vector
        a=(np.dot(vect,Detect))/(DetLength*VectLength)  #determines the angles between the scatter vector and the detector vector
        omega=np.arccos(a)
        if omega <= np.deg2rad(DFD):        #if this angle is within our degreees of freedom = keep
            writestring_SV=str(kx[i])+'\t'+str(ky[i])+'\t'+str(kz[i])+'\n'
            outfile_SV.write(writestring_SV)
            writestring_SE=str(Ex[i])+'\t'+str(Ey[i])+'\t'+str(Ez[i])+'\n'
            outfile_SE.write(writestring_SE)
        i+=1

    outfile_SV.close()
    outfile_SE.close()

    x,y,z=loadtxt('Selected_Exit_Vectors.dat',unpack=True)
    Ex,Ey,Ez=loadtxt('Selected_Exit_EFields.dat',unpack=True)

