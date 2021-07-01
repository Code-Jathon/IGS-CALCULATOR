from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter
import tkinter.font as tkFont
from tkinter import messagebox
from integralesIndefinidas import *
from integralesDefinidas import *
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter
from tkinter import font
import tkinter.font as tkFont
import matplotlib.pyplot as plt 
import numpy as np
from sympy import *
from sympy import Integral, integrate
from sympy.core import symbol
from sympy.core.numbers import Exp1
from sympy.plotting import plot
from sympy import Symbol
from sympy.plotting import plot
from Volumen import *
from tkinter import messagebox

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

    #--------Desarrollo de la pestaña integrales-----
    #-----------Parte Indefinidas-----------------
        #Ecuacion
    ecuaI = tk.Label(pes0, text ="Digite el problema:", width = "35", height = "1", font = ("Helvetica 14"), bg = 'white')
    caja1 = Entry(pes0, width = 40, font = ("Helvetica 16"), highlightbackground = '#007b99', highlightcolor = '#f39200', highlightthickness = 3)
        #Resultado    
    resulI = tk.Label(pes0, text = "El resultado de la integral es:", width = "35", height = "1", font = ("Helvetica 14"),  bg = 'white')
    muestraI = tk.Label(pes0, text = "" , width = "35", height = "1", font = ("Helvetica 14 italic bold"), foreground = "#007b99", background = "#f39200")
        #Grafica
    graficaI = tk.Label(pes0, text ="¿Desea conocer la grafica de la integral?", width = "35", height = "1", font = ("Helvetica 14"), bg = 'white')
        #Menu Despegable
    menuI = ttk.Combobox(pes0, width = "35", font = ("Helvetica 18"), state = "readonly", foreground = "#007b99",
                         values = ["Si.", 
                                   "Si, mostrando la grafica de la integral."])
    menuI.current()#Valor por defectos
        #Botones de verificacion
    def obtenerI():
        funcion  = caja1.get()
        respuesta = menuI.get()
        menuI.select_clear()
        solucion = muestraI.cget("text")
        prueba2 = graficaIS(funcion, solucion, respuesta)

    def limpiarI():
        caja1.delete(0, END)
        muestraI.config(text = "")
        menuI.set("")
        messagebox.showinfo("Informacion", "La ecuacion y ha sido borrada")
        caja1.focus_set()
        
    def save():
        prueba = caja1.get()
        solucion = ecuacionI(prueba)
        muestraI.config(text = solucion)
        
    botonGraf = Button(pes0, text = "Grafica", width = "20", font = ("Helvetica 14 bold"),
                    command = obtenerI, foreground = "white", bg = '#007b99', activebackground = 'white', activeforeground = '#007b99')
    boton3 = Button(pes0, text = "Borrar", width = "20", height = "1", font = ("Helvetica 14 bold"), 
                    command = limpiarI, foreground = "white", bg = '#007b99', activebackground = 'white', activeforeground = '#007b99')
    boton4 = Button(pes0, text = "Ingresar", width = "20", height = "1", font = ("Helvetica 14 bold"),
                    command = save, foreground = "white", bg = '#007b99', activebackground = 'white', activeforeground = '#007b99')
    #-----------Parte Definidas-----------------
        #Limites
    limInfe = tk.Label(pes0, text="Ingrese limite inferior:", width = "35", height = "1", font = ("Helvetica 14"), bg = 'white')
    cajaInfe = Entry(pes0, width = 20, font = ("Helvetica 16"), highlightbackground = '#007b99', highlightcolor = '#f39200', highlightthickness = 3)
    limSupe = tk.Label(pes0, text="Ingrese limite superior:", width = "35", height = "1", font = ("Helvetica 14"), bg = 'white')
    cajaSupe = Entry(pes0, width = 20, font = ("Helvetica 16"), highlightbackground = '#007b99', highlightcolor = '#f39200', highlightthickness = 3)
        #Ecuacion
    ecuaD = tk.Label(pes0, text ="Digite la ecuacion:", width = "35", height = "1", font = ("Helvetica 14"), bg = 'white')
    caja2 = Entry(pes0, width = 40, font = ("Helvetica 16"), highlightbackground = '#007b99', highlightcolor = '#f39200', highlightthickness = 3)
        #Pregunta
    question = '''      ¿Desea conocer el resultado
    en fraccionario o en decimales ?'''
    pregu = tk.Label(pes0, text = question, width = "35", height = "2", font = ("Helvetica 14"), justify = tk.LEFT, bg = 'white')
        #Menu Despegable
    menuD =  ttk.Combobox(pes0, width = "35", font = ("Helvetica 14"), state = "readonly", foreground = "#007b99")
    menuD['values'] = (  "Fraccionario.",
                         "Decimales.")
    menuD.current()
        #Solucion
    resulD = tk.Label(pes0, text = "El resultado de la integral es:", width = "35", height = "1", font = ("Helvetica 14"),  bg="white")
    muestraD = tk.Label(pes0, text = "", width = "35", height = "1", font = ("Helvetica 14 italic bold"), bg = "white", foreground = "#007b99", 
                        background = "#f39200")

        #Botones de verificacion
    def limpiarD():
        cajaInfe.delete(0, END)
        cajaSupe.delete(0, END)
        caja2.delete(0, END)
        menuD.set("")
        muestraD.config(text = "")
        messagebox.showinfo("Informacion", "Los valores ingresados han sido borrados")
        cajaInfe.focus_set()

    def obtenerD():
        LimI = cajaInfe.get()
        LimS = cajaSupe.get()
        ec   = caja2.get()
        res  = menuD.get()
        menuD.select_clear()
        solucionI = ecuacionD(LimI, LimS, ec, res)
        muestraD.config(text = solucionI)

    boton5 = Button(pes0, text = "Borrar", width = "20", height = "1", font = ("Helvetica 14 bold"), 
                    command = limpiarD, foreground = "white", bg = '#007b99', activebackground = 'white', activeforeground = '#007b99')
    boton6 = Button(pes0, text = "Resultado", width = "20", height = "1", font = ("Helvetica 14 bold"),
                    command = obtenerD, foreground = "white", bg = '#007b99', activebackground = 'white', activeforeground = '#007b99')
    boton7 = Button(pes0, text = "Grafica", width = "20", height = "1", font = ("Helvetica 14 bold"),
                    command = lambda: graficaES(caja2.get()), foreground = "white", bg = '#007b99', activebackground = 'white', 
                    activeforeground = '#007b99')

    #ShowWidgets
    def indefi():
        caja1.focus_set()
        ocultarD()
        ecuaI.grid(row = 2, column = 0, pady = 5)
        caja1.place(x = 630, y = 120)
        resulI.grid(row = 3, column = 0, pady = 25)
        muestraI.place(x = 630, y = 180)
        graficaI.grid(row = 4, column = 0, pady = 10)
        menuI.place(x = 630, y = 245)
        boton3.grid(row = 6, column= 0, pady = 30)
        boton4.grid(row = 6, column= 1)
        botonGraf.place(x = 460, y = 310)

    def defi():
        cajaInfe.focus_set()
        ocutarI()
        limInfe.grid(row = 2, column = 0)
        cajaInfe.place(x = 630 , y = 115)
        limSupe.grid(row = 3, column= 0, pady = 25)
        cajaSupe.place(x = 630 , y = 170)
        ecuaD.grid(row = 4, column = 0, pady = 4)
        caja2.place(x = 630 , y = 225)
        pregu.grid(row = 5, column = 0, pady = 25)
        menuD.place(x = 630 , y = 310)
        resulD.grid(row = 7, column = 0)
        muestraD.place( x = 630, y = 360)    
        boton5.grid(row = 8, column = 0, pady = 25)
        boton6.grid(row = 8, column = 1)
        boton7.place(x = 461, y = 411)

    #OcultarWidgets
    def ocutarI():
        ecuaI.grid_forget()
        caja1.place_forget()
        graficaI.grid_forget()
        menuI.place_forget()
        resulI.grid_forget()
        muestraI.place_forget()
        boton3.grid_forget()
        boton4.grid_forget()
        botonGraf.place_forget()
        
    def ocultarD():
        limInfe.grid_forget()
        cajaInfe.place_forget()
        limSupe.grid_forget()
        cajaSupe.place_forget()
        ecuaD.grid_forget()
        caja2.place_forget()
        pregu.grid_forget()
        menuD.place_forget()
        resulD.grid_forget()
        muestraD.place_forget()
        boton5.grid_forget()
        boton6.grid_forget()
        boton7.place_forget()
        
    #Botones_I&D
    boton1 = Button(pes0, text = "INDEFINIDAS", width = "78", height = "3", font = ("Calibri 10 bold italic"),
                    command = indefi, foreground = "white", bg = '#007b99', activebackground = 'white', activeforeground = '#007b99')
    boton2 = Button(pes0, text = "DEFINIDAS", width = "80", height = "3", font = ("Calibri 10 bold italic"),
                    command = defi, foreground = "white", bg = '#f39200', activebackground = 'white', activeforeground = '#f39200')
    #AGG botenes en pantalla
    boton1.grid(row = 1, column=0, padx = 16, pady = 30)
    boton2.grid(row = 1, column=1, padx = 8, pady = 30)

    #--------Desarrollo de la pestaña areas-----
    pes1 = tkinter.Frame(notebook,background="white")
    pes2 = tkinter.Frame(notebook,background="white")
