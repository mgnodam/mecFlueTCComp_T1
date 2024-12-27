import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections
import matplotlib.cm as cm
import mesh_check as mc
import pandas as pd
from math import *

# DEFININDO CONTORNOS DA SIMULACAO

lf = 5   # Comprimento à frente
lb = 15  # Comprimento atrás

h = 10

# DEFININDO PARAMETROS

eSizeEdges = 1.0
eSizeAirf = 0.1

# DEFININDO PONTOS DO PERFIL

airfoil = np.array(pd.read_csv("n0012.csv" , sep = ';'))

airfPoints = []

for line in airfoil:
    airfPoints.append([line[0] , line[1]])

# CONSTRUINDO A GEOMETRIA

    # Pontos
pointsStr = ''

pointsStr += "Point({:.0f})".format(1) + " = {" + "{:.3f}, {:.3f}, {:.3f}, {:.3f}".format(-lf,-h/2,0,eSizeEdges) +"};\n"
pointsStr += "Point({:.0f})".format(2) + " = {" + "{:.3f}, {:.3f}, {:.3f}, {:.3f}".format(lb,-h/2,0,eSizeEdges) +"};\n"
pointsStr += "Point({:.0f})".format(3) + " = {" + "{:.3f}, {:.3f}, {:.3f}, {:.3f}".format(lb,h/2,0,eSizeEdges) +"};\n"
pointsStr += "Point({:.0f})".format(4) + " = {" + "{:.3f}, {:.3f}, {:.3f}, {:.3f}".format(-lf,h/2,0,eSizeEdges) +"};\n"

for i in range(len(airfPoints)-1):  #-1 porque o último ponto é o primeiro
    airfStr = "Point({:.0f})".format(i+5) + " = {" + "{:.6f}, {:.6f}, {:.6f}, {:.6f}".format(airfPoints[i][0],airfPoints[i][1],0,eSizeAirf) +"};\n"
    pointsStr += airfStr
    
    # Linhas
linesStr= '\n'

for i in range(1,5):
    contourLinesStr= "Line({:.0f})".format(i) + " = {" + "{:.0f}, {:.0f}".format(i,i%4 + 1) +"};\n" #Usando o resto para voltar ao ponto 1
    linesStr += contourLinesStr
    
for i in range(1,len(airfPoints)):
    airfLinesStr= "Line({:.0f})".format(i+4) + " = {" + "{:.0f}, {:.0f}".format(i+4,i%(len(airfPoints)-1) + 5) +"};\n"  #Usando o resto para voltar ao ponto inicial, o +4 vem dos 4 pontos do contorno
    linesStr += airfLinesStr
    
    # Curvas
    
curvesStr = '\n'

contourCurves = ''
airfCurves = ''

for i in range(1,5):
    contourCurves += '{}, '.format(i)

for i in range(1,len(airfPoints)):
    airfCurves += '{}, '.format(i+4)
    
contourCurveStr = "\nLine Loop(1) = {" + contourCurves[0:(len(contourCurves)-2)] + "};\n"   #Retirando espaço e vírgula dos últimos
airfCurveStr = "\nLine Loop(2) = {" + airfCurves[0:(len(airfCurves)-2)] + "};\n"            #Retirando espaço e vírgula dos últimos

curvesStr= contourCurveStr + airfCurveStr

    # Áreas
    
areaStr = "\nPlane Surface (1) = {1, 2};\n"

# DEFININDO ELEMENTOS DE MALHA

    # Condições de contorno

contourCondStr = '\n'

contourCondStr += 'Physical Line("wall",' + ' {}'.format(len(airfPoints) + 4) + ') = {1, 3, ' + airfCurves[0:(len(airfCurves)-2)] + "};\n"

contourCondStr += 'Physical Line("inflow",' + ' {}'.format(len(airfPoints) + 5) + ') = {4};\n'

contourCondStr += 'Physical Line("outflow",' + ' {}'.format(len(airfPoints) + 6) + ') = {2};\n'

contourCondStr += 'Physical Surface("sur",' + ' {}'.format(len(airfPoints) + 7) + ') = {1};\n'

    # Recombinando
    
recombineStr=''

#recombineStr= "\nRecombine Surface {1};"

# JUNTANDO AS CONSTRUÇÕES
    
meshStr = pointsStr + linesStr + curvesStr + areaStr + contourCondStr + recombineStr

# ESCREVENDO O ARQUIVO GEO

with open('msh.geo', 'w') as mesh:
    mesh.write(meshStr)