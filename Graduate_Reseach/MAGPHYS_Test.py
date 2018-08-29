from __future__ import division
from math import *
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

'''
#A1 ID 	            A2 zbest              A3 M_med           A4 RA 	 A5 DEC
#A6 IRAC_Ch1_FLUX   A7 IRAC_Ch1_FLUXERR   A8 IRAC_Ch2_FLUX   A9 IRAC_Ch2_FLUXERR
#A10 IRAC_Ch3_FLUX  A11 IRAC_Ch3_FLUXERR  A12 IRAC_Ch4_FLUX  A13 IRAC_Ch4_FLUXERR
#A14 f_IRAC_58      A15 f_IRAC_80         A16 f_MIPS24       A17 f_MIPS70
#A18 f_MIPS160 	    A19 f_PACS_100        A20 f_PACS_160     A21 f_SPIRE_250
#A22 f_SPIRE_350    A23 f_SPIRE_500

A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23=loadtxt("Master_Flux_Catalog.txt",unpack=True)
ID_2,RA_2,DEC_2=loadtxt("ID_RA_DEC_MAGPHYS_ca_mir_t1.txt",unpack=True)

ID_1=A1
DEC_1=A5
RA_1=A4

Outfile_G = open("Close_Galaxies.txt",'w')
Outfile_G.write('# ID_Ours \t ID_MAGPHYS \t Distance(Arc Seconds) \n \n')

DISTANCE_FINAL=[]

for i in range(len(DEC_1)):
    for j in range(len(DEC_2)):
        AVERAGE_DEC=(DEC_1[i]+DEC_2[j])/2         #Degrees
        DELTA_DEC = DEC_1[i]-DEC_2[j]             #Degrees
        DELTA_RA = (RA_1[i]-RA_2[j])*np.cos(AVERAGE_DEC)      #Degrees*unitless

        DISTANCE = np.sqrt(DELTA_DEC**2+DELTA_RA**2)    #root(Degrees**2+Degrees**2) = Degrees

        DISTANCE_FINAL.append(DISTANCE*3600)
        
        if DISTANCE*3600 <= 2:
            Outfile_G.write(str(ID_1[i])+'\t'+str(ID_2[j])+'\t'+str(DISTANCE/3600)+'\n')
            
Outfile_G.close()            

'''

Outfile_AGN=open('MAGPHYS_Galaxy_Matches.txt','w')
Outfile_AGN.write('#ID \t AGN \t FLAG \n')


ID,ID_M2, DIST = loadtxt('Close_Galaxies.txt',unpack=True)
ID_M, FLAG = np.genfromtxt('AGNF_50_AGN_ca_mir_t1.txt',dtype=float,filling_values=-99.99,unpack=True)#loadtxt('AGNF_50_AGN_ca_mir_t1.txt',unpack=True)

for i in range(len(ID_M2)):
    for j in range(len(ID_M)):
        if ID_M2[i] == ID_M[j]:
            
            Outfile_AGN.write("{:10}{:8}\n".format(str(int(ID[i])),str(FLAG[j])))

Outfile_AGN.close()









