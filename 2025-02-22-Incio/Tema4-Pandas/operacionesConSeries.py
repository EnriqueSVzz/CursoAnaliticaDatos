import pandas as pd

# Crear la Serie
s = pd.Series([2, 4, 6, 8], index=["num1", "num2", "num3", "num4"])

# Mostrar la Serie
print("Serie:")
print(s)

# Operaciones comunes en pandas Series
print("\nOperaciones comunes:")

# Acceder a un valor por su etiqueta
print("Valor asociado a 'num2':", s['num2'])

# Slicing por etiquetas (ver un rango)
print("Slicing por etiquetas ('num2' a 'num4'):")
print(s['num2':'num4'])

# Filtrar valores mayores que 5
print("Valores mayores que 5:")
print(s[s > 5])

# Multiplicar todos los elementos por 2
print("Multiplicar todos los elementos por 2:")
print(s * 2)

# Calcular la media de los elementos
print("Media de los elementos:", s.mean())
