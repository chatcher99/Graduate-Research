from __future__ import division
from math import *
from numpy import *
import numpy as np
import matplotlib.pyplot as plt


#C1 ID C2 Fraction  C3 Color
C1,C2,C3=loadtxt('Color_Selection.txt',unpack=True)

#M1 ID M2Fraction
M1,M2=loadtxt('MAGPHYS_Galaxy_Matches.txt',unpack=True)

#F1 ID  F2 IRAC     F3 Full Lx  F4 Soft Lx  F5 Hard Lx  F6 ANG Flag
#F7 Full Flx Fran    F8 Soft Flx Fran   9 Hard Flx Fran     10 HR Fran

F1,F2,F3,F4,F5,F6,F7,F8,F9,F10=loadtxt('Master_AGN_Catalog.txt',unpack=True)

#R1 Field   R2 ID   R3 z    R4 f(AGN)   R5 MIR  R7 LIR  R8 Mstar    R9 Edd Ratio
#R10 LX(AGN) R10 LX(Total)   ### XRay Lum are predited from LIR

R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11=genfromtxt('Edd_acc_rates.txt',unpack=True,dtype=float,filling_values=1)

'''
### Color vs MAGPHYS ###

CC_MM=[]

for i in range(len(C1)):
    for j in range(len(M1)):
        if C1[i]==M1[j]:
            if M2[j] != -99.99:
                CC_MM.append(C2[i]-M2[j])


plt.figure()

plt.hist(CC_MM,3,color='blue',edgecolor='white')
#plt.scatter(CC1,MM,s=10)
plt.xlabel('Color f(AGN)')
plt.ylabel('MAGPHYS f(AGN)')
plt.title("Color Selection vs. MAGPHYS")
plt.savefig('Color Selection vs. MAGPHYS.png')


### Color vs Full Xray Lum ###

CC2=[]
CC3=[]
FF1=[]
FF2=[]

for i in range(len(C1)):
    for j in range(len(F1)):
        if C1[i]==F1[j]:
            if F3[j]!=-99.99:
                CC2.append(C2[i])
                FF1.append(F3[j])
                
                if 0<C2[i]<=0.3:
                    C2[i]=0.3
                    CC3.append(C2[i])
                    FF2.append(F3[j])
                if 0.3<C2[i]<=0.6:
                    C2[i]=0.6
                    CC3.append(C2[i])
                    FF2.append(F3[j])
                if 0.6<C2[i]<=1:
                    C2[i]=0.9
                    CC3.append(C2[i])
                    FF2.append(F3[j])
                

plt.figure()
#plt.scatter(CC2,FF1,s=10)
plt.scatter(CC3,FF2,color='red',s=10)
plt.xlabel('Color f(AGN)')
#plt.xticks(plt.hist(CC_MM,3,color='blue',edgecolor='white')
plt.ylabel('Full XRay Lum)')
plt.title("Color Selection vs. XRay Lum")
#plt.show()        

plt.savefig('Color Selection vs. XRay Lum.png')

'''

### Lir VS Lx ###

FF2=[]
RR1=[]

for i in range(len(F1)):
    for j in range(len(R1)):
        if F1[i]==R2[j]:
            if F3[i]!=-99.99:
                FF2.append(F3[i])
                RR1.append(R7[j])
plt.figure()
plt.scatter(RR1,FF2,s=10)
plt.xlabel('Lir')
plt.ylabel('Lx')
plt.title("IR Lum vs. XRay Lum")

plt.savefig('IR Lum vs. XRay Lum.png')

plt.show()