#------------------------------------------------------------------- INICIO PARTE DE VOLUMEN-----------------------------------------------------------------------#
#HABILITAR TEXTBOX PARA SEGUNDA FUNCION    
    def Habilitar():
        boxFuncion2.config(state=NORMAL)

    def LimpiarCampos():
        boxFuncion1.delete(0, END)
        boxFuncion2.delete(0 , END)
        boxLimi1.delete(0 , END)
        boxLimi2.delete(0 , END)
        boxFuncion1.focus_set()
        boxFuncion2.config(state=DISABLED)
        FuncionMayor =  Label(pes2, text="", width="500", height="35", bg='white')
        FuncionMayor.place(x=540, y=25, width=500, height=35)
        FuncionMenor = Label(pes2, text="", width="500", height="35", bg='white')
        FuncionMenor.place(x=540, y=60, width=500, height=35)
        ResultadoVolumen = Label(pes2, text="", width="500", height=35, bg='white')
        ResultadoVolumen.place(x=540, y=90, width="500", height="35")
#FUNCION QUE GRAFICA CON LAS EXPRESIONES DADAS EN LOS TEXTBOX'S
    def Grafica():
        Expresion1 = boxFuncion1.get()
        if not Expresion1:
            messagebox.showerror("Error", "Ingrese una funcion") 
        Expresion2 = boxFuncion2.get()
        if not Expresion2:
            Expresion2 = 0
        Limite1 = boxLimi1.get()
        Limite2 = boxLimi2.get()
        Graficar(Expresion1, Expresion2, Limite1, Limite2)
