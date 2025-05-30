# ✅ Crear una lista
mi_lista = [10, 20, 30, 40, 50]
print("Lista inicial:", mi_lista)

# ✅ Acceso a elementos (por índice)
print("Primer elemento:", mi_lista[0])      # 10
print("Último elemento:", mi_lista[-1])     # 50

# ✅ Modificar un valor
mi_lista[1] = 100
print("Lista después de modificar:", mi_lista)  # [10, 100, 30, 40, 50]

# ✅ Slicing (extraer subconjunto)
print("Subconjunto (índices 1 a 3):", mi_lista[1:4])  # [100, 30, 40]

# ✅ Añadir elementos a la lista
mi_lista.append(60)          # Añade al final
mi_lista.insert(2, 25)       # Inserta en la posición 2
print("Lista después de añadir elementos:", mi_lista)  

# ✅ Eliminar elementos de la lista
mi_lista.remove(25)          # Elimina el valor 25
valor = mi_lista.pop()       # Elimina y devuelve el último elemento
print("Elemento eliminado con pop():", valor)
print("Lista después de eliminar elementos:", mi_lista)

# ✅ Ordenar la lista
mi_lista.sort()
print("Lista ordenada:", mi_lista)

# ✅ Invertir la lista
mi_lista.reverse()
print("Lista invertida:", mi_lista)

# ✅ Concatenar listas
otra_lista = [70, 80, 90]
nueva_lista = mi_lista + otra_lista
print("Lista concatenada:", nueva_lista)

# ✅ Comprobar si un valor está en la lista
existe = 100 in nueva_lista
print("¿100 está en la lista?:", existe)   # True

# ✅ Longitud de la lista
print("Tamaño de la lista:", len(nueva_lista))

# ✅ Contar cuántas veces aparece un valor
print("Cantidad de veces que aparece 40:", nueva_lista.count(40))

# ✅ Índice de un valor
print("Índice de 40:", nueva_lista.index(40))

# ✅ Vaciar la lista
nueva_lista.clear()
print("Lista vacía:", nueva_lista)
