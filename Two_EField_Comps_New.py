from __future__ import division
from math import *
from numpy import *
import numpy as np
from Thesis_lib_2 import *
from One_Compton_Scatter import *

def EField_Comps(Detect,nph):
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


    #Find EField Compents in Detector Reference Frame
    outfile_EC=open('Exit_EField_Comps.dat','w')

    D=Detect

    XD=np.array((1/(D[0]**2+D[1]**2+D[2]**2))**(1/2)*D)                                        #direction of detector=xaxis of detector reference frame=line through back of detector
    ZD=np.array([ (-sign(XD[0])*XD[2]/(XD[0]**2+XD[2]**2)**(1/2)) , 0 , (1-(XD[2]**2/(XD[0]**2+XD[2]**2)))**(1/2) ])     #z axis of the detector
    Zy=(1/((XD[0]**2/XD[2]**2)+((XD[0]**2+XD[2]**2)**2/(XD[1]**2*XD[2]**2))+1))**(1/2)
    YD=np.array([(Zy*XD[0]/XD[2]), -((Zy/XD[1])*((XD[0]**2+XD[2]**2)/XD[2])), Zy])     #is the yaxis of the detector reference frame

    #print "Number of Photons: " +str(len(Ex))

    for i in range(Ex.size):
        E=(Ex[i],Ey[i],Ez[i])

        Ecx=np.dot(E,XD)/np.linalg.norm(XD)
        Ecy=np.dot(E,YD)/np.linalg.norm(YD)
        Ecz=np.dot(E,ZD)/np.linalg.norm(ZD)

        writestring_EC=str(Ecx)+'\t'+str(Ecy)+'\t'+str(Ecz)+'\n'
        outfile_EC.write(writestring_EC)
            
        Ep=(Ecx,Ecy,Ecz)

    outfile_EC.close()
    return 

Detect=np.array([0.001,0.001,1])
EField_Comps(Detect,10**3)


