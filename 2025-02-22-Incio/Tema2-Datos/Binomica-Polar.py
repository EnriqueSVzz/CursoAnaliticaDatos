import cmath
import math  # Necesario para convertir radianes a grados

# Número complejo en forma binómica
z_binomico = 3 + 4j

# Obtener coordenadas polares
r, theta_radianes = cmath.polar(z_binomico)

# Convertir theta de radianes a grados
theta_grados = math.degrees(theta_radianes)

# Obtener el número complejo en coordenadas polares
z_polar = cmath.rect(abs(z_binomico), theta_radianes)

# Mostrar resultados
print(f"Número complejo en forma binómica: {z_binomico}")
print(f"Coordenadas polares: r = {r}, Radines= {theta_radianes}, θ = {theta_grados}°")
print(f"Número complejo en coordenadas polares: {z_polar}")