#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#    author='@rocky_roll,
#    license='GNU GPLv3'
#

import queue
import random

import speech_recognition as sr
from playsound import playsound

listener = sr.Recognizer()

filename = ('cat1.mp3', 'cat5.mp3')

cont = 0
cont1 = 0
q = queue.Queue()
q1 = queue.Queue()


def _sonido():
    global cont1
    cont1 += 1
    q1.put_nowait(cont)
    numeros = random.randint(0, 1)
    playsound(filename[numeros])


def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            listener.adjust_for_ambient_noise(source, duration=0.1)
            audio = listener.listen(source)
    except Exception as e:
        pass
    return audio


def recognize_audio(audio):
    print("Procesando...")
    rec = listener.recognize_google(audio, language='es-AR')
    rec = rec.lower()
    return rec


def main():
    global cont
    global q

    while True:
        try:
            response = recognize_audio(listen())

            if "macri" in response or "Macri" in response:
                _sonido()
                cont += 1
                q.put_nowait(cont)
        except:
            pass


if __name__ == "__main__":
    main()
