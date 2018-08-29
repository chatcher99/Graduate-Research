from __future__ import division
from math import *
from numpy import *
import numpy as np
import matplotlib.pyplot as plt


#A1 ID  A2 zbest    A3 M_med    A4 RA   A5 DEC  A6 IRAC_Ch1_FLUX    A7 IRAC_Ch1_FLUXERR
#A8 IRAC_Ch2_FLUX   A9 IRAC_Ch2_FLUXERR     A10 IRAC_Ch3_FLUX   A11 IRAC_Ch3_FLUXERR
#A12 IRAC_Ch4_FLUX  A13 IRAC_Ch4_FLUXERR    A14 f_IRAC_58   A15 f_IRAC_80   A16 f_MIPS24
#A17 f_MIPS70   A18 f_MIPS160   A19 f_PACS_100   A20 f_PACS_160   A21 f_SPIRE_250   A22 f_SPIRE_350 A23 f_SPIRE_500

A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23=loadtxt('Master_Flux_Catalog.txt',unpack=True)

### Wavelengths are in micrometers. They are the numbers at the end of the filter names

#A6 = 3.6       A8 = 4.5        A10 = 5.8       A12 = 8.0       A14 = 58
#A15 = 80       A16 = 24        A17 = 70        A18 = 160       A19 = 100
#A20 = 160      A21 = 250       A22 = 350       A23 = 500

'''
Nonzero = []

for i in range(len(A14)):
    if A14[i] != 0:
        Nonzero.append(A1[i])

#print(Nonzero)
'''

#GALAXY=random.choice(Nonzero)
INDEX=list(A1).index(62)

AA6= A6/1000
AA8=A8/1000
AA10=A10/1000
AA12=A12/1000


FLUX = np.array([AA6[INDEX],AA8[INDEX],AA10[INDEX],AA12[INDEX],A14[INDEX],A15[INDEX],A16[INDEX],
                 A17[INDEX],A18[INDEX],A19[INDEX],A20[INDEX],A21[INDEX],A22[INDEX],A23[INDEX]])

WL = np.array([3.6,4.5,5.8,8.0,58,80,24,70,160,100,160,250,350,500])
RWL=np.zeros([len(WL)])*10**-6
Z = A2[INDEX]

for i in range(len(WL)):
    RWL[i] = WL[i]/(1+Z)
    


#print(FLUX)
#print(RWL)
plt.scatter(RWL,FLUX)
#plt.yscale('log')
plt.xscale('log')
plt.show()



