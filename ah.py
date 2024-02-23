#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#    author='@rocky_roll,
#    license='GNU GPLv3'
#

import os
import threading
import tkinter as tk
from tkinter import *

from recognize_google_ import *

counter = 0


def start():
    global t0
    t0 = threading.Thread(target=main, daemon=True)
    t0.start()


def close():
    os._exit(0)


def position(window, width_window, tall_window):
    x_window = window.winfo_screenwidth() // 2 - width_window // 2
    y_window = window.winfo_screenheight() // 2 - tall_window // 2
    position_ = str(width_window) + "x" + str(tall_window) + \
        "+" + str(x_window) + "+" + str(y_window)
    return position_

root = tk.Tk()
root.option_add('*Dialog.msg.font', 'Roboto 10')
root.title("Ah... ")
p1 = PhotoImage(file='logo32.png')
root.iconphoto(True, p1)
root.resizable(0, 0)
root.geometry(position(root,250,300))

class Application():

    def __init__(seft,root):
        seft.label = tk.Label(
            root, text=f"Ah... pero Macri {counter}",  font=("Roboto", 14))
        seft.label.pack(pady=6, padx=1)
        seft.imagen = tk.PhotoImage(file="cat1.png")
        seft.imagen2 = tk.PhotoImage(file="cat2.png")
        seft.label1 = tk.Label(root, image=seft.imagen)
        seft.label1.pack(pady=2, padx=1, ipadx=4, ipady=4)
        btnMiboton2 = tk.Button(root, text="salir", command=close,
                                activebackground="red", activeforeground="#D3D7CF")
        btnMiboton2.pack(pady=7, padx=4, ipadx=4, ipady=4)
        root.after(10, seft.actualizar_etiqueta, q)

    def actualizar_imagen(seft, q):
        try:
            cont = q.get_nowait()
            if cont == True:
                seft.label1.configure(image=seft.imagen2)
            if cont == False:
                seft.label1.configure(image=seft.imagen)
        except queue.Empty:
            pass
        root.after(10, seft.actualizar_imagen, q)

    def actualizar_etiqueta(seft, q):
        global counter
        try:
            cont = q.get_nowait()
            if cont == True:
                counter += 1
                seft.label.configure(text=f"Ah... pero Macri {counter}")
        except queue.Empty:
            pass
        root.after(10, seft.actualizar_etiqueta, q)


start()
obj1 = Application(root)
root.mainloop()