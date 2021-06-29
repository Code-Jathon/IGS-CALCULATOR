from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter
import tkinter.font as tkFont
from tkinter import messagebox 
from numpy.lib import math
from sympy import *
import sympy
from numpy import *
import matplotlib.pyplot as plt
from sympy.simplify.fu import L
sympy.init_printing() 
x, y, z = symbols('x, y, z')

def main():
    ventana= Tk()
    ventana.config(bg="white",bd=0)
    ventana.title('IGS Calculator')
    label= tkinter.Label(ventana, text="IGS Calculator", bg="white", fg="#007b99", )
    label.configure(font=("Bahnschrift Light", 19,tkFont.BOLD))
    label.pack()
    style = ttk.Style()    
    settings = {"TNotebook.Tab": {"configure": {"padding": [120, 5],
                                            "background": "#f39200",
                                            "font":"Helvetica, 11 "
                                            }}}  
    style.theme_create("mi_estilo", parent="alt", settings=settings)
    style.theme_use("mi_estilo")
    notebook = ttk.Notebook(ventana)
    notebook.pack(fill='both', expand='yes',padx=7, pady=20)
    notebook.pressed_index = None
    pes0 = tkinter.Frame(notebook,background="white")
    pes1 = tkinter.Frame(notebook,background="white")
    pes2 = tkinter.Frame(notebook,background="white")
    pes3 = tkinter.Frame(notebook,background="white")
    notebook.add(pes0, text='Integrales')
    #Parte Area   
    notebook.add(pes1, text='Área')
    fun1=tk.Label(pes1,text="Ingrese la funcion en terminos de x: ", width="35", height="1", font=("Helvetica 14"), bg='white')
    fun1.grid(row=2, column=0)
    caj1 = Entry(pes1, width= 45, font = ("Helvetica 16"), highlightbackground='#007b99', highlightcolor='#f39200', highlightthickness=3)
    caj1.grid(row=2, column=1)
    #accion boton
    def sefu():
        fun2.grid(row=4, column=0)
        caj2.grid(row=4,column=1)
    bot2fun = tk.Button(pes1, text="Añadir segunda funcion", width = "20", height = "1", command=sefu 
    , font = ("Helvetica 14"),foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
    bot2fun.grid(row=3,column=0)
    fun2=tk.Label(pes1,text="Ingrese la funcion en terminos de x: ", width = "35", height = "1", font = ("Helvetica 14"), bg='white')
    caj2 = Entry(pes1, width= 45, font= ("Calibri 16"), highlightbackground='#007b99'
    , highlightcolor='#f39200', highlightthickness=3)
    #accion boton
    def puntos_corte(): 
        expre1=caj1.get()
        expre2=caj2.get()
        if not expre2:
            expre2 = 0
        expre1 = sympify(expre1)
        expre2 = sympify(expre2)
        aux_puntos = (expre1)-(expre2)      
        solucion = solve(aux_puntos, dict=False)  
        pcorte = tk.Label(pes1, text="Los puntos de corte son: " + str(solucion), width = "35", height = "1"
        , font = ("Helvetica 14"), bg='white')
        pcorte.grid(row=6,column=0)

    botpun = tk.Button(pes1, text="Calcular puntos de corte", width = "20", height = "1", command = puntos_corte
     , font = ("Helvetica 14") ,foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
    botpun.grid(row=5, column=0)
    liminfe = tk.Label(pes1, text="Ingrese limite inferior: ", width = "35", height = "1", font = ("Helvetica 14"), bg='white')
    liminfe.grid(row=7, column=0)
    caj3 = Entry(pes1,width= 45, font= ("Calibri 16"), highlightbackground='#007b99', highlightcolor='#f39200', highlightthickness=3)
    caj3.grid(row=7, column=1)
    limsupe = tk.Label(pes1, text="Ingrese limite superior: ", width = "35", height = "1", font = ("Helvetica 14"), bg='white')
    limsupe.grid(row=10, column=0)
    caj4 = Entry(pes1,width= 45, font= ("Calibri 16"), highlightbackground='#007b99', highlightcolor='#f39200', highlightthickness=3)
    caj4.grid(row=10, column=1)
    #accion boton
    #grafica
    def grafica(expre1, expre2, lim1, lim2):  #sin sombrear
        expre1=sympify(expre1)       
        expre2=sympify(expre2)  
        h1=(lim1-2)
        h2=(lim2+2)
        p=plot(expre1,expre2, (x, h1, h2), legend = true, show=false)
        p[0].line_color = 'b'
        p[1].line_color = 'r'
        p.show()  
    #evaluar funcion mayor
    def evaluar(expre1, expre2, l1):
        expre1 = sympify(expre1)
        expre2 = sympify(expre2)
        l1 = sympify(l1)
        evaluar = l1 + 0.2
        eval_expre1 = expre1.evalf(subs={x: evaluar}) #evalua en la primera funcion 
        eval_expre2 = expre2.evalf(subs={x: evaluar}) # evalua en la segunda funcion
        if eval_expre1 < eval_expre2:  #identifica la funcion mayor y la menor
            aux1=expre1     
            expre1=expre2          
            expre2=aux1
        return expre1, expre2
    #calcular area
    def area_funcion():
        expre1=caj1.get()
        expre2=caj2.get()
        lim1=caj3.get()
        lim2=caj4.get()
        if not expre2:
            expre2 = 0
        lim1=sympify(lim1)
        lim2=sympify(lim2)
        expre1=sympify(expre1)
        expre2=sympify(expre2)  
        lista=evaluar(expre1, expre2, lim1)
        expre1 = lista[0]
        expre2 = lista[1]
        aux = (expre1) - (expre2)   
        area = integrate(aux ,(x, lim1, lim2)), "U^2"
        funmay = tk.Label(pes1, text="La funcion mayor es: " + str(expre1), width = "35", height = "1", font = ("Helvetica 14"), bg='white')
        funmay.grid(row=16,column=0)
        funmen = tk.Label(pes1, text="La funcion menor es: " + str(expre2), width = "35", height = "1", font = ("Helvetica 14"), bg='white')
        funmen.grid(row=18,column=0)      
        resulta = tk.Label(pes1, text="El area de la funcion es: " + str(area), width = "35", height = "1", font = ("Helvetica 14"), bg='white')
        resulta.grid(row=20,column=0)
        grafica(expre1, expre2, lim1, lim2)

    botresult = tk.Button(pes1, text="Calcular", width = "20", height = "1", command = area_funcion, font = ("Helvetica 14")
    ,foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
    botresult.grid(row=14,column=0)  

    notebook.add(pes2, text='Volumen')
    notebook.add(pes3, text='About Us')
    ventana.geometry("1200x650")
    ventana.resizable(1,1)
    ventana.mainloop()

if __name__=='__main__':
    main()