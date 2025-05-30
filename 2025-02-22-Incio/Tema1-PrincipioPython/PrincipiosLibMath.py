import math

# Ejemplo de funciones de la librería math

# Operaciones algebraicas
num1 = 16
num2 = 4
print(f"Suma de {num1} y {num2}: {num1 + num2}")

# Raíz cuadrada
print(f"Raíz cuadrada de {num1}: {math.sqrt(num1)}")

# Seno y coseno
angle_rad = math.radians(45)  # Convertir grados a radianes
print(f"Seno de 45 grados: {math.sin(angle_rad)}")
print(f"Coseno de 45 grados: {math.cos(angle_rad)}")

# Valor absoluto
num3 = -10
print(f"Valor absoluto de {num3}: {math.fabs(num3)}")

# Potencia
base = 2
exponente = 3
print(f"{base} elevado a la {exponente}: {math.pow(base, exponente)}")

# Pi y Euler
print(f"Número Pi: {math.pi}")
print(f"Número de Euler (e): {math.e}")
