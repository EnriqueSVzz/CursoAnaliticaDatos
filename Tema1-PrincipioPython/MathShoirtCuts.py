import math as mt
from math import pi as PI
from math import e as E
from math import log

# Uso de Pi
radio_circulo = 0
radio_circulo = int(input("Por favor Ingresa el radio del circulo:"))
area_circulo = PI * radio_circulo**2
print(f"El Área de un círculo con radio {radio_circulo}: {area_circulo}")

# Uso del número de Euler (e)
base_logaritmo_natural = E
resultado_logaritmo = mt.log(10, base_logaritmo_natural)
print(f"Logaritmo natural de 10 en (base e): {resultado_logaritmo}")

# Otro ejemplo de logaritmo
valor = 0
base_log = 0
valor =  int(input("Por favor ingrese el valor:"))
base_log = int(input("Por favor Ingresa la base del logaritmo"))
resultado_logaritmo_otra_base = mt.log(base_log, valor)
print(f"Logaritmo de 100 en base 10: {resultado_logaritmo_otra_base}")

# Ingresar los valores de base y exponente desde el teclado
base = float(input("Ingresa la base para la función exponencial: "))
exponente = float(input("Ingresa el exponente para la función exponencial: "))

# Calcular la función exponencial e -> e^(base^exponente)
resultado = mt.exp(base ** exponente)

# Mostrar el resultado
print(f"\nEl resultado de la función exponencial con base {base} y exponente {exponente} es: {resultado}")