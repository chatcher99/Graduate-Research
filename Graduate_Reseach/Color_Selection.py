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

#units of MIPS and SPIRE [mJy]
#units of IRAC [uJy]

A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23=loadtxt("Master_Flux_Catalog.txt",unpack=True)

#C1 Column 1: Redshift.
#C2 Column 2: Lower threshold, log (S100/S24)
#C3 Column 3: Upper threshold, log (S100/S24)
#C4 Column 4: Lower threshold, log (S8/S3.6)
#C5 Column 5: Upper threshold, log (S8/S3.6)
#C6 Column 6: f(AGN)_MIR  fraction of mid-IR luminosity due to heating by an AGN
#C7 Column 7: Uncertainty

C1,C2,C3,C4,C5,C6,C7 = loadtxt('diagnostic_100.txt',unpack=True)

#D1 Column 1: Redshift.
#D2 Column 2: Lower threshold, log (S24/S8)
#D3 Column 3: Upper threshold, log (S24/S8)
#D4 Column 4: Lower threshold, log (S8/S3.6)
#D5 Column 5: Upper threshold, log (S8/S3.6)
#D6 Column 6: f(AGN)_MIR  fraction of mid-IR luminosity due to heating by an AGN
#D7 Column 7: Uncertainty

D1,D2,D3,D4,D5,D6,D7 = loadtxt('diagnostic_24.txt',unpack=True)


#Convert to mJy

AA6=A6/1000
AA8=A8/1000
AA10=A10/1000
AA12=A12/1000

# Redshift.
#"0.5" = 0.25<z<0.75
#"1.0" = 0.75<z<1.25
#"1.5" = 1.25<z<1.75
#"2.0" = 1.75<z<2.25
#"2.5" = 2.25<z<2.75
#"3.0" = 2.75<z<3.25

'''
Outfile_C=open('Color_Selection.txt','w')        
Outfile_250_Test=open('250_Test.txt','w')
Outfile_100_Test=open('100_Test.txt','w')
Outfile_24_Test=open('24_Test.txt','w')

for i in range(len(A1)):
    ### Test 250 ###
    if A21[i] != 0 and A21[i] != -99:
        Outfile_250_Test.write(str(A1[i]) + '   250 \n')

    ### Test 100 ###
    if A19[i] != 0 and A19[i] != -99:
        Outfile_100_Test.write(str(A1[i]) + '   100 \n')

    ### Test 250 ###
    if A16[i] != 0 and A16[i] != -99:
        Outfile_24_Test.write(str(A1[i]) + '   24 \n')

Outfile_250_Test.close()
Outfile_100_Test.close()
Outfile_24_Test.close()
'''

#B1 Column 1: Redshift.
#B2 Column 2: Lower threshold, log (S250/S24)
#B3 Column 3: Upper threshold, log (S250/S24)
#B4 Column 4: Lower threshold, log (S8/S3.6)
#B5 Column 5: Upper threshold, log (S8/S3.6)
#B6 Column 6: f(AGN)_MIR  fraction of mid-IR luminosity due to heating by an AGN
#B7 Column 7: Uncertainty

B1,B2,B3,B4,B5,B6,B7 = loadtxt('diagnostic_250.txt',unpack=True)

#Want
#A2 zbest
#A6 IRAC CH1    A8 IRAC CH2     A10 IRAC CH3    A12 IRAC CH4
#A16 f_MIPS24   A19 f_PACS_100  A21 f_SPIRE_250



for i in range(len(A1)):
    if A21[i]!= 0 and A21[i]!= -99: 
        S250=log10(A21[i]/A16[i])
        S8 = log10(AA12[i]/AA6[i])
        for j in range(len(B1)):
            if 0.25 < A2[i] < 0.75:
                Z=0.5
                if (Z == B1[j]) and (B2[j]<S250<B3[j]) and (B4[j]<S8<B5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(B6[j])+'\t S250 \n')
            if 0.75 < A2[i] < 1.25:
                Z=1
                if (Z == B1[j]) and (B2[j]<S250<B3[j]) and (B4[j]<S8<B5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(B6[j])+'\t S250 \n')
            if 1.25< A2[i] < 1.75:
                Z= 1.5
                if (Z == B1[j]) and (B2[j]<S250<B3[j]) and (B4[j]<S8<B5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(B6[j])+'\t S250 \n')
            if 1.75 < A2[i] < 2.25:
                Z = 2
                if (Z == B1[j]) and (B2[j]<S250<B3[j]) and (B4[j]<S8<B5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(B6[j])+'\t S250 \n')
            if 2.25 < A2[i] < 2.75:
                Z = 2.5
                if (Z == B1[j]) and (B2[j]<S250<B3[j]) and (B4[j]<S8<B5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(B6[j])+'\t S250 \n')
            if 2.75 < A2[i] < 3.25:
                Z = 3
                if (Z == B1[j]) and (B2[j]<S250<B3[j]) and (B4[j]<S8<B5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(B6[j])+'\t S250 \n')

