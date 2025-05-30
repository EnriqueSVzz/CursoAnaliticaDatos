'''
Un array de números pares del 2 al 20 usando np.arange()
'''

import numpy as np 

# Calculamos toda lista
lista = np.arange(1, 21)
#todos los valores que no sean par, los guardamos.
for a in lista:
    if a % 2 != 0:
        lista = np.delete(lista, np.where(lista == a))
print(f'Array De los pares del [2,20]: {lista}')

#Forma 2.
# especificamos que tome de 2 en 2.
array_pares = np.arange(2, 21, 2)
print(array_pares)