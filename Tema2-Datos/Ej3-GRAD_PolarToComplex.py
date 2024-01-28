#transformar de Polar a la forma Binomial pero con grados

import math as mt
import cmath as cm

def polar_a_binomica(r, theta):
    # Coordenadas polares a forma binómica
    numero_binomico = cm.rect(r, cm.pi * theta / 180.0)
    return numero_binomico

#conversion
band = True
r =0
theta=0 
count=0

op = int(input(print("Ingrese la cantidad de ejercicios:")))

while band :
    r = float(input(print("Ingrese la parte r")))
    theta = float(input(print("Ingrese la parte Theta")))
    numero_binomico_resultante = polar_a_binomica(r, theta)
    print(f"Coordenadas polares ({r}, {theta}°) a forma binómica: {numero_binomico_resultante}")
    count +=1
    if op < count :
        band = False