'''
    ### Test for 100 ##                 
    if A9[i]!= 0 and A9[i]!= -99:
        S100=log10(A9[i]/A6[i])
        S8 = log10(AA28[i]/AA22[i])
        for j in range(len(C1)):
            if 0.25 < A2[i] < 0.75:
                Z=0.5
                if (Z == C1[j]) and (C2[j]<S100<C3[j]) and (C4[j]<S8<C5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(C6[j])+'\t S100 \n')
            if 0.75 < A2[i] < 1.25:
                Z=1
                if (Z == C1[j]) and (C2[j]<S100<C3[j]) and (C4[j]<S8<C5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(C6[j])+'\t S100 \n')
            if 1.25< A2[i] < 1.75:
                Z= 1.5
                if (Z == C1[j]) and (C2[j]<S100<C3[j]) and (C4[j]<S8<C5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(C6[j])+'\t S100 \n')
            if 1.75 < A2[i] < 2.25:
                Z = 2
                if (Z == C1[j]) and (C2[j]<S100<C3[j]) and (C4[j]<S8<C5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(C6[j])+'\t S100 \n')
            if 2.25 < A2[i] < 2.75:
                Z = 2.5
                if (Z == C1[j]) and (C2[j]<S100<C3[j]) and (C4[j]<S8<C5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(C6[j])+'\t S100 \n')
            if 2.75 < A2[i] < 3.25:
                Z = 3
                if (Z == C1[j]) and (C2[j]<S100<C3[j]) and (C4[j]<S8<C5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(C6[j])+'\t S100 \n')
    ## Test for 24 ##
    
    if A6[i]!= 0 and A6[i]!= -99:
        #print(str(A1[i])+" YES")
        #print(A2[i])
        S24=log10(A6[i]/AA28[i])
        #print(S24)
        S8 = log10(AA28[i]/AA22[i])
        #print(S8)
        if S24 or S8 == nan:
            Outfile_C.write(str(int(A1[i]))+'\t nan \t undetection \n')
        for j in range(len(D1)):
            if 0.25 < A2[i] < 0.75:
                Z=0.5
                if (Z == D1[j]) and (D2[j]<S24<D3[j]) and (D4[j]<S8<D5[j]):
                    print(0.5)
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(D6[j])+'\t S24 \n')

            if 0.75 < A2[i] < 1.25:
                Z=1
                if (Z == D1[j]) and (D2[j]<S24<D3[j]) and (D4[j]<S8<D5[j]):
                    print(1)
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(D6[j])+'\t S24 \n') 
            if 1.25< A2[i] < 1.75:
                Z= 1.5
                if (Z == D1[j]) and (D2[j]<S24<D3[j]) and (D4[j]<S8<D5[j]):
                    print(1.5)
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(D6[j])+'\t S24 \n')                     
            if 1.75 < A2[i] < 2.25:
                Z = 2
                if (Z == D1[j]) and (D2[j]<S24<D3[j]) and (D4[j]<S8<D5[j]):
                    print(2)
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(D6[j])+'\t S24 \n')                    
            if 2.25 < A2[i] < 2.75:
                Z = 2.5
                if (Z == D1[j]) and (D2[j]<S24<D3[j]) and (D4[j]<S8<D5[j]):
                    print(2.5)
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(D6[j])+'\t S24 \n')                     
            if 2.75 < A2[i] < 3.25:
                Z = 3
                if (Z == D1[j]) and (D2[j]<S24<D3[j]) and (D4[j]<S8<D5[j]):
                    print(3)
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(D6[j])+'\t S24 \n')                         
        
    else:
        Outfile_C.write(str(int(A1[i]))+'\t -99 \t nondetection \n')   


'''


