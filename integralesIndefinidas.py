from matplotlib.pyplot import legend
from sympy import symbols
from sympy import integrate
from sympy import *

dx = symbols('x') #Diferencial

fx = input("Ingrese la ecuacion: ") #Lee la funcion
fx = sympify(fx)
pprint(fx)

print("El resultado de la integral es: ")
pprint(integrate(fx, dx)) #Intrega la funcion

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