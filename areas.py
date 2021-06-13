from sympy import *
import sympy
from sympy import symbols
from sympy import integrate
from sympy.plotting import plot
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
sympy.init_printing()

def puntos_corte(expre_1,expre_2,): 
    expre_1 = sympify(expre_1)
    expre_2 = sympify(expre_2)
    aux_puntos = (expre_1)-(expre_2)      
    solucion = solve(aux_puntos, dict=False)  
    return solucion

x,y, z = symbols('x, y, z')  
print("Primera función")
expre1 = input("Expresion en terminos de x: ")
print("¿Desea ingresar otra funcion?")
print("1. Si")
print("2. No")
resp = input("Ingrese su eleccion: ")
if(resp == '1'):
    print("segunda función")         
    expre2 = input("Expresion en terminos de x: ")
else:
    expre2 ='0'

expre1=sympify(expre1)
expre2=sympify(expre2)  

p_corte = puntos_corte(expre1, expre2)
p_corte = sympify(p_corte)
pprint(p_corte)
print("Los puntos de corte entre ",expre1," y ", expre2,"es: ",p_corte)

lim1 = input("Limite inferior: ")
lim2 = input("limite superior: ")

lim1=sympify(lim1)
lim2=sympify(lim2)

aux = (expre1) - (expre2)   

print("EL AREA DE LA FUNCION= ", integrate(aux ,(x, lim1, lim2)), "U^2")

h1=int(lim1-10)
h2=int(lim2+10)

p=plot(expre1,expre2, (x, h1, h2), legend = true, show=false)
p[0].line_color = 'b'
p[1].line_color = 'r'
p.show()

'''
def grafica(expre1,expre2,lim1,lim2):
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    plt.plot(x,expre1,x,expre2)  
    plt.fill_between(x, expre1,expre2, where = [(x > lim1) and (x < lim2) for x in x], color = 'red', alpha = 0.5)      
    plt.grid(True)         
    plt.show()

#grafica(expre1,expre2, lim1, lim2)
'''