#FUNCION PARA HACER EL PROCESO DEL CALCULO DEL VOLUMEN
    def vol():
        Expresion1=boxFuncion1.get()
        if not Expresion1:
            messagebox.showerror("Error", "Ingrese una función")
        Expresion2=boxFuncion2.get()
        if not Expresion2:
            Expresion2=0 #EN LA CAJA 2 PARA SEGUNDA FUNCIÓN LLEVAR CERO SI NO DIGITÓ NADA
        Limite1=boxLimi1.get()
        Limite2=boxLimi2.get()
        auxResultado=volumenTotal(Expresion1,Expresion2,Limite1, Limite2)
        Expresion1 = auxResultado[0]
        Expresion2 = auxResultado[1]
        auxilio3 = auxResultado[2]
        FuncionMayor =  Label(pes2, text="Función Mayor: " + str(Expresion1),width = "500", height = "35", font = ("Helvetica 16"), bg='white') #SALIDAS DE EXPRESIONES MENORES Y MAYORES
        FuncionMayor.place(x=540, y=25, width=500, height=35)
        FuncionMenor = Label(pes2, text="Función Menor: " + str(Expresion2),width = "500", height = "35", font = ("Helvetica 16"), bg='white')
        FuncionMenor.place(x=540, y=60, width=500, height=35)
        ResultadoVolumen = Label(pes2, text="El volúmen total: " + str(auxilio3),width = "500", height = "35", font = ("Helvetica 16"), bg='white')
        ResultadoVolumen.place(x=540, y=90, width=500, height=35)
 #ETIQUETAS DE TEXTO
    lblFuncion1=Label(pes2, text="Ingrese la función en términos de x:", width = "35", height = "1", font = ("Helvetica 14"), bg='white') #PRIMERA FUNCIÓN
    lblFuncion1.place(x=20, y=25, width=300, height=25)#POSICIONAMIENTO 

    lblFuncion2=Label(pes2,text="Ingrese la función en términos de x:", width = "35", height = "1", font = ("Helvetica 14"), bg='white')
    lblFuncion2.place(x=20, y=100, width=300, height=25)#POSICIONAMIENTO

    lblLimite1=Label(pes2,text="Ingrese límite inferior:", width = "35", height = "1", font = ("Helvetica 14"), bg='white')#PRIMER LIMITE (INFERIOR)
    lblLimite1.place(x=20, y=175, width=225, height=30)#POSICIONAMIENTO

    lbllimite2=Label(pes2,text="Ingrese limite superior:", width = "35", height = "1", font = ("Helvetica 14"), bg='white')#SEGUNDO LIMITE (SUPERIOR)
    lbllimite2.place(x=20, y=250, width=225, height=30)#POSICIONAMIENTO
