from numpy.lib import math
from sympy import *
import sympy
from sympy import symbols
from sympy import integrate
from sympy.core import expr
from sympy.plotting import plot
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from sympy.simplify.fu import L
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

p_corte = puntos_corte(expre1, expre2)
#p_corte = sympify(p_corte)

print("Los puntos de corte entre ",expre1," y ", expre2,"es: ",p_corte)

lim1 = int(input("Limite inferior: "))
lim2 = int(input("limite superior: "))

#ordena las funciones en mayor y menor
mayor1=0
mayor2=0
for i in range((lim1),(lim2+1)): 
    j=lim1
    j=j+0.2
    libres={"x":j}             
    if((eval(expre1, {}, libres))>(eval(expre2, {}, libres))): 
      mayor1=mayor1+1
    else: 
      mayor2=mayor2+1

if mayor2>mayor1:  
   aux1=expre1     
   expre1=expre2          
   expre2=aux1             
print("La funcion mayor es: ")
print(expre1)
print("La funcion menor es: ")
print(expre2)

lim1=sympify(lim1)
lim2=sympify(lim2)
expre1=sympify(expre1)
expre2=sympify(expre2)  

aux = (expre1) - (expre2)   

print("EL AREA DE LA FUNCION= ", integrate(aux ,(x, lim1, lim2)), "U^2")

