from math import *
import numpy as np
import matplotlib.pyplot as plt

def areaTri(v1,v2,v3):

    "Calcula e retorna a área (float) de um triângulo dadas as coordenadas x,y de seus 3 vértices"

    side1= v2-v1
    side2= v3-v2

    area=np.linalg.norm(np.cross(side1,side2))/2

    return area

def anglesTri(v1,v2,v3):

    "Calcula e retorna os ângulos em radianos (lista de floats) de um triângulo dadas as coordenadas x,y de seus 3 vértices"

    side1= v2-v1
    side2= v3-v2
    side3= v1-v3

    angle1= acos(np.dot(side1,-side3)/(np.linalg.norm(side1)*np.linalg.norm(side3)))
    angle2= acos(np.dot(side1,-side2)/(np.linalg.norm(side1)*np.linalg.norm(side2)))
    angle3= acos(np.dot(side3,-side2)/(np.linalg.norm(side3)*np.linalg.norm(side2)))

    return [angle1, angle2, angle3]

def perimeterTri(v1,v2,v3):

    "Calcula e retorna o perímetro (float) de um triângulo dadas as coordenadas x,y de seus 3 vértices"

    side1= v2-v1
    side2= v3-v2
    side3= v1-v3

    perimeter= np.linalg.norm(side1) + np.linalg.norm(side2) + np.linalg.norm(side3)

    return perimeter

def radiusTriIn(v1,v2,v3):

    "Calcula e retorna o raio da circunferência inscrita (float) dadas as coordenadas x,y de seus 3 vértices"

    side1= v2-v1
    side2= v3-v2
    side3= v1-v3

    radius= (4*areaTri(v1,v2,v3))/perimeterTri(v1,v2,v3)

    return radius

def radiusTriOut(v1,v2,v3):

    "Calcula e retorna o raio da circunferência que circunscreve o triângulo (float) dadas as coordenadas x,y de seus 3 vértices"

    side1= v2-v1
    side2= v3-v2
    side3= v1-v3

    len1= np.linalg.norm(side1)
    len2= np.linalg.norm(side2)
    len3= np.linalg.norm(side3)

    radius= (len1*len2*len3)/(4*areaTri(v1,v2,v3))

    return radius

def aspectR(v1,v2,v3):

    "Calcula e retorna a razão de aspecto de um triângulo (float), dadas as coordenadas x,y de seus 3 vértices"

    ratio= radiusTriOut(v1,v2,v3)/radiusTriIn(v1,v2,v3)

    return ratio

def genTri(x1,x2,x3):

    "Calcula e retorna ? e plota ? de um triângulo dadas as coordenadas x de seus 3 vértices"

    y1= x1
    y2= -x2
    y3= x3

    v1= np.asarray((x1,y1))
    v2= np.asarray((x2,y2))
    v3= np.asarray((x3,y3))

    side1= v2-v1
    side2= v3-v2
    side3= v1-v3

    len1= np.linalg.norm(side1)
    len2= np.linalg.norm(side2)
    len3= np.linalg.norm(side3)

    radius= (len1*len2*len3)/(4*areaTri(v1,v2,v3))

    x=(x1,x2,x3)
    y=(y1,y2,y3)

    plt.plot(x,y)
    plt.show()

    return radius


    

#def neighbours(v1,v2,v3):

if __name__ == '__main__':

    print(radiusTriIn(np.array((-1,0)),np.array((1,0)),np.array((0,1))))
    print(radiusTriOut(np.array((-1,0)),np.array((1,0)),np.array((0,1))))


    #print(genTri(0.2,0.4,1))