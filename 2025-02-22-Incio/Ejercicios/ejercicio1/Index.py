# Soluciones problemario

#   Crea un array de 1D con los números del 0 al 9.
import numpy as np  # Asegúrate de importar numpy

# Usando listas
#Nota range empieza desde cero y el ultimo numero no cuenta
a = list(range(0, 9))
print(f'Array A con List: {a}') 

# Usando NumPy
b = np.arange(0, 9)
print(f'Array B con NumPy: {b}')