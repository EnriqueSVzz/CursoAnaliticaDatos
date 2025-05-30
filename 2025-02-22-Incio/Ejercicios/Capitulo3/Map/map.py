#Definimos nuestra lista
numeros = [1, 2, 3, 4, 5]

# Función que eleva al cuadrado
def cuadrado(x):
    return x ** 2

resultado = map(cuadrado, numeros)
print(list(resultado))  # [1, 4, 9, 16, 25]

numeros = [1, 2, 3, 4, 5]

resultado = map(lambda x: x ** 2, numeros)
print(list(resultado))  # [1, 4, 9, 16, 25]

valores = ["1", "2", "3", "4"]
numeros = list(map(int, valores))  # Convierte a enteros
print(numeros)  # [1, 2, 3, 4]