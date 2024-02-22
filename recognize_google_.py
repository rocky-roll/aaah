#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#    author='@rocky_roll,
#    license='GNU GPLv3'
#

import queue
import random

import speech_recognition as sr
# from playsound import playsound
import pygame
listener = sr.Recognizer()

filename = ('cat1.mp3', 'cat5.mp3')

cont = 0

q = queue.Queue()

pygame.init()


def random_():
    # numeros=0
    numeros = random.randint(0, 1)
    cat_sounds = filename[numeros]
    # print(str(cat_sounds),' ',numeros)
    return cat_sounds


def cat_sound():
    cat_sounds = random_()
    sound_ = pygame.mixer.Sound(cat_sounds)
    sound_.play()


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
    print(rec)
    return rec


def main():
    global q
    open_ = False
    while True:
        try:
            response = recognize_audio(listen())

            if "macri" in response or "hola" in response:
                cat_sound()
                open_ = True
                q.put_nowait(open_)
        except:
            pass


if __name__ == "__main__":
    main()
