'''
Crea una matriz 3x3 y súmale un valor constante de 5.
Multiplica una matriz 3x3 por un vector de 3 elementos.
'''
import numpy as np

# Matrices de ejemplo
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[9,8,7],[6,5,4],[3,2,1]])

print(f'Matriz Original A:\n{a}')
print(f'Matriz Original B:\n{b}')

# Suma de Matrices
c = a + b
print(f'Usando el Operador +:\n{c}')
c = np.add(a,b)
print(f'Usanndo el metodo add:\n{c}')

# Multiplicación de matrices
d = np.dot(a,b)
print(f'Multiplicacion:\n{c}')

#Acceder un atributo de la matriz
print(f' Primer Elemento de A:\n{a[0][1]}')  # Accede al elemento en la primera fila, segunda columna
print(f' Primera Fila:\n{a[0]}')     # Devuelve toda la primera fila de la matriz.

# Transponer una matriz (intercambiar filas x Columnas)
e = a.T
print(f'Matriz Transpuesta:\n{e}')

# Ordenar una fila de una matriz
indice_de_orden = np.argsort(a[:, 1])
matriz_ordenada = a[indice_de_orden, :]
print(f'Matriz ordenada:\n{matriz_ordenada}')

#Filtrado de Datos
mascara = a[:, 0] > 3
filtrado = a[mascara, :]
print(f'Filtrado >3:\n{filtrado}')

# Sumar una constante 5 a A.
f = a + 5
print(f'Suma de una constante:\n{f}')

#Multiplicando por un vector unitario
vector = np.array([1, 2, 3])
g = a * vector
print(f'Multiplicacion por un vector:\n{g}')
