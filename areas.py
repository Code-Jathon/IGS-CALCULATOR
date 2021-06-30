from numpy.lib import math
from sympy import *
import sympy
from numpy import *
import matplotlib.pyplot as plt
from sympy.core import expr
from sympy.simplify.fu import L
sympy.init_printing()


def puntos_corte(expre_1,expre_2,): 
    x, y, z = symbols('x, y, z')
    expre_1 = sympify(expre_1)
    expre_2 = sympify(expre_2)
    aux_puntos = (expre_1)-(expre_2)      
    solucion = solve(aux_puntos, dict=False)  
    return solucion

def evaluar(exp1, exp2, l1):
    x, y, z = symbols('x, y, z')
    evaluar = l1 + 0.2
    eval_expre1 = exp1.evalf(subs={x: evaluar}) #evalua en la primera funcion 
    eval_expre2 = exp2.evalf(subs={x: evaluar}) # evalua en la segunda funcion

    if eval_expre1 < eval_expre2:  #identifica la funcion mayor y la menor
        aux1=exp1     
        exp1=exp2          
        exp2=aux1

    return(exp1, exp2)     

def area(expre1, expre2, lim1, lim2):
    x, y, z = symbols('x, y, z')
    lim1=sympify(lim1)
    lim2=sympify(lim2)
    expre1=sympify(expre1)
    expre2=sympify(expre2) 

    #ordena las funciones en mayor y menor
    lista=evaluar(expre1, expre2, lim1)

    expre1 = lista[0]
    expre2 = lista[1]

    aux = (expre1) - (expre2)   
    areaf = integrate(aux ,(x, lim1, lim2))
    return expre1, expre2, areaf

def graficar(expre1, expre2, lim1, lim2):
    x, y, z = symbols('x, y, z')
    lim1=sympify(lim1)
    lim2=sympify(lim2)
    expre1=sympify(expre1)
    expre2=sympify(expre2) 
    h1=(lim1-10)
    h2=(lim2+10)

    p=plot(expre1,expre2, (x, h1, h2), legend = true, show=false)
    p[0].line_color = 'b'
    p[1].line_color = 'r'
    p.show()    