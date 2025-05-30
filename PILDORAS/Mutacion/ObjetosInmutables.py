texto = "Hola"
# Esto dará error porque las cadenas son inmutables
# texto[0] = 'h'  # TypeError
# Pero puedes crear una nueva cadena
texto = "hola"
print(texto)  # "hola"

tupla = (1, 2, 3)
# No puedes modificar un valor existente
# tupla[1] = 20  # TypeError
# Pero puedes crear una nueva tupla
nueva_tupla = tupla + (4,)
print(nueva_tupla)  # (1, 2, 3, 4)

x = 10
x = x + 5  # Se crea un nuevo objeto, no se modifica el original
print(x)  # 15