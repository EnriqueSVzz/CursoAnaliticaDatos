import keyword

keywords = keyword.kwlist
print("Palabras clave en Python:", keywords)

word = "if"
if keyword.iskeyword(word):
    print(f"{word} es una palabra clave en Python.")
else:
    print(f"{word} no es una palabra clave en Python.")
