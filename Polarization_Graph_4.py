from __future__ import division
from math import *
from numpy import *
import numpy as np
from Thesis_lib_4 import *
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

nph = 5*10**6
NumD = 10
DoF = 5

alpha = 1.2
runID = str(alpha)

SemiMajor = 10
SemiMinor = 0.625
Height = 0.625

Gen_Plot_Data(nph,NumD,DoF,alpha,runID,SemiMajor,SemiMinor,Height)


Angle = loadtxt('PLOTDATA/ANGLE_'+str(SemiMajor)+'_'+str(SemiMinor)+'_'+str(Height)+'_a='+runID+'.dat',unpack=True)
Polar = loadtxt('PLOTDATA/POLAR_'+str(SemiMajor)+'_'+str(SemiMinor)+'_'+str(Height)+'_a='+runID+'.dat',unpack=True)
Error = loadtxt('PLOTDATA/ERROR_'+str(SemiMajor)+'_'+str(SemiMinor)+'_'+str(Height)+'_a='+runID+'.dat',unpack=True)
AVG_SCAT=loadtxt('PLOTDATA/AVG_SCAT_'+str(SemiMajor)+'_'+str(SemiMinor)+'_'+str(Height)+'_a='+runID+'.dat',unpack=True)

#Sum2=sum(int(s.strip()) for s in open('DATASETS/Scatter_Count_a='+runID+'.dat'))
#average2=Sum2/len(open('DATASETS/Scatter_Count_a='+runID+'.dat').readlines())
#print('\n'+'Average Overall Scatter = '+str(average2))

MaxP=100*max(Polar)
print("Maximum Polarization: "+str(MaxP))

print("Average Scatter: "+str(AVG_SCAT))

j=np.arange(0,np.pi/2,0.01) 
C=np.cos(j)**2
F=(1-C)/(1+C)*100

plt.figure(1)

plt.plot(j*180/np.pi,F, color='b', label='Theoretical',linewidth=2.5)
plt.errorbar(Angle*180/np.pi,Polar*100,yerr=Error,fmt='o',markersize=5.5,ls='-', linewidth=2.5,color = 'red',label='Simulation')
plt.plot([0,90],[0,0],'k--')

plt.xlabel('Angle off of X axis (Degrees)', fontsize=18, weight='bold',labelpad=12)
plt.ylabel('Linar Polarization (%)', fontsize=18,weight='bold',labelpad=10)

plt.axis([-0.5,92,-0.5,12])
plt.xticks(np.arange(0,95,10),fontsize=15)
plt.yticks(np.arange(0,11,2),fontsize=15)
plt.legend(loc='best',fontsize=20)
plt.title(r'$\alpha$='+runID+'           Max Polarization = '+str(MaxP), fontsize=20)
plt.show()
