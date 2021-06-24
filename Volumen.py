import matplotlib.pyplot as plt 
import numpy as np
from sympy import *
from sympy import Integral, integrate
from sympy.core import symbol
from sympy.core.numbers import Exp1
from sympy.plotting import plot
from sympy import Symbol
from sympy.plotting import plot

def evaluar(exp1, exp2,l1):

    evaluar = l1 + 0.2
    eval_expre1 = exp1.evalf(subs={x: evaluar}) #evalua en la primera funcion 
    eval_expre2 = exp2.evalf(subs={x: evaluar}) # evalua en la segunda funcion

    if eval_expre1 < eval_expre2:  #identifica la funcion mayor y la menor
        aux1=exp1     
        exp1=exp2          
        exp2=aux1

    return(exp1, exp2)     


x, y, z =symbols('x, y, z')


expre1=input('Ingrese su función en términos de x: ')
expre1=sympify(expre1)
pprint(expre1)

print("Agregar nueva función")
print("1 Si; 2 No")
opc=input("Elección: ")


if opc=='1': 
    expre2=input('Ingrese su función en terminos de x: ')
    expre2=sympify(expre2)
    pprint(expre2)
else:
    expre2='0'

l1 = int(input('Ingrese el valor del limite inferior: '))    
l2 = int(input('Ingrese el valor del limite superior: '))

expre1=sympify(expre1)
expre2=sympify(expre2)


lista=evaluar(expre1, expre2, l1)

expre1 = lista[0]
expre2 = lista[1]

print("Expresión mayor: ")
expre1=sympify(expre1)
print(expre1)


print("Expresión menor: ")
expre2=sympify(expre2)
print(expre2)

d1 = np.pi * Integral(expre1**2,(x,l1,l2)).doit()
d2 = np.pi * Integral(expre2**2,(x,l1,l2)).doit()
print("El valor del volumen entre {} y {} es : {}".format(l1, l2, d1-d2))

p = plot(expre1, expre2, legend=True, show=False)
p[0].line_color = 'b'
p[1].line_color = 'r'
p.show()