import pandas as pd

#podemos crear primero un diccionario y luego hacer el data frame
data = {'Nombre': ['Alice', 'Bob', 'Charlie'],
        'Edad': [25, 30, 35],
        'Ciudad': ['Ciudad A', 'Ciudad B', 'Ciudad C']}

df = pd.DataFrame(data)

#También podemos ir cargando todo de uno por uno.
df = pd.DataFrame()
df['Nombre'] = ['Alice', 'Bob', 'Charlie']
df['Edad'] = [25, 30, 35]
df['Ciudad'] = ['Ciudad A', 'Ciudad B', 'Ciudad C']