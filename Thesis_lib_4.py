from __future__ import division
import sys
from math import*
import numpy as np
from numpy import*
import time
import datetime


def Theta_Find(num_pts):
    XX=[]
    for i in range(num_pts):                        #generate random x values for sine graph and scatter
        x=np.random.rand()*np.pi              #same x values for both sine scatter allows for easier comparison because we can now just focus on the discrpancies in Y values
        XX.append(x)
    Xsine=XX                                        #sort random values so that when plotting sin it will be correct
    Ysine=np.sin(Xsine)**3                       #generates y values for sin^3 graph

    YY=[]
    for t in range(len(Xsine)):                     #generates random y value for random scatter, for every X value. 
        y=np.random.rand()                   
        YY.append(y)

    Xscat=[]        
    Yscat=[]
    for i in range(len(YY)):                        #compares y values of scatter to y values of sin at cooresponding x values
        if YY[i]<= Ysine[i]:
            Yscat.append(YY[i])
            Xscat.append(Xsine[i])

    Theta=Xscat[0]
    return Theta



def Scatter_Vectors(K,Theta,Phi):
    Kxx=sin(Theta)*cos(Phi)
    Kyy=cos(Theta)
    Kzz=sin(Theta)*sin(Phi)
    
    Kdp=(Kxx,Kyy,Kzz)                                #Scatter Vector

    return np.array(Kdp)



def Scatter_EField(K,Kdp,Ep):
    L=np.cross(Kdp,Ep)                                 #vector orthoganal to the plane formed by E and KK
    
    Lx=L[0]
    Ly=L[1]
    Lz=L[2]

    Kxx=Kdp[0]
    Kyy=Kdp[1]
    Kzz=Kdp[2]

    Exx= (1/(1+(((Ly*(Kxx-(Lx*Kzz/Lz)))/(Lz*(Kyy-(Ly*Kzz/Lz))))+(Lx/Lz))**2+(-(Kxx-(Lx*Kzz/Lz))/(Kyy-(Ly*Kzz/Lz)))**2))**(1/2)
    Eyy= - Exx*(Kxx-(Lx*Kzz/Lz))/(Kyy-(Ly*Kzz/Lz))
    Ezz= (Exx/Lz)*((Ly*(Kxx-(Lx*Kzz/Lz))/(Kyy-(Ly*Kzz/Lz)))-Lx)

    Edp=np.array([Exx,Eyy,Ezz])
    Edp=Edp/np.sqrt(np.sum(Edp**2))                                   #E field of propogation
    return Edp



def RotateX(E,Sigma):   #Clockwise Rotation about X
    Rotate=np.matrix([[1,0,0],[0,np.cos(Sigma),-np.sin(Sigma)],[0,np.sin(Sigma),np.cos(Sigma)]])
    Erotate=E*Rotate
    Erotate2=np.empty(3)
    Erotate2[0]=Erotate[0,0]
    Erotate2[1]=Erotate[0,1]
    Erotate2[2]=Erotate[0,2]

    return Erotate2



def RotateY(E,Phi):     #Clockwise Rotation about Y
    Rotate=np.matrix([[np.cos(Phi),0,np.sin(Phi)],[0,1,0],[-np.sin(Phi),0,np.cos(Phi)]])
    Erotate=E*Rotate
    Erotate2=np.empty(3)
    Erotate2[0]=Erotate[0,0]
    Erotate2[1]=Erotate[0,1]
    Erotate2[2]=Erotate[0,2]

    return Erotate2



def RotateZ(E,Theta):   #Clockwise Rotation about Z
    Rotate=np.matrix([[np.cos(Theta),-np.sin(Theta),0],[np.sin(Theta),np.cos(Theta),0],[0,0,1]])
    Erotate=E*Rotate
    Erotate2=np.empty(3)
    Erotate2[0]=Erotate[0,0]
    Erotate2[1]=Erotate[0,1]
    Erotate2[2]=Erotate[0,2]

    return Erotate2


