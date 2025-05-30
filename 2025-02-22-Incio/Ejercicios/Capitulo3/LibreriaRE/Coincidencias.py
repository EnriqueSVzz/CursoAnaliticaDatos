texto = "Correos: usuario1@mail.com, usuario2@gmail.com"
patron = r"\w+@\w+\.\w+"  # Busca emails

emails = re.findall(patron, texto)
print(emails)  # ['usuario1@mail.com', 'usuario2@gmail.com']