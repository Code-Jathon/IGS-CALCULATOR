from    sympy   import symbols
from    sympy   import integrate
from    sympy   import *
import  matplotlib.pyplot as plt
import  numpy as np

dx = symbols('x') #Diferencial

i = input('Ingrese el limite inferior de la ecuacion: ') #Limites
s = input('Ingrese el limite superior de la ecuacion: ')

fx = input("Ingrese la ecuacion: ")
fx = sympify(fx)
pprint(fx)

def valor(): #Menu
    print("-----------¿Desea conocer el resultado en fraccionarios o decimales -----------")
    print("1. Fraccionarios")
    print("2. Decimales")
    print("-----------------------------------")     
valor()

resp = input("INGRESE LA OPCION DE SU PREFERENCIA: ") #Mostrar resultado
if(resp == '1'):
    inte = integrate(fx, (dx, i, s)) #Fraccionario
elif(resp == '2'):
    inte = integrate(fx, (dx, i, s)).evalf(4) #Decimal
else:
    print("Opcion no valida")

print("El resultado de la integral es: ")
plot(integrate (fx)) #Grafica
pprint(inte)