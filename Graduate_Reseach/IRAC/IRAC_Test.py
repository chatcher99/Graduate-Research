from __future__ import division
from math import *
from numpy import *
import numpy as np
import matplotlib.pyplot as plt



Outfile_XY=open("XY_Values_IRAC.txt",'w')
Outfile_AGNs=open("AGNs_IRAC.txt","w")



#ID,CH1,CH1ERR,CH2,CH2ERR,CH3,CH3ERR,CH4,CH4ERR = loadtxt('IRAC_ID_Channels.txt',unpack=True)


#A1 ID              A2 zbest                A3 M_med            A4 RA                   A5 DEC
#A6 IRAC_Ch1_FLUX   A7 IRAC_Ch1_FLUXERR     A8 IRAC_Ch2_FLUX    A9 IRAC_Ch2_FLUXERR
#A10 IRAC_Ch3_FLUX  A11 IRAC_Ch3_FLUXERR    A12 IRAC_Ch4_FLUX   A13 IRAC_Ch4_FLUXERR
#A14 f_IRAC_58      A15 f_IRAC_80           A16 f_MIPS24        A17 f_MIPS70
#A18 f_MIPS160      A19 f_PACS_100          A20 f_PACS_160      A21 f_SPIRE_250
#A22 f_SPIRE_350    A23 f_SPIRE_500 

A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23=loadtxt('Master_Flux_Catalog.txt',unpack=True)

ID=A1
CH1=A6
CH1ERR=A7
CH2=A8
CH2ERR=A9
CH3=A10
CH3ERR=A11
CH4=A12
CH4ERR=A13

XAGN=np.zeros([len(CH1)])   #AGNS
YAGN=np.zeros([len(CH1)])

XG=np.zeros([len(CH1)])   #Green
YG=np.zeros([len(CH1)])

XU=np.zeros([len(CH1)])   #Orange
YU=np.zeros([len(CH1)])

XSFG=np.zeros([len(CH1)])   #SFGS
YSFG=np.zeros([len(CH1)])

XX1=np.zeros([len(CH1)])    #Condition Lines
YY1=np.zeros([len(CH1)])
XX2=np.zeros([len(CH1)])
YY2=np.zeros([len(CH1)])

Outfile_AGNs.write("#ID \t Flag \n# 888 = AGN \t 111 = SFG \n\n\n" )

SIGMA1=np.std(CH1)
SIGMA2=np.std(CH2)
SIGMA3=np.std(CH3)
SIGMA4=np.std(CH4)

AGN=888
SFG=111


for i in range(len(CH1)):
    x = np.log10(CH3[i]/CH1[i])
    y = np.log10(CH4[i]/CH2[i])

    if (x >= 0.08) and (y >= 0.15) and (y >= ((1.21*x)-0.27)) and (y <= ((1.21*x)+0.27)):
        if (CH2[i] > CH1[i]) and (CH3[i] > CH2[i]) and (CH4[i] > CH3[i]): 
            #Outfile_XY.write(str(ID[i])+'\t'+str(round(x,5))+'\t'+str(round(y,5))+'\n')
            Outfile_XY.write("{:<15}{:<15}{:<15}\n".format(str(ID[i]),x,y))
            #Outfile_AGNs.write(str(ID[i])+'\t'+"AGN"+'\n')
            Outfile_AGNs.write("{:8}{:5}\n".format(str(int(ID[i])),str(int(AGN))))

            XAGN[i]=x
            YAGN[i]=y
        else:
            XG[i]=x
            YG[i]=y
            #print(str(ID[i])+'  XG: '+str(XG[i])+'   YG: '+str(YG[i]))
            #print('CH1: '+str(CH1[i])+'  CH2: '+str(CH2[i])+'  CH3: '+str(CH3[i])+'  CH4: '+str(CH4[i]))
    else:
        Outfile_XY.write(str(ID[i])+'\t'+str(round(x,5))+'\t'+str(round(y,5))+'\n')
        #Outfile_AGNs.write(str(ID[i])+'\t'+"SFG"+'\n')
        Outfile_AGNs.write("{:8}{:5}\n".format(str(int(ID[i])),str(int(SFG))))

        XSFG[i]=x
        YSFG[i]=y


    if (CH1[i]/CH1ERR[i] > 3*SIGMA1) and (CH2[i]/CH2ERR[i] > 3*SIGMA2) and (CH3[i]/CH3ERR[i] > 3*SIGMA2) and (CH4[i]/CH4ERR[i] > 3*SIGMA4): 
        XU[i]=x
        YU[i]=y


    if x<inf:
        yy1=(1.21*x)-0.27
        XX1[i]= x
        YY1[i]=yy1
        yy2=(1.21*x)+0.27
        XX2[i]= x
        YY2[i]=yy2

        
Outfile_XY.close()
Outfile_AGNs.close()

plt.scatter(XG,YG, s=5, c='red', label = 'Unclassifiable')
plt.scatter(XU,YU, s=5, c='red')
plt.scatter(XSFG,YSFG, s=5, c='blue', label='SFG')
plt.scatter(XAGN,YAGN, s=5, c='green', label='AGN')




plt.plot([0.08,0.08],[0.15,3],'k-', label='AGN Constraints')
plt.plot([0.08,3],[0.15,0.15],'k-')

plt.plot([0.3471,max(XX1)],[0.15,max(YY1)],'k-')
plt.plot([0.08,max(XX2)],[0.3668,max(YY2)],'k-')
plt.xlabel('log(S_5.8/S_3.6)')
plt.ylabel('log(S_8.0/S_4.5)')
plt.legend()
plt.show()

