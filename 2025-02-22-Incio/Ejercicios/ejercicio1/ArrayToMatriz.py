'''
Convierte un array 1D de tamaño 12 en una matriz de 3x4.
Convierte una matriz 2D en un array de 1D.
'''
import numpy as np
# Creamos un array 1D de tamaño 12
arr_1d = np.arange(12)
# Convertimos el array 1D en una matriz de 3x4
arr_2d = arr_1d.reshape(3, 4)

print(f'Array Unidimensional<12>: {arr_1d}')
print(f'Array Bidimensional<3,4>: {arr_2d}') 

arr_3d = arr_2d.reshape(12)
print(f'Array Unidimensional<12,1>: {arr_3d}') 