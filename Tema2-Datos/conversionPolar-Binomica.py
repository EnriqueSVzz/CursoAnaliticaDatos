import cmath

def polar_a_binomica(r, theta):
    # Coordenadas polares a forma binómica
    numero_binomico = cmath.rect(r, cmath.pi * theta / 180.0)
    return numero_binomico

def binomica_a_polar(numero_binomico):
    # Forma binómica a coordenadas polares
    r, theta_radianes = cmath.polar(numero_binomico)
    theta_grados = (theta_radianes * 180.0) / cmath.pi
    return r, theta_grados

# Ejemplo de coordenadas polares a forma binómica
r = 5
theta = 30
numero_binomico_resultante = polar_a_binomica(r, theta)
print(f"Coordenadas polares ({r}, {theta}°) a forma binómica: {numero_binomico_resultante}")

# Ejemplo de forma binómica a coordenadas polares
numero_binomico = 3 + 4j
r_resultante, theta_resultante = binomica_a_polar(numero_binomico)
print(f"Forma binómica {numero_binomico} a coordenadas polares: ({r_resultante}, {theta_resultante}°)")