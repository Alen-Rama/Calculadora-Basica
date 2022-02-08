from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Calculadora")
root.iconbitmap("C:\\Users\\alenr\\OneDrive\\Escritorio\\Python\\Calculadora\\images-removebg-preview.ico")


#? VARIABLES|-------------------------------------------------------------------------------------------------------


calculadoraPantalla = StringVar()
resultado = 0
operacion = ""
operacion2 = False
numero = False
punto = False
error = False
desabilitados = False
numeroPantalla = 0
cero = False
coma = False
ceroDesabilitado = False
texto = False


#? FUNCIONES|-------------------------------------------------------------------------------------------------------


def boton(num):
    global operacion2
    global numero
    global desabilitados
    global cero
    global coma
    if num != "0" and num != ".":
        numero = True
    if ceroDesabilitado and numero:
        cuadroPantalla.delete(0, "end")
    if num == ".":
        coma = True
    if num == "0" and not(coma) and not(numero):
        desabilitarCero()
    if num != "0":
        habilitarCero()
    if desabilitados:
        habilitarBotones()
        desabilitados = False
    if operacion2:
        cuadroPantalla.delete(0, "end")
    if num != "0" or numero or not(cero):
        calculadoraPantalla.set(calculadoraPantalla.get() + num)
        operacion2 = False
    if num == ".":
        desabilitarPunto()


def desenfocar():
    root.focus()


def desabilitarCero():
    global ceroDesabilitado
    boton0['state'] = DISABLED
    ceroDesabilitado = True


def habilitarCero():
    global ceroDesabilitado
    boton0['state'] = NORMAL
    ceroDesabilitado = False


def controlarCeros():
    global numeroPantalla
    global resultado
    global texto
    count = 0
    for i in calculadoraPantalla.get()[calculadoraPantalla.get().find('.')+1:]:
        if i == "0":
            count += 1
        else:
            break
    if count == len(calculadoraPantalla.get()[calculadoraPantalla.get().find('.'):])-1:
        try:
            numeroPantalla = float(calculadoraPantalla.get())
            numeroPantalla = int(numeroPantalla)
        except ValueError:
            messagebox.showwarning("¡Atención!", "Ingrese un número valido por favor")
            texto = True
    else:
        try:
            numeroPantalla = float(calculadoraPantalla.get())
        except ValueError:
            messagebox.showwarning("¡Atención!", "Ingrese un número valido por favor")
            texto = True


def controlarCerosResultado():
    global resultado
    global texto
    resultado = str(resultado)
    count = 0
    for i in resultado[resultado.find('.')+1:]:
        if i == "0":
            count += 1
        else:
            break
    if count == len(resultado[resultado.find('.'):])-1:
        try:
            numeroPantalla = float(resultado)
            numeroPantalla = int(numeroPantalla)
            resultado = numeroPantalla
        except ValueError:
            messagebox.showwarning("¡Atención!", "Ingrese un número valido por favor")
            texto = True
    else:
        try:
            numeroPantalla = float(resultado)
            resultado = numeroPantalla
        except ValueError:
            messagebox.showwarning("¡Atención!", "Ingrese un número valido por favor")
            texto = True


def operaciones():
    global operacion
    global resultado
    global error
    global numeroPantalla
    if operacion == "":
        controlarCeros()
        resultado = numeroPantalla
    if operacion == "suma":
        controlarCeros()
        resultado += numeroPantalla
    if operacion == "resta":
        controlarCeros()
        resultado -= numeroPantalla
    if operacion == "producto":
        controlarCeros()
        resultado *= numeroPantalla
    if operacion == "divicion":
        controlarCeros()
        try:
            resultado /= numeroPantalla
        except ZeroDivisionError:
            messagebox.showwarning("¡Atención!", "No se puede dividir entre 0")
            resultado = 0
            error = True


def desabilitarPunto():
    global punto
    botonPunto['state'] = DISABLED
    punto = True


def habilitarPunto():
    botonPunto['state'] = NORMAL


def desabilitarBotones():
    global desabilitados
    global error
    if error:
        botonSuma['state'] = DISABLED
        botonResta['state'] = DISABLED
        botonProducto['state'] = DISABLED
        botonDividir['state'] = DISABLED
        botonPunto['state'] = DISABLED
        desabilitados = True
        error = False


def habilitarBotones():
    global operacion
    global resultado
    botonSuma['state'] = NORMAL
    botonResta['state'] = NORMAL
    botonProducto['state'] = NORMAL
    botonDividir['state'] = NORMAL
    botonPunto['state'] = NORMAL
    operacion = ""
    resultado = 0
    calculadoraPantalla.set(resultado)


