import numpy as np

# Ejemplo con numpy.full
shape_full = (3, 4) #dimension
valor_llenado = 5
array_full = np.full(shape_full, valor_llenado)

print("Array creado con numpy.full:")
print(array_full)
print()

# Ejemplo con numpy.empty
shape_empty = (3, 4)
array_empty = np.empty(shape_empty)

print("Array creado con numpy.empty (sin inicializar):")
print(array_empty)