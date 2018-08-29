from __future__ import division
from math import *
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

# A1 X_ID   A2 H_ID         A3 hRA      A4 hDEC     A5 xRA      A6 xDEC     A7 Class
# A8 LR     A9 xFLUX(Full)  A10 zbest   A11 FullLx  A12 SoftLx  A13 HardLx  A14 FlagAGN

A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14=loadtxt('xray_counterparts.COS.080116.txt',unpack=True)

Outfile_X=open('XRay_Counterparts.txt','w')
Outfile_X.write('#ID \t Full Lx \t Soft Lx \t Hard Lx \t FlagAGN \n # 888 = AGN 111 = SFG \n\n')

AGN = 888
SFG = 111

for i in range(len(A2)):
    if (A11[i] or A12[i] or A13[i]) > 42:
        Outfile_X.write("{:8}{:12}{:12}{:12}{:12}\n".format(str(int(A2[i])),str(A11[i]),str(A12[i]),str(A13[i]),str(AGN)))
    else:
        Outfile_X.write("{:8}{:12}{:12}{:12}{:12}\n".format(str(int(A2[i])),str(A11[i]),str(A12[i]),str(A13[i]),str(SFG)))
Outfile_X.close()