def suma():
    global operacion
    global operacion2
    global resultado
    global punto
    global error
    global cero
    global numero
    global coma
    global texto
    operacion2 = True
    operaciones()
    operacion = "suma"
    controlarCerosResultado()
    if texto:
        calculadoraPantalla.set('')
        resultado = 0
        texto = False
    else:
        calculadoraPantalla.set(resultado)
    if error:
        resultado = 0
        desabilitarBotones()
        calculadoraPantalla.set('')
    cero = False
    numero = False
    if punto:
        habilitarPunto()
    coma = False


def resta():
    global resultado
    global operacion
    global operacion2
    global punto
    global error
    global cero
    global numero
    global coma
    global texto
    operacion2 = True
    operaciones()
    operacion = "resta"
    controlarCerosResultado()
    if texto:
        calculadoraPantalla.set('')
        resultado = 0
        texto = False
    else:
        calculadoraPantalla.set(resultado)
    if error:
        resultado = 0
        desabilitarBotones()
        calculadoraPantalla.set('')
    cero = False
    numero = False
    if punto:
        habilitarPunto()
    coma = False


def producto():
    global resultado
    global operacion
    global operacion2
    global punto
    global error
    global cero
    global numero
    global coma
    global texto
    operacion2 = True
    operaciones()
    operacion = "producto"
    controlarCerosResultado()
    if texto:
        calculadoraPantalla.set('')
        resultado = 0
        texto = False
    else:
        calculadoraPantalla.set(resultado)
    if error:
        resultado = 0
        desabilitarBotones()
        calculadoraPantalla.set('')
    cero = False
    numero = False
    if punto:
        habilitarPunto()
    coma = False


def divicion():
    global resultado
    global operacion
    global operacion2
    global punto
    global error
    global cero
    global numero
    global coma
    global texto
    operacion2 = True
    operaciones()
    operacion = "divicion"
    controlarCerosResultado()
    if texto:
        calculadoraPantalla.set('')
        resultado = 0
        texto = False
    else:
        calculadoraPantalla.set(resultado)
    if error:
        resultado = 0
        desabilitarBotones()
        calculadoraPantalla.set('')
    cero = False
    numero = False
    if punto:
        habilitarPunto()
    coma = False


def igual():
    global resultado
    global operacion
    global operacion2
    global numero
    global punto
    global error
    global desabilitados
    global cero
    global coma
    global texto
    if not(desabilitados):
        operaciones()
    controlarCerosResultado()
    if texto:
        calculadoraPantalla.set('')
        resultado = 0
        texto = False
    else:
        calculadoraPantalla.set(resultado)
    if desabilitados:
        habilitarBotones()
        desabilitados = False 
    if error:
        resultado = 0
        desabilitarBotones()
        calculadoraPantalla.set('')
    operacion = ""
    operacion2 = True
    resultado = 0
    numero = False
    cero = False
    if punto:
        habilitarPunto()
    coma = False

def borrar():
    global numero
    global contador
    global resultado
    global operacion
    global operacion2
    global punto
    global error
    global desabilitados
    global cero
    global coma
    cuadroPantalla.delete(0, "end")
    numero = False
    contador = 0
    resultado = 0
    operacion = ""
    operacion2 = False
    error = False
    if desabilitados:
        habilitarBotones()
        desabilitados = False
    cero = False
    habilitarPunto()
    habilitarCero()
    desenfocar()
    coma = False


def borrarNumero():
    global desabilitados
    global numero
    global coma
    if desabilitados:
        habilitarBotones()
        desabilitados = False
    else:
        if calculadoraPantalla.get() != "":
            numeroNuevo = ""
            num = calculadoraPantalla.get()
            if len(num)-1 != 0:
                for i in range(len(num)-1):
                    numeroNuevo += num[i]
                calculadoraPantalla.set(numeroNuevo)
                if num[-1] == '.':
                    coma = False
                    habilitarPunto()
                    desabilitarCero()
            else:
                calculadoraPantalla.set("")
                numero = False
                habilitarCero()
                habilitarPunto()
    

#? CREACIÓN DEL FRAME|----------------------------------------------------------------------------------------------


frame = Frame(root)
frame.pack()
frame.config(bg="#5B538A")


