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

# B1 RA
# B2 DEC
# B3 Flux_F
# B4 Flux_S
# B5 Flux_H
# B6 HR


Outfile_X=open("XRay_Counterparts_Fran.txt",'w')

A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23 = loadtxt('Master_Flux_Catalog.txt',unpack=True)

B1,B2,B3,B4,B5,B6 = loadtxt('chandra_COSMOS_legacy_opt_NIR_counterparts_20160113_4d _1__t1.txt',unpack=True)
Outfile_X.write('#Closest ID \t RA\t DEC \t Flux_F_FRAN \t FLux_S_FRAN \t Flux_H_FRAN \t HR_FRAN \n \n \n')

for i in range(len(A1)):
    for j in range(len(B1)):
        if np.isclose(A4[i], B1[j],rtol=0.00001) and np.isclose(A5[i], B2[j],rtol=0.0001,atol=0.000001):
            #Outfile_X.write(str(A1[i])+'\t'+str(B1[j])+'\t'+str(B2[j])+'\t'+str(B3[j])+'\t'+str(B4[j])+'\t'+str(B5[j])+'\t'+str(B6[j])+'\n')
            #print(B2[j])
            #print(B3[j])
            Outfile_X.write("{:10}{:15}{:15}{:15}{:15}{:15}{:12}\n".format(str(int(A1[i])),str(round(B1[j],6)),str(round(B2[j],6)),str(B3[j]),str(B4[j]),str(B5[j]),str(B6[j])))
            

Outfile_X.close()

                                                                                           
