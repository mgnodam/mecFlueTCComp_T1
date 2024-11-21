from math import *
import numpy as np
import matplotlib.pyplot as plt

# PArAMETROS INICIAIS 

lx= 1
nx= 4
dx= lx/nx

ly= 1
ny= 4
dy= ly/ny

npoints=nx*ny

#CRIACAO DA MALHA

x= np.linspace(0,lx,nx)
y= np.linspace(0,ly,ny)

x,y= np.meshgrid(x,y)

x= np.reshape(x,npoints)
y= np.reshape(y,npoints)

# CRIAÇÃO DA IEN

ne= (nx-1)*(ny-1)

ien= np.zeros((ne,4),dtype='int')

ien[0]= 0, 1, nx + 1, nx

for i in range(1,len(ien)):
    ien[i]= (i + (i)//(nx-1)), 1 + (i + (i)//(nx-1)), nx + 1 + (i + (i)//(nx-1)), nx + (i + (i)//(nx-1))

#PLOTAGEM DOS RESULTADOS

print(ien)

plt.plot(x,y,'ko')

for i in range(0,npoints):
    plt.text(x[i] + 0.01 , y[i] + 0.01 , str(i) , color='b')

plt.show()