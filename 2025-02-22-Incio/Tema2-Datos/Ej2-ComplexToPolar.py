import math as mt
import cmath as cm

#convertir de complejo a polar
band = True
a =0
b=0 
r = 0 
the_rad=0 
the_grad = 0 
count = 0 
z = complex(0,0) 

op = int(input(print("Ingrese la cantidad de ejercicios:")))

while band :
    a = float(input(print("Ingrese la parte Real")))
    b = float(input(print("Ingrese la parte Imaginaria")))
    z = complex(a,b)
    r, the_rad = cm.polar(z)
    the_grad = mt.degrees(the_rad)
    print(f'\n Z{count+1} = {z} --> Polar[{r}, RAD {the_rad}  o GRA {the_grad}]')
    count +=1
    if op < count :
        band = False