cuadroPantalla = Entry(frame, justify="right", width=38, textvariable=calculadoraPantalla)
cuadroPantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
cuadroPantalla.config(borderwidth=10, bg="#C0B5FF")
#cuadroPantalla['state'] = DISABLED


#? BOTONES 7, 8, 9|-------------------------------------------------------------------------------------------------


boton7 = Button(frame, text="7", width=4, height=3, font=(5), command=lambda:boton("7"))
boton7.grid(row=1, column=0, padx=10, pady=10)
boton7.config(bg='#ADFCEF')


boton8 = Button(frame, text="8", width=4, height=3, font=(5), command=lambda:boton("8"))
boton8.grid(row=1, column=1, padx=10, pady=10)
boton8.config(bg='#ADFCEF')


boton9 = Button(frame, text="9", width=4, height=3, font=(5), command=lambda:boton("9"))
boton9.grid(row=1, column=2, padx=10, pady=10)
boton9.config(bg='#ADFCEF')


#? BOTONES 4, 5, 6|-------------------------------------------------------------------------------------------------


boton4 = Button(frame, text="4", width=4, height=3, font=(5), command=lambda:boton("4"))
boton4.grid(row=2, column=0, padx=10, pady=10)
boton4.config(bg='#ADFCEF')


boton5 = Button(frame, text="5", width=4, height=3, font=(5), command=lambda:boton("5"))
boton5.grid(row=2, column=1, padx=10, pady=10)
boton5.config(bg='#ADFCEF')


boton6 = Button(frame, text="6", width=4, height=3, font=(5), command=lambda:boton("6"))
boton6.grid(row=2, column=2, padx=10, pady=10)
boton6.config(bg='#ADFCEF')


#? BOTONES 1, 2, 3|-------------------------------------------------------------------------------------------------


boton1 = Button(frame, text="1", width=4, height=3, font=(5), command=lambda:boton("1"))
boton1.grid(row=3, column=0, padx=10, pady=10)
boton1.config(bg='#ADFCEF')


boton2 = Button(frame, text="2", width=4, height=3, font=(5), command=lambda:boton("2"))
boton2.grid(row=3, column=1, padx=10, pady=10)
boton2.config(bg='#ADFCEF')


boton3 = Button(frame, text="3", width=4, height=3, font=(5), command=lambda:boton("3"))
boton3.grid(row=3, column=2, padx=10, pady=10)
boton3.config(bg='#ADFCEF')


#? BOTONES ., 0, =|-------------------------------------------------------------------------------------------------


botonPunto = Button(frame, text=",", width=4, height=3, font=(5), command=lambda:boton("."))
botonPunto.grid(row=4, column=0, padx=10, pady=10)
botonPunto.config(bg='#FCADAD')


boton0 = Button(frame, text="0", width=4, height=3, font=(5), command=lambda:boton("0"))
boton0.grid(row=4, column=1, padx=10, pady=10)
boton0.config(bg='#ADFCEF')


botonIgual = Button(frame, text="=", width=4, height=3, font=(5), command=igual)
botonIgual.grid(row=4, column=2, padx=10, pady=10)
botonIgual.config(bg='#B2FCAD')


#? BOTONES +, -, *, /|----------------------------------------------------------------------------------------------


botonDividir = Button(frame, text="/", width=4, height=3, font=(5), command=divicion)
botonDividir.grid(row=1, column=3, padx=10, pady=10)
botonDividir.config(bg='#FCADAD')


botonProducto = Button(frame, text="x", width=4, height=3, font=(5), command=producto)
botonProducto.grid(row=2, column=3, padx=10, pady=10)
botonProducto.config(bg='#FCADAD')


botonResta = Button(frame, text="-", width=4, height=3, font=(5), command=resta)
botonResta.grid(row=3, column=3, padx=10, pady=10)
botonResta.config(bg='#FCADAD')


botonSuma = Button(frame, text="+", width=4, height=3, font=(5), command=suma)
botonSuma.grid(row=4, column=3, padx=10, pady=10)
botonSuma.config(bg='#FCADAD')


#? BOTONES DE BORRAR|-----------------------------------------------------------------------------------------------


botonBorrar = Button(frame, text="C", width=12, height=3, font=(5), command=lambda:borrar())
botonBorrar.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
botonBorrar.config(bg='#B2FCAD')


botonBorrarNumero = Button(frame, text="<", width=12, height=3, font=(5), command=borrarNumero)
botonBorrarNumero.grid(row=5, column=2, columnspan=2, padx=10, pady=10)
botonBorrarNumero.config(bg='#B2FCAD')







root.mainloop()

