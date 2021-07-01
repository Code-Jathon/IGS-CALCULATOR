from    sympy   import symbols
from    sympy   import integrate
from    sympy   import *
import  matplotlib.pyplot as plt
from    matplotlib.pyplot import legend
import  numpy as np
from    tkinter import messagebox

def ecuacionD(i, s, fx, resp):

    if(i == ""):
        messagebox.showerror("Error", "Ingrese el limite inferior por favor")
    elif(s == ""):
        messagebox.showerror("Error", "Ingrese el limite superior por favor")
    elif(fx == ""):
        messagebox.showerror("Error", "Ingrese una integral por favor")
       

    dx = symbols('x') #Diferencial
    fx = sympify(fx)
    
    print("limite inferior: " + i)
    print("limite superior: " + s)
    pprint(fx)

    if(resp == "Fraccionario."):
        inte = integrate(fx, (dx, i, s)) #Fraccionario
        print("El resultado de la integral es: ")
        pprint(inte)
    elif(resp == "Decimales."):
        inte = integrate(fx, (dx, i, s)).evalf(3) #Decimal
        print("El resultado de la integral es: ")
        pprint(inte)
    else:
        messagebox.showerror("Error", "Seleccione una opcion por favor")

    return inte

def graficaES(fx):

    fx = sympify(fx)
    s = plot(fx, legend = True, show = False)#Grafica
    s[0].line_color = 'orange'
    s.show()