def EllipCloud(Theta,Phi,SemiMajor,SemiMinor,Height):
    #outer radii of ellipitcal cloud
    X=SemiMajor*np.outer(np.cos(Phi),np.sin(Theta))
    Y=SemiMinor*np.outer(np.ones(np.size(Phi)),np.cos(Theta))
    Z=Height*np.outer(np.sin(Phi),np.sin(Theta))

    R=(X**2+Y**2+Z**2)**(1/2)
    
    return R


def Photon_Propagation(Lambda):
    # first we create the incoming propagation vector K and electric field E
    d=Lambda*(-np.log(np.random.rand()))       #distance traveled based on mean free path

    Theta = np.arccos((np.random.rand()*2)-1)  #randomly generate direction of photon
    Phi = np.random.uniform(-1,1)*np.pi #np.random.rand()*2*np.pi-np.pi#
    ThetaPrime = np.pi/2 - Theta
    Sigma = np.random.rand()*(pi)                   #generating random angle of E prop. 

    k=np.array([d,0,0])
    kk=RotateZ(k,-ThetaPrime)
    K=RotateY(kk,Phi)

    e=array([0,cos(Sigma),sin(Sigma)])
    ee= RotateZ(e,-ThetaPrime)
    E= RotateY(ee,Phi)

    return K,E,Theta,Phi


def Compton_Scatter(K,E,Lambda):
    #Find angles
    Theta = np.arctan2(np.sqrt(K[0]**2+K[2]**2),K[1])
    ThetaPrime = np.pi/2 - Theta
    Phi=np.arctan2(K[2],K[0])

    ee = RotateY(E,-Phi)
    e= RotateZ(ee,ThetaPrime)
    Sigma = np.arctan2(e[2],e[1])
    
    # we then rotate the frames so that the electric field is in the y direction
    Ep= RotateX(e,Sigma)

    kk=RotateY(K,-Phi)
    k=RotateZ(kk,ThetaPrime)
    Kp = RotateX(k,Sigma)

    # we now generate the scattering angles  
    ThetaScat = Theta_Find(100)                           #Theta is off of y axis in xy plane (probability proportional to Theta^3)
    PhiScat = np.random.uniform(-1,1)*np.pi                       #Phi is off of x axis in xz plane (Randomly generated)

    #Find Scattered vectors
    d=Lambda*(-np.log(np.random.rand()))       #distance traveled based on mean free path
    Kdp = d*Scatter_Vectors(Kp,ThetaScat,PhiScat)
    Edp=Scatter_EField(K,Kdp,Ep)
    
    #Counter rotate scattered EField and vector
    Etp=RotateX(Edp,-Sigma)
    Ktp=RotateX(Kdp,-Sigma)

    #Counter Rotate by ThetaPrime and Phi
    kk = RotateZ(Ktp,-ThetaPrime)
    KF= RotateY(kk,Phi)
    ee = RotateZ(Etp,-ThetaPrime)
    EF= RotateY(ee,Phi)

    return KF, EF



