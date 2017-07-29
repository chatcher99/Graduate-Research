from __future__ import division
from math import*
from numpy import*
import numpy as np
from matplotlib import pyplot as plt
from Thesis_lib_2 import*


def Cloud_Scatter(nph):
    outfile_V=open('Exit_Vectors.dat','w')
    outfile_E=open('Exit_EFields.dat','w')
    outfile_F=open('Final_Location.dat','w')

    ####Define parameters####

    C=3.0*10**8             #m/s

    a=3*10**10              #m semimajor x axis 
    b=10**10                #m semiminor z axis axis
    c=b                     #m semininor y axis

    alpha = 0.1
    Lambda = alpha*a        #R/T #Mean Free Path

    TimeS=np.empty(nph)     #create empty array for time values 

    for p in range(nph):

        K,E,Theta,Phi,d=Propagation(Lambda)         #Create Initial Propagation Vector
        
        R=EllipCloud(Theta,Phi,a,b,c)[0,0]          #Radius of cloud at angle of propagation

        X=K[0]
        Y=K[1]
        Z=K[2]

        D=np.linalg.norm(K)                     #Distance from orgin
        #Sigma=np.random.rand()*(pi)             #Random angle for Efield 
        #E=array([0,cos(Sigma),sin(Sigma)])
        

        i=0
        TimeT=np.linalg.norm(K)/C               #initial time of travel
        
        while D <= R:                            #Scatter Process
            #print("K: "+str(K))
            Kqp,Eqp,Zeta,Psi,d = ComptonScatter(K,E,Lambda,Theta,Phi)    #rotates K to (1,0,0) and E to (0,1,0) then scatters and counter rotates
            X=X+Kqp[0]
            Y=Y+Kqp[1]
            Z=Z+Kqp[2]
            Dist=(X**2+Y**2+Z**2)**(1/2)
            D=Dist
            
            #find angle D is away from y axis now
            ThetaR=np.arccos(Y/D)

            #find angle D is away from x axis now
            PhiR=np.arctan(Z/X)
            R=EllipCloud(ThetaR,PhiR,a,b,c)[0,0]      #Radius at angle of scatte
            
            K = Kqp
            E = Eqp
            Theta = Zeta
            Phi = Psi
            
            Time=(np.linalg.norm(K)/C)                                  #Time per scatter displacement
            TimeT=TimeT+Time                            #Total Time of photon motion
            i+=1

        Rd=D-R                                          #Distance traveled after leaving the star 
        if TimeT==0:
            TimeS[p]=0
        else:
            TimeS[p]=(TimeT-(Rd/C))                         #Total time of photon motion while in the star   

        writestring_V=str(K[0])+'\t'+str(K[1])+'\t'+str(K[2])+'\n'
        writestring_E=str(E[0])+'\t'+str(E[1])+'\t'+str(E[2])+'\n'
        writestring_F=str(Theta)+'\t'+str(Phi)+'\t'+str(D)+'\n'
        
        outfile_V.write(writestring_V)
        outfile_E.write(writestring_E)
        outfile_F.write(writestring_F)
    
    outfile_V.close()
    outfile_E.close()
    outfile_F.close()
       
    '''plt.hist(TimeS,align='mid', bins=100)
    plt.ylabel('Number of Photons')
    plt.xlabel('Total Scattering Time (s)')
    plt.show()'''

    return

a=3*10**10              #m semimajor x axis 
b=10**10                #m semiminor z axis axis
c=b                     #m semininor y axis


Cloud_Scatter(10**3)
