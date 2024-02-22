#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#    author='@rocky_roll,
#    license='GNU GPLv3'
#

import os
import threading
import time
import tkinter as tk
from tkinter import *

from recognize_google_ import *

counter = 0


def start():
    t0 = threading.Thread(target=main, daemon=True)
    t0.start()


start()


def close():
    os._exit(0)


def actualizar_imagen(q):
    try:
        cont = q.get_nowait()
        if cont == True:
            label1.configure(image=imagen2)
        if cont == False:
            label1.configure(image=imagen)
    except queue.Empty:
        pass
    root.after(10, actualizar_imagen, q)


def actualizar_etiqueta(q):
    global counter
    try:
        cont = q.get_nowait()
        if cont == True:
            counter += 1
            label.configure(text=f"Ah... pero Macri {counter}")

    except queue.Empty:
        pass
    root.after(10, actualizar_etiqueta, q)


root = tk.Tk()
root.title("Ah... ")
ancho_ventana = 250
alto_ventana = 300
x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
    "+" + str(x_ventana) + "+" + str(y_ventana)
root.geometry(posicion)
p1 = PhotoImage(file='logo32.png')
root.iconphoto(True, p1)
root.resizable(0, 0)
# root.configure(bg="#3B3E3F")
label = tk.Label(
    root, text=f"Ah... pero Macri {counter}",  font=("Roboto", 14))
label.pack(pady=6, padx=1)
imagen = tk.PhotoImage(file="cat1.png")
imagen2 = tk.PhotoImage(file="cat2.png")
label1 = tk.Label(root, image=imagen)
label1.pack(pady=2, padx=1, ipadx=4, ipady=4)
btnMiboton2 = tk.Button(root, text="salir", command=close,
                        activebackground="red", activeforeground="#D3D7CF")
btnMiboton2.pack(pady=7, padx=4, ipadx=4, ipady=4)
root.after(1, actualizar_etiqueta, q)
root.mainloop()