def Cloud_Scatter(nph,SemiMajor,SemiMinor,Height,Lambda,runID,NumD,DoF):
    outfile_E=open('DATASETS/Scatter_E_Fields_a='+runID+'.dat','w')
    outfile_K=open('DATASETS/Scatter_Vectors_a='+runID+'.dat','w')
    outfile_S=open('DATASETS/Scatter_Count_a='+runID+'.dat','w')

    Detect=np.zeros((NumD,3))   #Array of detector coordinates

    DetectD=np.zeros((NumD))       #Degrees at which detectors are located
    OutFiles_KD = {}
    OutFiles_ED = {}
    OutFiles_SD = {}
    for n in range(0,NumD):
        DetectD[n] = n*90/(NumD-1)
        Detect[n] = np.array([np.cos(n*np.pi/((NumD*2)-2)),0,np.sin(n*np.pi/((NumD*2)-2))])

        OutFiles_KD[n] = "outfile_DetK"+str(n)
        OutFiles_KD[n] = open('DATASETS/Detector_Vectors_'+str(DetectD[n])+'_a='+runID+'.dat','w')

        OutFiles_ED[n] = "outfile_DetE"+str(n)
        OutFiles_ED[n] = open('DATASETS/Detector_EFields_'+str(DetectD[n])+'_a='+runID+'.dat','w')

        OutFiles_SD[n] = "outfile_DetS"+str(n)
        OutFiles_SD[n] = open('DATASETS/Detector_Scatter_Counter_'+str(DetectD[n])+'_a='+runID+'.dat','w')

    timeStart = time.time()

    for p in range(nph):

        if p==100: 
            time100=time.time()
            print ('>>>')
            print ('I have now run 100 photons. It took me ',time100-timeStart,' seconds')
            print ('I evaluate it will take me ',(time100-timeStart)/100*nph,' seconds to finish')
            print ('This is ',((time100-timeStart)/100*nph)/60,' minutes')
            print ('This is ',((time100-timeStart)/100*nph)/60/60,' hours')
            print ('To scatter and determine which detector was hit')
        if p==1000: 
            time1000=time.time()
            print ('>>>')
            print ('I have now run 1000 photons. It took me ',time1000-timeStart,' seconds')
            print ('I evaluate it will take me ',(time1000-timeStart)/1000*nph,' seconds to finish')
            print ('This is ',(time1000-timeStart)/1000*nph/60,' minutes')
            print ('This is ',(time1000-timeStart)/1000*nph/60/60,' hours')
            print ('To scatter and determine which detector was hit')
        if p==10000: 
            time10000=time.time()
            print ('>>>')
            print ('I have now run 10000 photons. It took me ',time10000-timeStart,' seconds')
            print ('I evaluate it will take me ',(time10000-timeStart)/10000*nph,' seconds to finish')
            print ('This is ',(time10000-timeStart)/10000*nph/60,' minutes')
            print ('This is ',(time10000-timeStart)/10000*nph/60/60,' hours')
            print ('To scatter and determine which detector was hit')
        if p==100000: 
            time100000=time.time()
            print ('>>>')
            print ('I have now run 100000 photons. It took me ',time100000-timeStart,' seconds')
            print ('I evaluate it will take me ',(time100000-timeStart)/100000*nph,' seconds to finish')
            print ('This is ',(time100000-timeStart)/100000*nph/60,' minutes')
            print ('This is ',(time100000-timeStart)/100000*nph/60/60,' hours')
            print ('To scatter and determine which detector was hit')
            print ('>>>')
        K,E,Theta,Phi = Photon_Propagation(Lambda)      #Create Initial Propagation Vector
        R=EllipCloud(Theta,Phi,SemiMajor,SemiMinor,Height)[0,0]                  #Radius of cloud at angle of propagation
        
        X=K[0]
        Y=K[1]
        Z=K[2]
        D=np.linalg.norm(K)                     #Distance from orgin

        i=0

        while D<=R:
            KF,EF = Compton_Scatter(K,E,Lambda)

            X=X+KF[0]
            Y=Y+KF[1]
            Z=Z+KF[2]
            D=(X**2+Y**2+Z**2)**(1/2)

            #find angles D is away from axes
            ThetaR=np.arctan2(np.sqrt(X**2+Z**2),Y)#(np.arccos(Y/D)
            PhiR = np.arctan2(Z,X)
            R=EllipCloud(ThetaR,PhiR,SemiMajor,SemiMinor,Height)[0,0]      #Radius at angle of scatter
            
            ## Reset Vectors ##
            K=KF
            E=EF
            
            i+=1

        writestring_S=str(i)+'\n'

        ###Find angle photon is from x axis
        Chi = np.arccos((np.dot(K,np.array([1,0,0])))/(1*np.linalg.norm(K)))

        ###Determine which detector was hit
        for n in range(0,NumD):
            ChiD=np.degrees(Chi)
            DetLength=np.linalg.norm(Detect[n])

            VectLength=np.linalg.norm(K)
            a=(np.dot(K,Detect[n]))/(DetLength*VectLength)
            omega=np.arccos(a)
            
            if omega <= np.deg2rad(DoF):
                writestring_KD = str(K[0])+'\t'+str(K[1])+'\t'+str(K[2])+'\n'
                writestring_ED = str(E[0])+'\t'+str(E[1])+'\t'+str(E[2])+'\n'
                if i == 0:
                    writestring_SD=str(i)+'\n'
                else:
                    writestring_SD=str(i-1)+'\n'

                OutFiles_KD[n].write(writestring_KD)       
                OutFiles_ED[n].write(writestring_ED)
                OutFiles_SD[n].write(writestring_SD)

        #create files to store vector data
        writestring_K=str(K[0])+'\t'+str(K[1])+'\t'+str(K[2])+'\n'
        writestring_E=str(E[0])+'\t'+str(E[1])+'\t'+str(E[2])+'\n'

        outfile_K.write(writestring_K)
        outfile_E.write(writestring_E)
        outfile_S.write(writestring_S)

        
    outfile_E.close()
    outfile_K.close()
    outfile_S.close()
    
    for n in range(0,NumD):
        OutFiles_KD[n].close()
        OutFiles_ED[n].close()
        OutFiles_SD[n].close()

    return DetectD, Detect



