import numpy as np

# Crear un arreglo bidimensional 3 X 3
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Imprimir el arreglo
print("Arreglo:")
print(arr)

# Mostrar la forma del arreglo
print("\nForma del arreglo (dimensiones) (shape):", arr.shape)

# Mostrar el rango del arreglo ; Es 2 porque son filas y columnas.
print("Rango del arreglo (Dimension espacial) (rank):", arr.ndim)

# Mostrar el tamaño del arreglo
print("Tamaño del arreglo (total de espacios) (size):", arr.size)

# Acceder a elementos específicos utilizando índices y ejes
print("\nElemento en la fila 1, columna 2:", arr[1, 2])