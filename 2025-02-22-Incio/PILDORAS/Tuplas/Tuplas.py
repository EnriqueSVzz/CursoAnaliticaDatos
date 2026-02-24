# Tupla con diferentes tipos de datos
mi_tupla = (1, "Hola", 3.14, True)
print(mi_tupla)  # (1, 'Hola', 3.14, True)

# Otra forma de instanciar una tupla
mi_tupla_2 = 1, 2, 3, 4
print(mi_tupla_2)  # (1, 2, 3, 4)

# Aquí con tuple, pero usando una lista como argumento
mi_tupla_3 = tuple([10, 20, 30])
print(mi_tupla_3)  # (10, 20, 30)

# Tupla de un solo elemento, es necesario poner la coma
tupla_un_elemento = (5,)
print(type(tupla_un_elemento))  # <class 'tuple'>

# slicing con tuplas
mi_tupla_4 = (1, 2, 3, 4, 5, 6)

# Extraer los primeros tres elementos
print(mi_tupla_4[:3])  # (1, 2, 3)

# Invertir una tupla
print(mi_tupla_4[::-1])  # (6, 5, 4, 3, 2, 1)

# Concatenar las tuplas si es posible
mi_tupla_5 = (1, 2, 3)
nueva_tupla = mi_tupla_5 + (4, 5)
print(nueva_tupla)  # (1, 2, 3, 4,5) 