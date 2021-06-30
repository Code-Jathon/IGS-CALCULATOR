from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter
import tkinter.font as tkFont
from tkinter import messagebox 
from areas import *
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
    pes1 = tkinter.Frame(notebook,background="white")
    pes2 = tkinter.Frame(notebook,background="white")
    pes3 = tkinter.Frame(notebook,background="white")
    notebook.add(pes0, text='Integrales')

    #Parte Area   
    notebook.add(pes1, text='Área')
    fun1=tk.Label(pes1,text="Ingrese la funcion en terminos de x: ", width="35", height="1", font=("Helvetica 14"), bg='white')
    fun1.grid(row=2, column=0, pady=4)
    caj1 = Entry(pes1, width= 45, font = ("Helvetica 16"), highlightbackground='#007b99', highlightcolor='#f39200', highlightthickness=3)
    caj1.grid(row=2, column=1, pady=4)
    #accion boton
    def sefu():
        fun2.grid(row=4, column=0)
        caj2.grid(row=4,column=1)

    bot2fun = tk.Button(pes1, text="Añadir segunda funcion", width = "20", height = "1", command=sefu 
    , font = ("Helvetica 14"),foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
    bot2fun.grid(row=3,column=0, pady= 6)
    fun2=tk.Label(pes1,text="Ingrese la funcion en terminos de x: ", width = "35", height = "1", font = ("Helvetica 14"), bg='white')
    caj2 = Entry(pes1, width= 45, font= ("Calibri 16"), highlightbackground='#007b99'
    , highlightcolor='#f39200', highlightthickness=3)
    #accion boton
    def pun_cor():
        e1 = caj1.get()
        if not e1:
            messagebox.showerror("Error", "Ingrese una funcion") 
        e2 = caj2.get()
        if not e2:
            e2 = 0
        aux1 = puntos_corte(e1, e2)
        resultPc = tk.Label(pes1, text="Los puntos de corte son: " + str(aux1), width = "35", height = "1"
        , font = ("Helvetica 14"), bg='white')
        resultPc.grid(row=6,column=0)

    botpun = tk.Button(pes1, text="Calcular puntos de corte", width = "20", height = "1", command = pun_cor
    , font = ("Helvetica 14") ,foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
    botpun.grid(row=5, column=0, pady= 8)
    liminfe = tk.Label(pes1, text="Ingrese limite inferior: ", width = "35", height = "1", font = ("Helvetica 14"), bg='white')
    liminfe.grid(row=7, column=0)
    caj3 = Entry(pes1,width= 45, font= ("Calibri 16"), highlightbackground='#007b99', highlightcolor='#f39200', highlightthickness=3)
    caj3.grid(row=7, column=1, pady= 9)
    limsupe = tk.Label(pes1, text="Ingrese limite superior: ", width = "35", height = "1", font = ("Helvetica 14"), bg='white')
    limsupe.grid(row=10, column=0)
    caj4 = Entry(pes1,width= 45, font= ("Calibri 16"), highlightbackground='#007b99', highlightcolor='#f39200', highlightthickness=3)
    caj4.grid(row=10, column=1, pady= 11)
    #accion boton
    def are():
        e1 = caj1.get()
        if not e1:
            messagebox.showerror("Error", "Ingrese una funcion") 
        e2 = caj2.get()
        if not e2:
            e2 = 0
        l1 = caj3.get()
        l2 = caj4.get()
        aux2 = area(e1, e2, l1, l2)
        e1 = aux2[0]
        e2 = aux2[1]
        aux3 = aux2[2]
        funmay = tk.Label(pes1, text="La funcion mayor es: " + str(e1), width = "35", height = "1", font = ("Helvetica 14"), bg='white')
        funmay.grid(row=16,column=0)
        funmen = tk.Label(pes1, text="La funcion menor es: " + str(e2), width = "35", height = "1", font = ("Helvetica 14"), bg='white')
        funmen.grid(row=18,column=0)      
        resulta = tk.Label(pes1, text="El area de la funcion es: " + str(aux3) + " U²", width = "35", height = "1", font = ("Helvetica 14"), bg='white')
        resulta.grid(row=20,column=0)

    botresult = tk.Button(pes1, text="Calcular", width = "20", height = "1",command = are, font = ("Helvetica 14")
    ,foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
    botresult.grid(row=14,column=0, pady=12)  
    #accion boton
    def gra():
        e1 = caj1.get()
        if not e1:
            messagebox.showerror("Error", "Ingrese una funcion") 
        e2 = caj2.get()
        if not e2:
            e2 = 0
        l1 = caj3.get()
        l2 = caj4.get()
        graficar(e1, e2, l1, l2)

    botgraf = tk.Button(pes1, text="Graficar", width = "20", height = "1",command = gra, font = ("Helvetica 14")
    ,foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
    botgraf.grid(row=24,column=0, pady=16)  
    #accion boton
    def eliminar():
        caj1.delete(0, END)
        caj2.delete(0 , END)
        caj3.delete(0 , END)
        caj4.delete(0 , END)
        caj1.focus_set()
        resultPc = tk.Label(pes1, text=" ", width = "35", height = "1", font = ("Helvetica 14"), bg='white')
        resultPc.grid(row=6,column=0)
        funmay = tk.Label(pes1, text=" ", width = "35", height = "1", font = ("Helvetica 14"), bg='white')
        funmay.grid(row=16,column=0)
        funmen = tk.Label(pes1, text=" ", width = "35", height = "1", font = ("Helvetica 14"), bg='white')
        funmen.grid(row=18,column=0)      
        resulta = tk.Label(pes1, text=" " , width = "35", height = "1", font = ("Helvetica 14"), bg='white')
        resulta.grid(row=20,column=0)

    botelim = tk.Button(pes1, text="Limpiar", width = "20", height = "1", command = eliminar, font = ("Helvetica 14")
    ,foreground="white", bg='#007b99', activebackground='white', activeforeground='#007b99')
    botelim.grid(row=24,column=1, pady=20)  

    notebook.add(pes2, text='Volumen')
    notebook.add(pes3, text='About Us')
    ventana.geometry("1200x650")
    ventana.resizable(1,1)
    ventana.mainloop()

if __name__=='__main__':
    main()