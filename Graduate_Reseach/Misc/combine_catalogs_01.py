from __future__ import division
from math import *
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

#A1-90
# A1 Source       A2 z            A3 L(8-1000)    A4 er           A5 L(3-1100)    A6 er           A7 L1_1           A8 L1_2        A9 L1_3
# A10 L1_4        A11 L2_1        A12 L2_2        A13 L2_3        A14 L2_4        A15 L_008       A16 er            A17 L_012      A18 er
# A19 L_015       A20 er          A21 L_024       A22 er          A23 SFR_TIR     A24 er          A25 SFR_008       A26 er         A27 SFR_012
# A28 er          A29 SFR_015     A30 er          A31 SFR_024     A32 er          A33 SFRonly24   A34 SFR_R+09      A35 SFR_R+13   A36 SFR_E+11
# A37 er          A38 SFR_W+11    A39 SFR1600     A40 SFR2800     A41 UV_beta     A42 A(V)        A43 SFR1600c      A44 SFR2800c   A45 A(V)e
# A46 SFR1600ce   A47 SFR2800ce   A48 qPAH_DL+07  A49 Umin_DL+07  A50 gamma_DL+07 A51 Mdust_DL+07 A52 temp_1        A53 temp_2     A54 temp_3
# A55 temp_4      A56 temp_only24 A57 factor_1    A58 factor_2    A59 factor_3    A60 factor_4    A61 factor_only24 A62 F(24)      A63 R+09_valA
# A64 R+09_valB   A65 R+13_valA   A66 R+13_valB   A67 W+11_val    A68 l_IRAC_58   A69 f_IRAC_58   A70 l_IRAC_80     A71 f_IRAC_80  A72 l_MIPS24
# A73 f_MIPS24    A74 l_MIPS70    A75 f_MIPS70    A76 l_MIPS160   A77 f_MIPS160   A78 l_PACS_100  A79 f_PACS_100    A80 l_PACS_160 A81 f_PACS_160
# A82 l_SPIRE_250 A83 f_SPIRE_250 A84 l_SPIRE_350 A85 f_SPIRE_350 A86 l_SPIRE_500 A87 f_SPIRE_500 A88 plot_maxy     A89 Nfit       A90 Nobs 


# I Want
#A1 Source    A69 f_IRAC_58    A71 f_IRAC_80    A73 f_MIPS24    A75 f_MIPS70    A77 f_MIPS160
#A79 f_PACS_100    A81 f_PACS_160    A83 f_SPIRE_250    A85 f_SPIRE_350    A87 f_SPIRE_500


#Want All
#B1 ID   B2 zbest  B3 M_med   B4 RA   B5 DEC   B6 IRAC_Ch1_FLUX   B7 IRAC_Ch1_FLUXERR   B8 IRAC_Ch2_FLUX
#B9 IRAC_Ch2_FLUXERR   B10 IRAC_Ch3_FLUX   B11 IRAC_Ch3_FLUXERR   B12 IRAC_Ch4_FLUX   B13 IRAC_Ch4_FLUXERR

A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23,A24,A25,A26,A27,A28,A29,A30,A31,A32,A33,A34,A35,A36,A37,A38,A39,A40,A41,A42,A43,A44,A45,A46,A47,A48,A49,A50,A51,A52,A53,A54,A55,A56,A57,A58,A59,A60,A61,A62,A63,A64,A65,A66,A67,A68,A69,A70,A71,A72,A73,A74,A75,A76,A77,A78,A79,A80,A81,A82,A83,A84,A85,A86,A87,A88,A89,A90 = np.genfromtxt('Original Files/cosmos_candels_checkage_official.ir_fitting',dtype=float,filling_values=-99.99,unpack=True)
B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13=loadtxt('Original Files/cos_merged_v1.1_t1.txt',unpack=True)

Outfile_C=open("Master_Flux_Catalog.txt",'w')
Outfile_C.write('#1:ID \t 2:zbest \t 3:M_med \t 4:RA \t 5:DEC \t 6:IRAC_Ch1_FLUX \t 7:IRAC_Ch1_FLUXERR \t 8:IRAC_Ch2_FLUX \t 9:IRAC_Ch2_FLUXERR \t 10:IRAC_Ch3_FLUX \t 11:IRAC_Ch3_FLUXERR \t 12:IRAC_Ch4_FLUX \t 13:IRAC_Ch4_FLUXERR \t 14:f_IRAC_58 \t 15:f_IRAC_80 \t 16:f_MIPS24 \t 17:f_MIPS70 \t 18:f_MIPS160 \t 19:f_PACS_100 \t 20:f_PACS_160 \t 21:f_SPIRE_250 \t 22:f_SPIRE_350 \t 23:f_SPIRE_500 \n\n\n')

for i in range(len(B1)):
    if B3[i]>9.5:
        for j in range(len(A1)):
            if B1[i]==A1[j]:
                if A69[j] == 23:
                    A69[j] = 0.0
                if A71[j] == 23:
                    A71[j] = 0.0
                if A73[j] == 23:
                    A73[j] = 0.0
                if A75[j] == 23:
                    A75[j] = 0.0
                if A77[j] == 23:
                    A77[j] = 0.0
                if A79[j] ==23:
                    A79[j] = 0.0
                if A81[j] == 23:
                    A81[j] = 0.0
                if A83[j] == 23:
                    A83[j] = 0.0
                if A85[j] == 23:
                    A85[j] = 0
                if A87[j] ==23:
                    A87[j] = 0.0
                '''
                Outfile_C.write(str(B1[i])+'\t'+str(B2[i])+'\t'+str(B3[i])+'\t'+str(B4[i])+'\t'+str(B5[i])+'\t'
                    +str(B6[i])+'\t'+str(B7[i])+'\t'+str(B8[i])+'\t'+str(B9[i])+'\t'+str(B10[i])+'\t'+str(B11[i])+'\t'
                    +str(B12[i])+'\t'+str(B13[i])+'\t'+str(A69[j])+'\t'+str(A71[j])+'\t'+str(A73[j])+'\t'+str(A75[j])+'\t'
                    +str(A77[j])+'\t'+str(A79[j])+'\t'+str(A81[j])+'\t'+str(A83[j])+'\t'+str(A85[j])+'\t'+str(A87[j])+'\n')
                '''
                Outfile_C.write("{:<8}{:<8}{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<12}{:<12}{:<12}{:<12}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}\n".format(str(int(B1[i])),str(B2[i]),str(B3[i]),str(B4[i]),str(B5[i]),
                                                                                                                                                                                    str(B6[i]),str(B7[i]),str(B8[i]),str(B9[i]),str(B10[i]),
                                                                                                                                                                                    str(B11[i]),str(B12[i]),str(B13[i]),str(A69[j]),str(A71[j]),
                                                                                                                                                                                    str(A73[j]),str(A75[j]),str(A77[j]),str(A79[j]),str(A81[j]),
                                                                                                                                                                                    str(A83[j]),str(A85[j]),str(A87[j])))
                
Outfile_C.close()






    
