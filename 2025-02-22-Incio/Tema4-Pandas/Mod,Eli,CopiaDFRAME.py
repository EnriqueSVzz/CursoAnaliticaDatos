import pandas as pd

# Crear un DataFrame desde un diccionario
data = {'Nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
        'Edad': [28, 35, 22, 45, 29],
        'Departamento': ['Ventas', 'TI', 'Recursos Humanos', 'Ventas', 'TI'],
        'Salario': [50000, 80000, 45000, 70000, 75000]}

df = pd.DataFrame(data)

# Mostrar el DataFrame original
print("DataFrame original:")
print(df)

# Modificar datos en el DataFrame
df.loc[df['Nombre'] == 'Bob', 'Salario'] = 85000
print("\nDataFrame después de modificar el salario de Bob:")
print(df)

# Eliminar una fila basada en una condición
df = df[df['Nombre'] != 'David']
print("\nDataFrame después de eliminar a David:")
print(df)

# Eliminar una columna
df = df.drop('Edad', axis=1)
print("\nDataFrame después de eliminar la columna 'Edad':")
print(df)

# Crear una copia del DataFrame
df_copia = df.copy()

# Ordenar el DataFrame por salario de forma descendente
df_copia = df_copia.sort_values(by='Salario', ascending=False)
print("\nDataFrame copiado y ordenado por salario:")
print(df_copia)