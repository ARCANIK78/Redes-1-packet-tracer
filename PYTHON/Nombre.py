from tkinter import *
from tkinter import messagebox

raiz = Tk()
raiz.title("Acceso")
raiz.geometry("500x200")
#Fuincones
def Accediste():
    messagebox.showinfo(message="Perfecto")

#textos y label del fondo
Texto_1 =Label(raiz, text="Accede a la Cuenta",bg="Aqua",font=("Helvetica", 15, "bold")).grid(row=0,columnspan=3)
Texto_2 = Label(raiz, text="Usuario ",bg="Aqua", ).grid(column=0,row=1)
Texto_2 = Label(raiz, text="Contraseña ",bg="Aqua").grid(column=0,row=2)

Nombre=Entry(raiz).grid(column=1,row=1)
contraseña=Entry(raiz, show="*").grid(column=1, row=2)

Boton = Button(raiz, text="Ingresea", font="Helvetica", command=Accediste).grid(row=3,columnspan=3)


raiz.config(background="Aqua")
raiz.mainloop()