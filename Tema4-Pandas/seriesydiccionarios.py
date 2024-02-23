import pandas as pd

# Crear una Serie de pandas desde una lista
datos = [10, 20, 30, 40, 50]
serie_lista = pd.Series(datos, name="EjemploLista")

# Crear una Serie de pandas desde un diccionario
diccionario = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
serie_diccionario = pd.Series(diccionario, name="EjemploDiccionario")

# Mostrar las Series
print("Serie creada desde lista:")
print(serie_lista)

print("\nSerie creada desde diccionario:")
print(serie_diccionario)