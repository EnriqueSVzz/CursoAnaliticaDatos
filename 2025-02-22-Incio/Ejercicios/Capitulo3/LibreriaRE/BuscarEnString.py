import re

texto = "Mi número es 123-456-7890"
patron = r"\d{3}-\d{3}-\d{4}"  # Busca un número en formato XXX-XXX-XXXX

resultado = re.search(patron, texto)
print(resultado.group())  # 123-456-7890


'''
Buscar en correos electronicos
'''
texto = "Correos: usuario1@mail.com, usuario2@gmail.com"
patron = r"\w+@\w+\.\w+"  # Busca emails

emails = re.findall(patron, texto)
print(emails)  # ['usuario1@mail.com', 'usuario2@gmail.com']

'''
Sustituir una palabra por otra en un string.
'''
texto = "Hola Juan, hola Pedro"
nuevo_texto = re.sub(r"hola", "Hi", texto, flags=re.IGNORECASE)
print(nuevo_texto)  # Hi Juan, Hi Pedro

'''
Separar un string por medio de algún caracter
'''
texto = "apple,banana;orange grape"
palabras = re.split(r"[,; ]+", texto)
print(palabras)  # ['apple', 'banana', 'orange', 'grape']