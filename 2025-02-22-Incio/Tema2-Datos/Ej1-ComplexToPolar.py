import math as mt
import cmath as cm

# 1)   Expresar en forma polar los siguientes complejos:
# z1 = 1 + raiz(3)i
# z2 = -2 + 2raiz(3)i
# z3 = -5 -5raiz(3)i
# z4 = 1 -i

# Resuelto por Enrique S Vázquez

raiz_3 = mt.sqrt(3)
a = 1
b = 1 * raiz_3
z = complex(a,b)
r, the_rad = cm.polar(z)
the_grad = (the_rad * (180/mt.pi))
print(f'Primer Ejemplo\n Z1 = {z} --> Polar[{r}, RAD {the_rad}  o GRA {the_grad}]')

a = -2
b = 2 * raiz_3
z = complex(a,b)
r, the_rad = cm.polar(z)
the_grad = (the_rad * (180/mt.pi))
print(f'Segundo Ejemplo\n Z2 = {z} --> Polar[{r}, RAD {the_rad}  o GRA {the_grad}]')

a = 1
b = -1
z = complex(a,b)
r, the_rad = cm.polar(z)
the_grad =(the_rad * (180/mt.pi))
print(f'Tercer Ejemplo\n Z3 = {z} --> Polar[{r}, RAD {the_rad}  o GRA {the_grad}]')

a = -5
b = -5 * raiz_3
z = complex(a,b)
r, the_rad = cm.polar(z)
the_grad = (the_rad * (180/mt.pi))
print(f'Cuarto Ejemplo\n Z4 = {z} --> Polar[{r}, RAD {the_rad}  o GRA {the_grad}]')
