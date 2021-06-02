from matplotlib.pyplot import legend
from sympy import Symbol
from sympy import integrate
from sympy import *

dx = Symbol('x')
fx = input("Ingrese la ecuacion: ") #Lee la funcion
fx = sympify(fx)
pprint(fx)

print("El resultado de la integral es: ")
print(integrate(fx), dx) #Intrega la funcion

def grafica(): #Menu
    print("----------- ¿Desea conocer la grafica? -----------")
    print("1. Si")
    print("2. Si, mostrando la funcion ingresada")
    print("3. No")
    print("-----------------------------------")    
grafica()

resp = input("Ingrese su eleccion: ") #Mostrar las grafica(s)
if(resp == '1'): 
    plot(integrate(fx))    
elif(resp == '2'):
    s = plot(fx, integrate(fx), legend = True, show = False)
    s[0].line_color = 'b'
    s[1].line_color = 'r'
    s.show()
else:
    print("Termino ejecucion")