#CAJAS DE ENTRADA DE FUNCIONES
    boxFuncion1=Entry(pes2, width=20, font=("Helvetica 16"),highlightbackground='#007b99', highlightcolor='#f39200', highlightthickness=3 ) #CAJA PARA PRIMERA FUNCION
    boxFuncion1.place(x=325,y=25, width=205, height=30)#POSICIONAMIENTO

    boxFuncion2=Entry(pes2, state=DISABLED,width=20, font=("Helvetica 16"),highlightbackground='#007b99', highlightcolor='#f39200', highlightthickness=3 )#CAJA PARA SEGUNDA FUNCION
    boxFuncion2.place(x=325, y=100, width=205, height=30)#POSICIONAMIENTO

    boxLimi1=Entry(pes2,width=20, font=("Helvetica 16"),highlightbackground='#007b99', highlightcolor='#f39200', highlightthickness=3)#CAJA PARA LIMITE INFERIOR
    boxLimi1.place(x=235, y=175, width=145, height=25)#POSICIONAMIENTO

    boxLimi2=Entry(pes2, width=20, font=("Helvetica 16"),highlightbackground='#007b99', highlightcolor='#f39200', highlightthickness=3)#CAJA PARA LIMITE SUPERIOR
    boxLimi2.place(x=235, y=250, width=145, height=25)#POSICIONAMIENTO
#BOTONERA
    buttonCalcular=Button(pes2,text="Calcular", command= vol, width = "20", height = "1", font = ("Helvetica 14"),foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')#BOTÓN PARA CALCULAR EL VOLUMEN
    buttonCalcular.place(x=20, y=350, width=80, height=45)#POSICIONAMIENTO

    buttonGrafica=Button(pes2, text="Gráfica", command=Grafica, width = "20", height = "1", font = ("Helvetica 14"),foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')#Llama a la funcion de la gráfica
    buttonGrafica.place(x=110, y=350, width=90, height=45)

    buttonLimpiar=Button(pes2, text="Limpiar Campos", command=LimpiarCampos, width = "20", height = "1", font = ("Helvetica 14"),foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
    buttonLimpiar.place(x=20, y=400, width=180, height=30)

    buttonHabilitar=Button(pes2, text="Añadir función", command=Habilitar, width = "20", height = "1", font = ("Helvetica 14"),foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
    buttonHabilitar.place(x=20, y=435,width=180, height=30)
#----------------------------------------------------------------------------FIN PARTE VOLUMEN----------------------------------------------------------------------------#
    pes3 = tkinter.Frame(notebook,background="white")
    notebook.add(pes0, text='Integrales')
    notebook.add(pes1, text='Area')
    notebook.add(pes2, text='Volumen')
    notebook.add(pes3, text='About Us')
    ventana.geometry("1200x650")
    ventana.resizable(1,1)
    ventana.mainloop()

if __name__=='__main__':
    main()