'''
Sclicing
'''

# En cadenas
texto = "Python"
# Extraer desde el índice 0 al 3 (sin incluir el 3)
resultado = texto[0:3]
print(resultado)  # "Pyt"

# En Listas
numeros = [10, 20, 30, 40, 50, 60]
# Extraer los elementos desde el índice 1 al 4
resultado = numeros[1:4]
print(resultado)  # [20, 30, 40]
# Extraer cada dos elementos
resultado = numeros[::2]
print(resultado)  # [10, 30, 50]

# Extraer los últimos 3 elementos
# Que empiece en el index -3 y corte hasta el final de la cadena
resultado = numeros[-3:]
print(resultado)  # [40, 50, 60]

# Invertir una cadena
texto = "Python"
resultado = texto[::-1]
print(resultado)  # "nohtyP"

