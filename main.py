from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter
from tkinter import font
import tkinter.font as tkFont

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
                                            "font":"Calibri, 11 "
                                            }}}  
    style.theme_create("mi_estilo", parent="alt", settings=settings)
    style.theme_use("mi_estilo")
    
    notebook = ttk.Notebook(ventana)
    notebook.pack(fill='both', expand='yes',padx=5, pady=20)
    notebook.pressed_index = None
    pes0 = tkinter.Frame(notebook,background="white")
    pes1 = tkinter.Frame(notebook,background="white")
    pes2 = tkinter.Frame(notebook,background="white")
    pes3 = tkinter.Frame(notebook,background="white")
    notebook.add(pes0, text='Integrales')   
    notebook.add(pes1, text='Área')
    notebook.add(pes2, text='Volumen')
    notebook.add(pes3, text='About Us')
    volumen=Label(pes2, text="Volúmen Sólidos de Revolución")
    volumen.place(x=500, y=2)
    #volumen.pack()
    ventana.geometry("1200x650")
    ventana.resizable(1,1)

    #ETIQUETAS DE TEXTO
    lblFuncion1=Label(pes2, text="Ingrese la función") #PRIMERA FUNCIÓN
    lblFuncion1.place(x=10, y=10, width=100, height=30)#POSICIONAMIENTO

    lblFuncion2=Label(pes2,text="Ingrese la función")
    lblFuncion2.place(x=10, y=70, width=100, height=30)
    
    #CAJAS DE ENTRADA DE FUNCIONES
    boxFuncion1=Entry(pes2) #CAJA PARA PRIMERA FUNCION
    boxFuncion1.place(x=10,y=35, width=100, height=30)
    boxFuncion2=Entry(pes2)#CAJA PARA SEGUNDA FUNCION
    boxFuncion2.place(x=10, y=100, width=100, height=30)




    ventana.mainloop()

if __name__=='__main__':
    main()