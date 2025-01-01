import meshio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections
import matplotlib.cm as cm
import mesh_check as mc
import pandas as pd
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
        

print(boundNames)

plt.triplot(X,Y,IEN)
plt.show()