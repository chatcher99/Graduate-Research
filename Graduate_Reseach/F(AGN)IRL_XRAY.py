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


CR=[]
FF3=[]

for i in range(len(C1)):
    for j in range(len(R1)):
        for k in range(len(F1)):
            if C1[i]==R2[j]==F1[k]:
                if F3[k] != -99.99:
                    CR.append(C2[i]*R7[j])
                    FF3.append(F3[k])


plt.scatter(CR,FF3,s=10)
plt.xlabel('Color f(AGN) * Lir')
plt.ylabel('Full XRay Lum')
plt.title("(Color f(AGN) * Lir) vs. Full XRay Lum")
plt.show()
