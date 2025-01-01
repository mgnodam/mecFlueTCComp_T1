import meshio
import numpy as np
import matplotlib.pyplot as plt
import mesh_check as mc
from math import *

msh = meshio.read('./gmsh/mshTri.msh')

X = msh.points[:,0]
Y = msh.points[:,1]

IEN = msh.cells[1].data
IENbound = msh.cells[0].data

IENboundTypeElem = list(msh.cell_data['gmsh:physical'][0] - 1)

boundNames= list(msh.field_data.keys())

#IENboundElem = [boundNames[elem] for elem in IENboundTypeElem]

IENboundElemNames = []

for i in IENboundTypeElem:
    if i == 4:
        IENboundElemNames.append(boundNames[0])
    if i == 5:
        IENboundElemNames.append(boundNames[1])
    if i == 6:
        IENboundElemNames.append(boundNames[2])
    if i == 7:
        IENboundElemNames.append(boundNames[3])

area = []
max_angles= []
aspectR=[]
neighbours=[]

for e in IEN:
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
    for pn in IEN: #potential neighbour
        vic=0           #vertices in common
        for ve in e:
            for vn in pn:    #vertice
                if ve == vn:
                    vic+=1
        
        if vic == 2:
            neighbours_e+=1

    neighbours.append(neighbours_e)

sumArea= np.sum(area)
print("Área total=", sumArea)

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