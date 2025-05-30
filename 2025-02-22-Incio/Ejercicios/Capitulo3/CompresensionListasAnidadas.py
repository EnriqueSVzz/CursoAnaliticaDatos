'''
 Supongamos que tenemos una lista de listas que contiene algunos
 nombres en inglés y español, y queremos mostrar los elementos que tengan 2 o más 'a' 
 ¿cómo se haría esto usando comprensión de lista anidada?
'''

# Lista de listas con nombres en inglés y español
nombres = [["Carlos", "Sarah", "Daniel"], 
           ["Ana", "Santiago", "Laura"], 
           ["Martin", "Alexandra", "Barbara"]]

# Filtrar nombres con dos o más 'a'
resultado = [[nombre for nombre in sublista if nombre.lower().count('a') >= 2] for sublista in nombres]

# Imprimir resultado
print(resultado)