'''
for i in range(len(A1)):
    ### Test 250 ###
    
    if A11[i]!= 0 and A11[i]!= -99: 
        S250=log10(A11[i]/A6[i])
        S8 = log10(AA28[i]/AA22[i])
        for j in range(len(B1)):
            if 0.25 < A2[i] < 0.75:
                Z=0.5
                if (Z == B1[j]) and (B2[j]<S250<B3[j]) and (B4[j]<S8<B5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(B6[j])+'\t S250 \n')
            if 0.75 < A2[i] < 1.25:
                Z=1
                if (Z == B1[j]) and (B2[j]<S250<B3[j]) and (B4[j]<S8<B5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(B6[j])+'\t S250 \n')
            if 1.25< A2[i] < 1.75:
                Z= 1.5
                if (Z == B1[j]) and (B2[j]<S250<B3[j]) and (B4[j]<S8<B5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(B6[j])+'\t S250 \n')
            if 1.75 < A2[i] < 2.25:
                Z = 2
                if (Z == B1[j]) and (B2[j]<S250<B3[j]) and (B4[j]<S8<B5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(B6[j])+'\t S250 \n')
            if 2.25 < A2[i] < 2.75:
                Z = 2.5
                if (Z == B1[j]) and (B2[j]<S250<B3[j]) and (B4[j]<S8<B5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(B6[j])+'\t S250 \n')
            if 2.75 < A2[i] < 3.25:
                Z = 3
                if (Z == B1[j]) and (B2[j]<S250<B3[j]) and (B4[j]<S8<B5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(B6[j])+'\t S250 \n')
    ### Test for 100 ##                 
    if A9[i]!= 0 and A9[i]!= -99:
        S100=log10(A9[i]/A6[i])
        S8 = log10(AA28[i]/AA22[i])
        for j in range(len(C1)):
            if 0.25 < A2[i] < 0.75:
                Z=0.5
                if (Z == C1[j]) and (C2[j]<S100<C3[j]) and (C4[j]<S8<C5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(C6[j])+'\t S100 \n')
            if 0.75 < A2[i] < 1.25:
                Z=1
                if (Z == C1[j]) and (C2[j]<S100<C3[j]) and (C4[j]<S8<C5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(C6[j])+'\t S100 \n')
            if 1.25< A2[i] < 1.75:
                Z= 1.5
                if (Z == C1[j]) and (C2[j]<S100<C3[j]) and (C4[j]<S8<C5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(C6[j])+'\t S100 \n')
            if 1.75 < A2[i] < 2.25:
                Z = 2
                if (Z == C1[j]) and (C2[j]<S100<C3[j]) and (C4[j]<S8<C5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(C6[j])+'\t S100 \n')
            if 2.25 < A2[i] < 2.75:
                Z = 2.5
                if (Z == C1[j]) and (C2[j]<S100<C3[j]) and (C4[j]<S8<C5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(C6[j])+'\t S100 \n')
            if 2.75 < A2[i] < 3.25:
                Z = 3
                if (Z == C1[j]) and (C2[j]<S100<C3[j]) and (C4[j]<S8<C5[j]):
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(C6[j])+'\t S100 \n')
    ## Test for 24 ##
    
    if A6[i]!= 0 and A6[i]!= -99:
        #print(str(A1[i])+" YES")
        #print(A2[i])
        S24=log10(A6[i]/AA28[i])
        #print(S24)
        S8 = log10(AA28[i]/AA22[i])
        #print(S8)
        if S24 or S8 == nan:
            Outfile_C.write(str(int(A1[i]))+'\t nan \t undetection \n')
        for j in range(len(D1)):
            if 0.25 < A2[i] < 0.75:
                Z=0.5
                if (Z == D1[j]) and (D2[j]<S24<D3[j]) and (D4[j]<S8<D5[j]):
                    print(0.5)
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(D6[j])+'\t S24 \n')

            if 0.75 < A2[i] < 1.25:
                Z=1
                if (Z == D1[j]) and (D2[j]<S24<D3[j]) and (D4[j]<S8<D5[j]):
                    print(1)
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(D6[j])+'\t S24 \n') 
            if 1.25< A2[i] < 1.75:
                Z= 1.5
                if (Z == D1[j]) and (D2[j]<S24<D3[j]) and (D4[j]<S8<D5[j]):
                    print(1.5)
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(D6[j])+'\t S24 \n')                     
            if 1.75 < A2[i] < 2.25:
                Z = 2
                if (Z == D1[j]) and (D2[j]<S24<D3[j]) and (D4[j]<S8<D5[j]):
                    print(2)
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(D6[j])+'\t S24 \n')                    
            if 2.25 < A2[i] < 2.75:
                Z = 2.5
                if (Z == D1[j]) and (D2[j]<S24<D3[j]) and (D4[j]<S8<D5[j]):
                    print(2.5)
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(D6[j])+'\t S24 \n')                     
            if 2.75 < A2[i] < 3.25:
                Z = 3
                if (Z == D1[j]) and (D2[j]<S24<D3[j]) and (D4[j]<S8<D5[j]):
                    print(3)
                    Outfile_C.write(str(int(A1[i]))+'\t'+str(D6[j])+'\t S24 \n')                         
        
    else:
        Outfile_C.write(str(int(A1[i]))+'\t -99 \t nondetection \n')                        

'''


Outfile_C.close()







                    
