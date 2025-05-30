'''
Una matriz 3x3 de números aleatorios entre 0 y 1.
https://keepcoding.io/blog/como-definir-matrices-en-python/
'''
import numpy as np

#En escencia, la matriz es un arreglo de arreglos,
#donde cada elemento es un número aleatorio entre 0 y 1.

# Ejemplo 1.
A = [[1,  0,  0],
    [0,  1,  0],
    [0,  0,  1]]

print (A)
print (type (A))

#Ejemplo 2.
B= np.array ([[1,  0,  0], [0,  1,  0], [0,0,1]])
print(B)
print(type(B))

#Ejemplo 3
# Redondiamos a un solo decimal
# Como la Distribución normal son valores del 0 al 1, se usó esta forma
C = np.round(np.random.rand(3, 3))
print(C)
print(type (C))

#Ejemplo 4
# Usando una distribición uniforme
D = np.random.uniform(0, 1, (3, 3))
print(D)
print(type (D))

#Ejemplo 5
# Usando una distribición normal redondeada
E= np.random.random_sample((3, 3))
print(E)
print(type (E))

#Ejemplo6
#Función para matriz identidad.
F = np.eye (3,  3)
print(F)
print(type(F))