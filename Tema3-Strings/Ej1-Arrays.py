import numpy as np

# Ejercicio 1: Crear un array unidimensional
print("Ejercicio 1:")
array_1d = np.array([1, 2, 3, 4, 5])
print("Array unidimensional:", array_1d)

# Ejercicio 2: Crear una matriz
print("\nEjercicio 2:")
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matriz:")
print(matriz)

# Ejercicio 3: Realizar operaciones en un array
print("\nEjercicio 3:")
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

suma = array_a + array_b
producto = array_a * array_b

print("Array A:", array_a)
print("Array B:", array_b)
print("Suma:", suma)
print("Producto:", producto)

# Ejercicio 4: Indexación y slicing
print("\nEjercicio 4:")
array_original = np.array([10, 20, 30, 40, 50])
print("Array original:", array_original)

# Obtener el elemento en la posición 2
elemento_posicion_2 = array_original[2]
print("Elemento en posición 2:", elemento_posicion_2)

# Obtener una porción del array
porcion_array = array_original[1:4]
print("Porción del array (posiciones 1 a 3):", porcion_array)

# Cambiar el valor en la posición 0
array_original[0] = 99
print("Array modificado:", array_original)