from tkinter import *
import tkinter as tk




raizito = Tk()
raizito.title("Cantbilidad")
raizito.geometry("700x500")

#Barra de tareas
barra_menu = tk.Menu()
menu_archivo = tk.Menu(barra_menu, tearoff=False)
barra_menu.add_cascade(menu=menu_archivo, label="Archivo")
barra_menu.add_cascade(menu=menu_archivo, label="Sistema")
barra_menu.add_cascade(menu=menu_archivo, label="Acerca de")
raizito.config(menu=barra_menu)
#barra de tareas
#Imagenes
Imagne_1 = PhotoImage(file="/home/mrarcani/Documentos/Proyectos/PYTHON/Contabilidad/Conta_imagenes/LibroNegro.jpg")
#Imganes

Titulo = Label(raizito, text="Sistema contable",font=("Helvetica", 30, "bold")).grid(row=0,columnspan=4)
titulo1= Label(raizito, text="Libro Diario", font=30).grid(row=1, column=1)
boton1 = Button(raizito,width=30, image=Imagne_1, height=10)
boton1.grid(row=2, column=1)
titulo2= Label(raizito, text="Libro Mayor", font=30).grid(row=1, column=2)
boton2 = Button(raizito, text="Ejemplo2" ,width=30, height=10 ).grid(row=2, column=2)
titulo1= Label(raizito, text="Comprobacion de suma y Saldos",font=30).grid(row=3, columnspan=3)
boton3 = Button(raizito, text="Ejemplo2",width=30, height=10).grid(row=4, columnspan=3)
raizito.config(bg="Aqua")
raizito.mainloop()