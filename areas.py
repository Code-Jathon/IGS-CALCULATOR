from sympy import *
import sympy
from sympy.plotting import plot
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
sympy.init_printing()

x,y, z = symbols('x, y, z')  
print("Primera función")
expre1 = input("Expresion en terminos de x: ")
print("segunda función")         
expre2 = input("Expresion en terminos de x: ")

lim1 = int(input("Limite inferior: "))
lim2 = int(input("limite superior: "))


expre1=sympify(expre1)
expre2=sympify(expre2)  

aux = (expre1) - (expre2)   

print("EL AREA DE LA FUNCION= ", integrate(aux ,(x, lim1, lim2)), "U^2")

h1=int(lim1-2)
h2=int(lim2+2)

p=plot(expre1,expre2, (x, h1, h2), show=false)
p[1].line_color = 'r'
p.show()