def EField_Comps(Detect,nph,runID,DetectD):
    #print('n: '+str(n))
    #Select Vectors in Direction of Detector
    Ex,Ey,Ez=loadtxt('DATASETS/Detector_EFields_'+str(DetectD)+'_a='+runID+'.dat',unpack=True)

    #Find EField Compents in Detector Reference Frame
    outfile_EC=open('DATASETS/EField_Comps_'+str(DetectD)+'_a='+runID+'.dat','w')
    
    D=Detect
    #print('D: '+str(D))
    XD=np.array((1/(D[0]**2+D[1]**2+D[2]**2))**(1/2)*D)                                        #direction of detector=xaxis of detector reference frame=line through back of detector
    YD=np.array([0,1,0])
    ZD=RotateY(XD,np.pi/2)

    for i in range(Ex.size):
        E=(Ex[i],Ey[i],Ez[i])
        #print(E)
        #print(XD)
        Ecx=np.dot(E,XD)/np.linalg.norm(XD)
        Ecy=np.dot(E,YD)/np.linalg.norm(YD)
        Ecz=np.dot(E,ZD)/np.linalg.norm(ZD)

        writestring_EC=str(Ecx)+'\t'+str(Ecy)+'\t'+str(Ecz)+'\n'
        outfile_EC.write(writestring_EC)

    outfile_EC.close()
    return 



def Stokes(EFieldComps,runID,DetectD):
    #Calculate componets of Efields on each axis
    Ecx,Ecy,Ecz=loadtxt('DATASETS/EField_Comps_'+str(DetectD)+'_a='+runID+'.dat', unpack=True)
        
    a=array([sqrt(2),sqrt(2)])/2          #rotates axes
    b=array([sqrt(2),-sqrt(2)])/2

    EZ=np.zeros([Ecx.size])
    EY=np.zeros([Ecx.size])
    Ea=np.zeros([Ecx.size])
    Eb=np.zeros([Ecx.size])
        
    for i in range(Ecx.size):
        Ec=array([Ecy[i], Ecz[i]])

        EZ[i]=Ecz[i]
        EY[i]=Ecy[i]

        Ea[i]=np.dot(Ec,a)
        Eb[i]=np.dot(Ec,b)

    #Compute Stokes Parameters
    EZ2=EZ**2
    EY2=EY**2
    Ea2=Ea**2
    Eb2=Eb**2

    I=sum(EZ2)/Ecx.size + sum(EY2)/Ecx.size
    Q=sum(EZ2)/Ecx.size - sum(EY2)/Ecx.size
    U=sum(Ea2)/Ecx.size - sum(Eb2)/Ecx.size
    P=np.sqrt(Q**2+U**2)/I

    Error=1/(len(Ecx)**(1/2))

    return P,Error


