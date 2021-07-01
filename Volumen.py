import matplotlib.pyplot as plt 
import numpy as np
from sympy import *
from sympy import Integral, integrate
from sympy.core import symbol
from sympy.core.numbers import Exp1
from sympy.plotting import plot
from sympy import Symbol
from sympy.plotting import plot
from sympy.testing.runtests import SymPyOutputChecker
from sympy.core import expr
from sympy.simplify.fu import L

def evaluar(exp1, exp2,l1):
    x, y, z =symbols('x, y, z')
    evaluar = l1 + 0.2
    eval_expre1 = exp1.evalf(subs={x: evaluar}) #evalua en la primera funcion 
    eval_expre2 = exp2.evalf(subs={x: evaluar}) # evalua en la segunda funcion

    if eval_expre1 < eval_expre2:  #identifica la funcion mayor y la menor
        aux1=exp1     
        exp1=exp2          
        exp2=aux1

    return(exp1, exp2)      

def volumenTotal(expresion1, expresion2, limite1, limite2):
    x, y, z =symbols('x, y, z')
    x=sympify('x')
    y=simplify('y')
    z=simplify('z')
    limite1=sympify(limite1)
    limite2=sympify(limite2)
    expresion1=sympify(expresion1)
    expresion2=sympify(expresion2)

#EVALUA LAS FUNCIONES PARA MAYOR Y MENOR.
    lista=evaluar(expresion1, expresion2, limite1)
    expresion1 = lista[0]
    expresion2 = lista[1]
    d1 = np.pi * Integral(expresion1**2,(x,limite1,limite2)).doit()
    d2 = np.pi * Integral(expresion2**2,(x,limite1,limite2)).doit()
    volumenR =(d1-d2)
    volumenR=sympify(volumenR)
    return expresion1, expresion2,volumenR
#FUNCION PARA GRAFICAR
def Graficar(expresion1, expresion2, limiteInf1, limiteSup2):   
    limiteInf1=sympify(limiteInf1)
    limiteSup2=sympify(limiteSup2)
    expresion1=sympify(expresion1)
    expresion2=sympify(expresion2)
    p = plot(expresion1, expresion2, legend=True, show=False)
    p[0].line_color = 'b'
    p[1].line_color = 'r'
    p.show()