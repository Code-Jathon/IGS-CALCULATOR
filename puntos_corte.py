from matplotlib.pyplot import legend
from sympy import Symbol
from sympy import integrate
from sympy import *

def puntos_corte(expre_1,expre_2,):
    expre_1 = sympify(expre_1)
    expre_2 = sympify(expre_2)
    aux_puntos = (expre_1)-(expre_2)      
    solucion = solve(aux_puntos, dict=False)  
    return solucion

fx1 = input("Ingrese la primera funcion en terminos de x: ") #Lee la primera función
fx1 = sympify(fx1)
pprint(fx1)

fx2 = input("Ingrese la segunda funcion en terminos de x: ") #Lee la segunda función
fx2 = sympify(fx2)
pprint(fx2)

p_corte = puntos_corte(fx1, fx2)
p_corte = sympify(p_corte)
pprint(p_corte)
print("Los puntos de corte entre ",fx1," y ", fx2,"es: ",p_corte)