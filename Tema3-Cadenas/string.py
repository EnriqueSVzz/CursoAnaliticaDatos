# Crear dos cadenas de texto
cadena1 = "Hola"
cadena2 = "Mundo"

# Concatenación de cadenas
concatenacion = cadena1 + " " + cadena2
print("Concatenación:", concatenacion)

# Longitud de la cadena
longitud = len(concatenacion)
print("Longitud de la cadena:", longitud)

# Mayúsculas y minúsculas
mayusculas = concatenacion.upper()
minusculas = concatenacion.lower()
print("Mayúsculas:", mayusculas)
print("Minúsculas:", minusculas)

# Reemplazar parte de la cadena
reemplazo = concatenacion.replace("Mundo", "Gente")
print("Reemplazo:", reemplazo)

# Dividir la cadena en una lista de palabras
palabras = concatenacion.split()
print("Palabras:", palabras)

# Verificar si la cadena comienza o termina con ciertos caracteres
comienza_con_hola = concatenacion.startswith("Hola")
termina_con_mundo = concatenacion.endswith("Mundo")
print("¿Comienza con 'Hola'?", comienza_con_hola)
print("¿Termina con 'Mundo'?", termina_con_mundo)