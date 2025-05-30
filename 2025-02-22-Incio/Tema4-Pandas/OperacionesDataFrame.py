import pandas as pd

# Crear un DataFrame desde un diccionario
data = {'Nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
        'Edad': [28, 35, 22, 45, 29],
        'Departamento': ['Ventas', 'TI', 'Recursos Humanos', 'Ventas', 'TI'],
        'Salario': [50000, 80000, 45000, 70000, 75000]}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print("DataFrame original:")
print(df)

# Operaciones comunes:

# Filtrar empleados mayores de 30 años
mayores_30 = df[df['Edad'] > 30]
print("\nEmpleados mayores de 30 años:")
print(mayores_30)

# Calcular el salario promedio
salario_promedio = df['Salario'].mean()
print("\nSalario promedio:", salario_promedio)

# Agrupar por departamento y calcular la suma de salarios por departamento
salarios_por_departamento = df.groupby('Departamento')['Salario'].sum()
print("\nSuma de salarios por departamento:")
print(salarios_por_departamento)

# Añadir una nueva columna calculada (Salario después de un aumento del 10%)
df['Salario_con_aumento'] = df['Salario'] * 1.1
print("\nDataFrame con columna de salario después de aumento:")
print(df)