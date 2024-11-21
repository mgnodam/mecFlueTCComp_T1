import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections
import matplotlib.cm as cm
import mesh_check as mc
from math import *

# dados da malha
Lx = 1.0
Ly = 1.0
nx = 20
ny = 20
dx= Lx/nx
dy= Ly/ny
npoints = nx*ny
ne = (nx-1)*(ny-1) # quadrilateros

# gerando a distribuicao de pontos
Xv = np.linspace(0,Lx,nx)
Yv = np.linspace(0,Ly,ny)

for i in range(0,nx):
    Xv[i]= Lx*sin((Xv[i]/Lx)*(pi/2))

for i in range(0,ny):
    Yv[i]= Ly*sin((Yv[i]/Ly)*(pi/2))

X,Y = np.meshgrid(Xv,Yv)
X = np.reshape(X,npoints)
Y = np.reshape(Y,npoints)

import matplotlib.tri as mtri
tri = mtri.Triangulation(X,Y)
IENTriM = tri.triangles

# Calculando os parâmetros da malha
area = []
max_angles= []
aspectR=[]
neighbours=[]

for e in IENTriM:
    v1 = np.asarray([X[e[0]],Y[e[0]]])
    v2 = np.asarray([X[e[1]],Y[e[1]]])
    v3 = np.asarray([X[e[2]],Y[e[2]]])
    
    area_e= mc.areaTri(v1,v2,v3)
    max_angles_e= degrees(max(mc.anglesTri(v1,v2,v3)))
    aspectR_e= mc.aspectR(v1,v2,v3)

    area.append(area_e)
    max_angles.append(max_angles_e)
    aspectR.append(aspectR_e)

    neighbours_e=0
    for pn in IENTriM: #potential neighbour
        vic=0           #vertices in common
        for ve in e:
            for vn in pn:    #vertice
                if ve == vn:
                    vic+=1
        
        if vic == 2:
            neighbours_e+=1

    neighbours.append(neighbours_e)

sumArea= np.sum(area)
print(sumArea)

# plot da malha de triangulos
plt.triplot(X,Y,IENTriM,color='black')
plt.show()

#Verificações de qualidade de malha

plt.hist(area)
plt.title("Área do triângulo")
plt.show()

plt.hist(max_angles)
plt.title("Ângulo maior do triângulo")
plt.show()

plt.hist(aspectR)
plt.title("Razão de aspecto")
plt.show()

plt.hist(aspectR, 25, range=[0,30])
plt.title("Razão de aspecto")
plt.show()