import cmath

def mostrar_argumento_en_grados(numero_complejo):
    argumento_radianes = cmath.phase(numero_complejo)
    argumento_grados = cmath.phase(numero_complejo) * (180 / cmath.pi)

    print(f"Número complejo: {numero_complejo}")
    print(f"Argumento en radianes: {argumento_radianes}")
    print(f"Argumento en grados: {argumento_grados}°\n")

# Ejemplos
numero_complejo_1 = 3 + 4j
numero_complejo_2 = -2 - 5j

mostrar_argumento_en_grados(numero_complejo_1)
mostrar_argumento_en_grados(numero_complejo_2)