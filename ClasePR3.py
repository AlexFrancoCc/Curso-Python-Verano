## MATRICES COMO UNA LISTA DE LISTAS
#============================================================
matriz = [[4,1,-3],[2,4.4,0],[-5,9,198],[2,4,-5]]
# print(matriz)

# for j in range(3):
#    for i in range(4):
#        print(matriz[i][j])

# len(matriz)
# len(matriz[0])

# for j in range(len(matriz[0])):
#    for i in range(len(matriz)):
#        print(matriz[i][j])

# Creando una matriz en forma interactiva n x n
n = 5
M = []
for i in range(n):
    F = []
    for j in range(n):
      F.append(0)
    M.append(F)
print(M)

# Creando ua matriz en forma interactiva n x n
n = 5
m = 3
M = []
for i in range(n):
    F = []
    for j in range(m):
        F.append(j)
    M.append(F)
print(M)   

# Otra forma de hacer lo mismo
n = 5
M = []
for i in range(n):
  M.append([4]*n)  # AGREGA EL 0 n=5 veces 
print(M)

#***  Usando la biblioteca NUMPY
#import numpy      # Carga el paquete
#A = numpy.matrix([[1,2,-5],[3,4,3.3]])
#print(A)   

## ********* DATA FRAMES (DICCIONARIO DE DATOS)
# paquetes panda
import pandas as pd
datos = {'name':['Luis','Maria','Pepe'],'ciudad':['San jose','Lisa','Buenos Aires'],
         'Edad':[23,56,12]}




