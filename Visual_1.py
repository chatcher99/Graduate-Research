from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import mpl_toolkits.mplot3d.axes3d as p3
from Thesis_lib_2 import*

outfile_P=open('Path.dat','w')

####Define parameters####
a=30 #**10              #m semimajor x axis 
b=10 #**10                #m semiminor z axis axis
c=b                     #m semininor y axis

alpha = 0.5
Lambda = alpha*a       #R/T #Mean Free Path

K,E,Theta,Phi,d=Propagation(Lambda)         #Create Initial Propagation Vector
        
R=EllipCloud(Theta,Phi,a,b,c)[0,0]      #Radius of cloud at angle of propagation

X=K[0]
Y=K[1]
Z=K[2]

D=np.linalg.norm(K)                     #Distance from orgin

Sigma=np.random.rand()*(pi)             #Random angle for Efield 
E=array([0,cos(Sigma),sin(Sigma)])
        
i=0
        
while D < R:                            #Scatter Process
    writestring_P=str(K[0])+'\t'+str(K[1])+'\t'+str(K[2])+'\n'
    outfile_P.write(writestring_P)
    Kqp,Eqp,Zeta,Psi,d = ComptonScatter(K,E,Lambda,Theta,Phi)    #rotates K to (1,0,0) and E to (0,1,0) then scatters and counter rotates
    X=X+Kqp[0]
    Y=Y+Kqp[1]
    Z=Z+Kqp[2]
    D=(X**2+Y**2+Z**2)**(1/2)

    #find angle D is away from y axis now
    ThetaR=np.arccos(Y/D)

    #find angle D is away from x axis now
    if np.sign(X) == 1:
        if np.sign(Z) == 1:
            PhiR = np.arctan(Z/X)
        if np.sign(Z) == -1:
            PhiR =(3*np.pi/2)+np.abs(np.arctan(X/Z))
                
    if np.sign(X) == -1:
        if np.sign(Z) == 1:
            PhiR =(np.pi/2)+ np.abs(np.arctan(X/Z))
        if np.sign(Z) == -1:
            PhiR =(np.pi)+ np.arctan(Z/X)
    if np.sign(Z)==0:
        PhiR=0
    if np.sign(X)==0:
        PhiR=np.pi/2

    R=EllipCloud(ThetaR,PhiR,a,b,c)[0,0]      #Radius at angle of scatte
    #print("D: "+str(D))
    #print ("R: "+str(R))     
    K = Kqp
    E = Eqp
    Theta = Zeta
    Phi = Psi
    
    i+=1

writestring_P=str(K[0])+'\t'+str(K[1])+'\t'+str(K[2])+'\n'
outfile_P.write(writestring_P) 
outfile_P.close()

path=loadtxt('Path.dat',unpack=True)
print("Number of Scatters: "+str(path[0].size-1))
#print(path)
dims=3       #number of dimentions the line has

def Gen_Line(length,dims=2):
    lineData = np.empty((dims, length))
    lineData[:,0] = 0
    for i in range(1,length):
        lineData[:,i] = lineData[:,i-1] + path[:,i-1]
    #print(lineData)
    return lineData

def update_lines(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines

# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

#generate theoretical elliptical plot
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, np.pi, 50)

x = a * np.outer(np.cos(u),np.sin(v))
z = b * np.outer(np.sin(u), np.sin(v))
y = c * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_wireframe(x,y,z,color='r',alpha=0.1)

data = [Gen_Line(path[0].size+1, dims) for index in range(1)]
lines = [ax.plot(dat[0, 0:1], dat[1, 0:1],dat[2, 0:1])[0] for dat in data ]

# Setting the axes properties
ax.set_xlim3d([-20,20])
ax.set_xlabel('X')
ax.set_ylim3d([-20,20])
ax.set_ylabel('Y')
ax.set_zlim3d([-20,20])
ax.set_zlabel('Z')

ax.set_title('Cloud Scatter')

# Creating the Animation object
line_ani = animation.FuncAnimation(fig, update_lines, 40, fargs=(data, lines),interval=500, blit=False)

plt.show()

