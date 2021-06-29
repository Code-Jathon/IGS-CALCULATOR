from numpy.lib import math
from sympy import *
import sympy
from numpy import *
import matplotlib.pyplot as plt
from sympy.simplify.fu import L
sympy.init_printing()

def puntos_corte(expre_1,expre_2,): 
    expre_1 = sympify(expre_1)
    expre_2 = sympify(expre_2)
    aux_puntos = (expre_1)-(expre_2)      
    solucion = solve(aux_puntos, dict=False)  
    return solucion

def evaluar(exp1, exp2, l1):

    evaluar = l1 + 0.2
    eval_expre1 = exp1.evalf(subs={x: evaluar}) #evalua en la primera funcion 
    eval_expre2 = exp2.evalf(subs={x: evaluar}) # evalua en la segunda funcion

    if eval_expre1 < eval_expre2:  #identifica la funcion mayor y la menor
        aux1=exp1     
        exp1=exp2          
        exp2=aux1

    return(exp1, exp2)     

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

lim1 = (input("Limite inferior: "))
lim2 = (input("limite superior: "))

lim1=sympify(lim1)
lim2=sympify(lim2)
expre1=sympify(expre1)
expre2=sympify(expre2) 

#ordena las funciones en mayor y menor
lista=evaluar(expre1, expre2, lim1)

expre1 = lista[0]
expre2 = lista[1]

print("La funcion mayor es: ")
pprint(expre1)
print("La funcion menor es: ")
pprint(expre2)

aux = (expre1) - (expre2)   

print("EL AREA DE LA FUNCION= ", integrate(aux ,(x, lim1, lim2)), "U^2")

h1=(lim1-10)
h2=(lim2+10)

p=plot(expre1,expre2, (x, h1, h2), legend = true, show=false)
p[0].line_color = 'b'
p[1].line_color = 'r'
p.show()