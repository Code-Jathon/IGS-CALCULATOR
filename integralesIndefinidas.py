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

print("----------- ¿Desea conocer la grafica? -----------")#Menu
print("1. Si")
print("2. Si, mostrando la funcion de la integral")
print("3. No")
print("-----------------------------------")    

resp = input("Ingrese su eleccion: ") #Mostrar las grafica(s)
if(resp == '1'):
    s = plot(fx, legend = True, show = False)
    s[0].line_color = 'orange'
    s.show()   
elif(resp == '2'):
    s = plot(fx, integrate(fx), legend = True, show = False)
    s[0].line_color = 'orange'
    s[1].line_color = 'b'
    s.show()
else:
    print("Termino ejecucion")