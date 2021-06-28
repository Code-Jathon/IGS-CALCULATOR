from    sympy   import symbols
from    sympy   import integrate
from    sympy   import *
import  matplotlib.pyplot as plt
from    matplotlib.pyplot import legend
import  numpy as np

dx = symbols('x') #Diferencial

i = input('Ingrese el limite inferior de la ecuacion: ') #Limites
s = input('Ingrese el limite superior de la ecuacion: ')

fx = input("Ingrese la ecuacion: ")
fx = sympify(fx)
pprint(fx)

print("-----------¿Desea conocer el resultado en fraccionarios o decimales -----------")#Menu
print("1. Fraccionarios")
print("2. Decimales")
print("-----------------------------------")     

resp = input("INGRESE LA OPCION DE SU PREFERENCIA: ") #Mostrar resultado
if(resp == '1'):
    inte = integrate(fx, (dx, i, s)) #Fraccionario
elif(resp == '2'):
    inte = integrate(fx, (dx, i, s)).evalf(4) #Decimal
else:
    print("Opcion no valida")
print("El resultado de la integral es: ")
pprint(inte)

s = plot(fx, legend = True, show = False)#Grafica
s[0].line_color = 'orange'
s.show()