contador = 0  # Variable global

def incrementar():
    global contador  # 🔹 Indica que vamos a modificar la variable global
    contador += 1
    print(contador)

incrementar()  # 1
incrementar()  # 2