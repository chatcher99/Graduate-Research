from __future__ import division
from math import *
from numpy import *
import numpy as np
from Thesis_lib import *
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

nph=10**5

Scatter(nph)            #run scattering code to get scatter vectors and scatter efields

x=np.array([1,0,0])     #define x axis

NumD=10                 #specify how many detectors you want in 90 degrees of the 360 degree array

#XZ Plane
D=np.zeros((NumD,3))   #Array of detector coordinates
T=np.zeros((NumD))     #Array of corresponding angles from x axis (T=Theta)
P=np.zeros((NumD))     #Array of corresponding polarization 

for n in range(0,NumD):                         # Itterate through detector locations based on angle from x axis
    if n == 0:                                  # if on x axis use this because can't have 0 need 0.0000001
        D[n]=np.array([1,10**-10, 10**-10])    #Calculate Detector
        T[n]=np.arccos((np.dot(x,D[n])/(np.linalg.norm(x)*np.linalg.norm(D[n]))))
        P[n]=Stokes(EField_Comps(D[n],nph))
    else:                                   #generate detector vectors for the remainging angles
        D[n]=np.array([np.cos(n*np.pi/((NumD*2)-2)),10**-10,np.sin(n*np.pi/((NumD*2)-2))])
        T[n]=np.arccos((np.dot(x,D[n])/(np.linalg.norm(x)*np.linalg.norm(D[n]))))
        P[n]=Stokes(EField_Comps(D[n],nph))

#arrays to plot theoretical
j=np.arange(0,np.pi/2,0.01) 
C=np.cos(j)**2
F=(1-C)/(1+C)

plt.plot(j,F, color='b', label='Theoretical')
plt.scatter(T,P,color='r', label='XZ Plane')
plt.xlabel('Angle off of X axis (radians)')
plt.ylabel('Linar Polarization (%)')

plt.legend(loc=2)
plt.show()
