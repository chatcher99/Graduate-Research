from __future__ import division
from math import *
from numpy import *
import numpy as np
import matplotlib.pyplot as plt


#A1 ID 	            A2 zbest              A3 M_med           A4 RA 	 A5 DEC
#A6 IRAC_Ch1_FLUX   A7 IRAC_Ch1_FLUXERR   A8 IRAC_Ch2_FLUX   A9 IRAC_Ch2_FLUXERR
#A10 IRAC_Ch3_FLUX  A11 IRAC_Ch3_FLUXERR  A12 IRAC_Ch4_FLUX  A13 IRAC_Ch4_FLUXERR
#A14 f_IRAC_58      A15 f_IRAC_80         A16 f_MIPS24       A17 f_MIPS70
#A18 f_MIPS160 	    A19 f_PACS_100        A20 f_PACS_160     A21 f_SPIRE_250
#A22 f_SPIRE_350    A23 f_SPIRE_500

A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23=loadtxt("Master_Flux_Catalog.txt",unpack=True)


## IRAC ##
Outfile_MB=open("Master_AGN_B.txt",'w')

#B1 ID  B2 Flag
B1,B2 = loadtxt("AGNs_IRAC.txt",unpack=True)
Outfile_MB.write('#ID   IRAC Flag \n\n\n')

for i in range(len(A1)):
    for j in range(len(B1)):
        if A1[i] == B1[j]:
            Outfile_MB.write("{:10}{:10}\n".format(str(int(A1[i])),B2[j]))

Outfile_MB.close()


'''
### XRay Counterparts

Outfile_MBC=open("Master_AGN_BC.txt",'w')

#A1 ID   A2 IRAC FLAG   A3 MAGHYS Fraction
A1,A2,A3 = loadtext("Master_AGN_B.txt",unpack=True)

#C1 ID  C2 Full Lx    C3 Soft Lx   C4 Hard Lx    C5 Flag AGN
# 111 = SFG  888 = AGN

C1,C2,C3,C4,C5 = loadtxt("XRay_Counterparts.txt",unpack=True)

Outfile_MBC.write("#ID   IRAC Flag  MAGPHYS Fraction   Full Lx    Soft Lx  Hard Lx    Flag AGN  \n\n\n")
for i in range(len(A1)):
    for j in range(len(D1)):
        if A1[i] == C1[j]:
            Outfile_MB.write("{:10}{:10}{:10}{:10}{:10}{:10}{:10}\n".format(str(int(A1[i])),A2[i],A3[i],C2[j],C3[j],C4[j],C5[j]))
            continue
        else:
            Outfile_MB.write("{:10}{:10}{:10}{:10}{:10}{:10}{:10}\n".format(str(int(A1[i])),A2[i],A3[i],"-99.99","-99.99","-99.99","-99.99"))
            continue

Outfile_MBC.close()

'''

'''
### XRay Counterparts FRAN

Outfile_MBCD=open("Master_AGN_BCD.txt",'w')

#A1 ID   A2 IRAC FLAG   A3 MAGHYS Fraction
A1,A2,A3 = loadtext("Master_AGN_BC.txt",unpack=True)

#C1 ID  C2 Full Lx    C3 Soft Lx   C4 Hard Lx    C5 Flag AGN
# 111 = SFG  888 = AGN

C1,C2,C3,C4,C5 = loadtxt("XRay_Counterparts.txt",unpack=True)

Outfile_MBC.write("#ID   IRAC Flag  MAGPHYS Fraction   Full Lx    Soft Lx  Hard Lx    Flag AGN  \n\n\n")
for i in range(len(A1)):
    for j in range(len(D1)):
        if A1[i] == C1[j]:
            Outfile_MB.write("{:10}{:10}{:10}{:10}{:10}{:10}{:10}\n".format(str(int(A1[i])),A2[i],A3[i],C2[j],C3[j],C4[j],C5[j]))
            continue
        else:
            Outfile_MB.write("{:10}{:10}{:10}{:10}{:10}{:10}{:10}\n".format(str(int(A1[i])),A2[i],A3[i],"-99.99","-99.99","-99.99","-99.99"))
            continue

Outfile_MBC.close()

'''






'''
## MAGPHYS ##

Outfile_MBC=open("Master_AGN_BC.txt",'w')

#A1 ID   A2 IRAC FLAG
A1,A2 = loadtxt("Master_AGN_B.txt",unpack=True)

#C1 ID  C2 MAGPHYS Flag

C1,C2 = loadtxt("MAGPHYS_Galaxy_Matches.txt",unpack=True)

Outfile_MBC.write("#ID   IRAC Flag     MAGPHYS Fraction   \n\n\n")
for i in range(len(A1)):
    for j in range(len(C1)):
        if A1[i] == C1[j]:
            Outfile_MBC.write("{:10}{:10}{:10}\n".format(str(int(A1[i])),A2[i],C2[j]))
        else:
            Outfile_MBC.write("{:10}{:10}{:10}\n".format(str(int(A1[i])),A2[i],"-99.99"))

Outfile_MBC.close()

'''