def Gen_Plot_Data(nph,NumD,DoF,alpha,runID,SemiMajor,SemiMinor,Height):
    TimeStamp1=time.time()
    StartTime=datetime.datetime.fromtimestamp(TimeStamp1).strftime('%m-%d-%Y  %H:%M')
    print("START TIME: "+str(StartTime))

    runID=str(alpha)

    Lambda=SemiMajor/alpha

    outfile_A=open('PLOTDATA/ANGLE_'+str(SemiMajor)+'_'+str(SemiMinor)+'_'+str(Height)+'_a='+runID+'.dat','w')
    outfile_P=open('PLOTDATA/POLAR_'+str(SemiMajor)+'_'+str(SemiMinor)+'_'+str(Height)+'_a='+runID+'.dat','w')
    outfile_Er=open('PLOTDATA/ERROR_'+str(SemiMajor)+'_'+str(SemiMinor)+'_'+str(Height)+'_a='+runID+'.dat','w')
    outfile_S = open('PLOTDATA/AVG_SCAT_'+str(SemiMajor)+'_'+str(SemiMinor)+'_'+str(Height)+'_a='+runID+'.dat','w')
    
    DetectD, Detect=Cloud_Scatter(nph,SemiMajor,SemiMinor,Height,Lambda,runID,NumD,DoF)

    x = np.array([1,0,0])       

    timeStart = time.time()

    for n in range(0,NumD):                         # Itterate through detector locations based on angle from x axis
        Angle=np.arccos((np.dot(x,Detect[n])/(np.linalg.norm(x)*np.linalg.norm(Detect[n]))))
        Polar,Error=Stokes(EField_Comps(Detect[n],nph,runID,DetectD[n]),runID,DetectD[n])

        writestring_A=str(Angle)+'\n'
        writestring_P=str(Polar)+'\n'
        writestring_Er=str(Error)+'\n'

        outfile_A.write(writestring_A)
        outfile_P.write(writestring_P)
        outfile_Er.write(writestring_Er)

        if n==0:
            timeN=time.time()
            print('>>>')
            print('I have analyized EFields and Polarization at 1 detector')
            print('It took ', timeN-timeStart,' seconds')
            print('I evaluate it will take me ',(timeN-timeStart)*NumD,' to analyze all detectors')
            print('This is ',(timeN-timeStart)*NumD/60,' minutes')
            print('This is ',(timeN-timeStart)*NumD/60/60,' hours')

        Sum1=sum(int(s.strip()) for s in open('DATASETS/Detector_Scatter_Counter_'+str(DetectD[n])+'_a='+runID+'.dat'))
        average1=Sum1/len(open('DATASETS/Detector_Scatter_Counter_'+str(DetectD[n])+'_a='+runID+'.dat').readlines())
        Photons1=len(open('DATASETS/Detector_Scatter_Counter_'+str(DetectD[n])+'_a='+runID+'.dat').readlines())
        print('Polarization at Detect'+str(n)+' = '+str(Polar))
        

    outfile_A.close()
    outfile_P.close()
    outfile_Er.close()

    Sum2=sum(int(s.strip()) for s in open('DATASETS/Scatter_Count_a='+runID+'.dat'))
    average2=Sum2/len(open('DATASETS/Scatter_Count_a='+runID+'.dat').readlines())
    print('\n'+'Average Overall Scatter = '+str(average2))

    writestring_S=str(average2)
    outfile_S.write(writestring_S)
    outfile_S.close()

    TimeStamp2=time.time()
    EndTime=datetime.datetime.fromtimestamp(TimeStamp2).strftime('%m-%d-%Y  %H:%M')
    print("END TIME: "+str(EndTime))

    return
