def externa():
    x = 10  # Variable en ámbito intermedio

    def interna():
        nonlocal x  # 🔹 Permite modificar 'x' de la función externa
        x += 5
        print(f"Dentro de interna: {x}")

    interna()
    print(f"Dentro de externa: {x}")

externa()