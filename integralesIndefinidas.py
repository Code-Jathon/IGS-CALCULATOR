from matplotlib.pyplot import legend
from sympy import symbols
from sympy import integrate
from sympy import *
from tkinter import messagebox

def ecuacionI(fx): #Lee la funcion

    dx = symbols('x') #Diferencial
    fx = sympify(fx)
    pprint(fx)

    integral = integrate(fx, dx) #Integra la funcion y lo toma
    print("El resultado de la integral es: ")
    pprint(integral)

    return integral
    
def graficaIS(fx, sol ,resp): #Menu Despegable
    
    dx = symbols('x') #Diferencial
    fx = sympify(fx)
    if(resp == "Si."):
        s = plot(fx, legend = True, show = False)
        s[0].line_color = 'orange'
        s.show()

    elif(resp == "Si, mostrando la grafica de la integral."):
        s = plot(fx, sol, legend = True, show = False)
        s[0].line_color = 'orange'
        s[1].line_color = 'b'
        s.show()
    else:
        messagebox.showerror("Error", "Seleccione una opcion por favor")