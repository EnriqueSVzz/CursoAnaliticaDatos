import numpy as np
import matplotlib.pyplot as plt 

# Generar un número aleatorio entre 0 y 1
random_number = np.random.random()
print("Número aleatorio entre 0 y 1:", random_number)

# Generar un arreglo de 5 números aleatorios entre 0 y 1
random_array = np.random.random(5)
print("Arreglo de números aleatorios:", random_array)

# Generar un número entero aleatorio entre 1 y 10
random_integer = np.random.randint(1, 11)
print("Número entero aleatorio entre 1 y 10:", random_integer)

# Arreglo original
original_array = np.array([1, 2, 3, 4, 5])

# Permutar el arreglo aleatoriamente
shuffled_array = np.random.permutation(original_array)
print("Arreglo original:", original_array)
print("Arreglo permutado:", shuffled_array)

# Generar 1000 números aleatorios con distribución normal (media=0, desviación estándar=1)
random_numbers = np.random.normal(0, 1, 1000)

# Visualizar el histograma de los números generados
plt.hist(random_numbers, bins=50, density=True, alpha=0.7, color='blue')
plt.title('Histograma de Distribución Normal')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()

