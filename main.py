from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter
import tkinter.font as tkFont
from integralesIndefinidas import *
from integralesDefinidas import *

def main():
    ventana= Tk()
    ventana.config(bg="gray",bd=0)
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
    notebook.pack(fill='both', expand='yes',padx=7, pady=20)
    notebook.pressed_index = None
    pes0 = tkinter.Frame(notebook,background="#b8ad9b")
    #--------Desarrollo de la pestaña integrales-----
    #PartIndefi
    def save():
        prueba = caja1.get()
        solucion = ecuacionI(prueba)
        muestraI.config(text = solucion)

        #Ecuacion
    ecuaI = tk.Label(pes0, text ="Digite el problema:", width = "35", height = "1", font = ("Calibri 14 italic"))
    caja1 = Entry(pes0, width = 45, font = ("Calibri 16"))
        #Botones de verificacion
    boton3 = Button(pes0, text = "Borrar", width = "20", height = "1", font = ("Calibri 14 bold italic"), 
                    command = lambda: caja1.delete(0, END))
    boton4 = Button(pes0, text = "Ingresar", width = "20", height = "1", font = ("Calibri 14 bold italic"),
                    command = save)
    
        #Resultado    
    resulI = tk.Label(pes0, text = "El resultado de la integral es:", width = "35", height = "1", font = ("Calibri 14 italic"))
    muestraI = tk.Label(pes0, text = "" , width = "35", height = "1", font = ("Calibri 14 italic"))
        #Menu Despegable
    def obtenerI():
        funcion  = caja1.get()
        respuesta = menuI.get()
        solucion = muestraI.cget("text")
        prueba2 = graficaIS(funcion, solucion, respuesta)

    #Grafica
    graficaI = tk.Label(pes0, text ="¿Desea conocer la grafica de la integral?", width = "35", height = "1", font = ("Calibri 14 italic"))
    menuI = ttk.Combobox(pes0, width = "35", font = ("Calibri 14 italic"), state = "readonly")
    menuI['values'] = ( "Si.",
                        "Si, mostrando la grafica de la integral.")
    menuI.current()#Valor por defectos
    botonGraf = Button(pes0, command = obtenerI, text = "Grafica", width = "20", font = ("Calibri 14 bold italic"))
    
    #PartDefi
    def obtenerD():
        LimI = cajaInfe.get()
        LimS = cajaSupe.get()
        ec   = caja2.get()
        res  = menuD.get()
        solucionI = ecuacionD(LimI, LimS, ec, res)
        muestraD.config(text = solucionI)

        #Limites
    limInfe = tk.Label(pes0, text="Ingrese limite inferior:", width = "35", height = "1", font = ("Calibri 14 italic"))
    cajaInfe = Entry(pes0, width = 20, font = ("Calibri 16"))
    limSupe = tk.Label(pes0, text="Ingrese limite superior:", width = "35", height = "1", font = ("Calibri 14 italic"))
    cajaSupe = Entry(pes0, width = 20, font = ("Calibri 16"))
        #Ecuacion
    ecuaD = tk.Label(pes0, text ="Digite la ecuacion:", width = "35", height = "1", font = ("Calibri 14 italic"))
    caja2 = Entry(pes0, width = 45, font = ("Calibri 16"))
        #Pregunta
    question = '''          ¿Desea conocer el resultado
    en fraccionario o en decimales ?'''
    pregu = tk.Label(pes0, text = question, width = "35", height = "2", font = ("Calibri 14 italic"), justify = tk.LEFT)
    menuD =  ttk.Combobox(pes0, width = "35", font = ("Calibri 14 italic"), state = "readonly")
    menuD['values'] = (  "Fraccionario.",
                            "Decimales.")
    menuD.current()

        #Botones de verificacion
    boton5 = Button(pes0, text = "Borrar", width = "20", height = "1", font = ("Calibri 14 bold italic"), 
                    command = lambda: caja2.delete(0, END))
    boton6 = Button(pes0, text = "Resultado", width = "20", height = "1", font = ("Calibri 14 bold italic"),
                    command = obtenerD)

    resulD = tk.Label(pes0, text = "El resultado de la integral es:", width = "35", height = "1", font = ("Calibri 14 italic"))
    muestraD = tk.Label(pes0, text = "", width = "35", height = "1", font = ("Calibri 14 italic"))

    def indefi():
        ocultarD()
        ecuaI.grid(row = 2, column = 0, pady = 5)
        caja1.grid(row = 2, column = 1)
        boton3.grid(row = 3, column= 0, pady = 30)
        boton4.grid(row = 3, column= 1)
        resulI.grid(row = 4, column = 0, pady = 5)
        muestraI.place(x = 630, y = 260)
        graficaI.grid(row = 5, column = 0, pady = 30)
        menuI.place(x = 630, y = 325)
        botonGraf.grid(row = 6, column = 1, pady = 5)   

    def defi():
        ocutarI()
        limInfe.grid(row = 2, column = 0)
        cajaInfe.place(x = 630 , y = 115)
        limSupe.grid(row = 3, column= 0, pady = 25)
        cajaSupe.place(x = 630 , y = 170)
        ecuaD.grid(row = 4, column = 0, pady = 4)
        caja2.grid(row = 4, column = 1)
        pregu.grid(row = 5, column = 0, pady = 25)
        menuD.place(x = 630 , y = 310)
        resulD.grid(row = 7, column = 0)
        muestraD.place( x = 630, y = 360)    
        boton5.grid(row = 8, column = 0, pady = 25)
        boton6.grid(row = 8, column = 1)

    #OcultarWidgets
    def ocutarI():
        ecuaI.grid_forget()
        caja1.grid_forget()
        boton3.grid_forget()
        boton4.grid_forget()
        graficaI.grid_forget()
        menuI.place_forget()
        botonGraf.grid_forget()
        resulI.grid_forget()
        muestraI.place_forget()
        
    def ocultarD():
        limInfe.grid_forget()
        cajaInfe.place_forget()
        limSupe.grid_forget()
        cajaSupe.place_forget()
        ecuaD.grid_forget()
        caja2.grid_forget()
        pregu.grid_forget()
        menuD.place_forget()
        boton5.grid_forget()
        boton6.grid_forget()
        resulD.grid_forget()
        muestraD.place_forget()
        
    #Botones_I&D
    boton1 = Button(pes0, text = "INDEFINIDAS", width = "78", height = "3", command = indefi, font = ("Calibri 10 bold italic"))
    boton2 = Button(pes0, text = "DEFINIDAS", width = "80", height = "3", command = defi, font = ("Calibri 10 bold italic"))
    #AGG botenes en pantalla
    boton1.grid(row = 1, column=0, padx = 16, pady = 30)
    boton2.grid(row = 1, column=1, padx = 8, pady = 30)

    #--------Desarrollo de la pestaña areas-----
    pes1 = tkinter.Frame(notebook,background="white")
    pes2 = tkinter.Frame(notebook,background="white")
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