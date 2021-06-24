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
    integrales= tkinter.Label(pes0,text="haga algo snakeeeeeeeeee")
    integrales.pack()
    ventana.geometry("1200x650")
    ventana.resizable(1,1)
    ventana.mainloop()

if __name__=='__main__':
    main()