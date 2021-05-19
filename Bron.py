from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image

#формування масиву
def BronMas(Bron):
    for i in range(10, 24):
        Bron.append(i)

#Налаштування  стилю  для рядка з часом
def BronTime(i,Bron,Vkladki):
    while i <= 13:
        Bron[i] = tk.Label(
            Vkladki[2],
            text=Bron[i],
            font=('Consolas', 20),
            bg='#c0fcee',
            width=2
        )
        i += 1

#Налаштування місця для рядка з часом
def BronPlaceTime(i,Bron1,x1,y1):
    while i <= 13:
        Bron1[i].place(x=x1, y=y1)
        x1 += 40
        i += 1

#Налаштування  стилю  для рядків з бронюванням
def Bronik(i,Bron,Vkladki):
    while i <= 13:
        Bron[i] = tk.Label(
            Vkladki[2],
            text='+',
            font=('Consolas', 20),
            bg='#3de060',
            width=2
        )
        i += 1

#Налаштування місця для рядка з бронюванням
def BronPlace(i,Bron1,x1,y1):
    while i <= 13:
        Bron1[i].place(x=x1, y=y1)
        x1 += 40
        i += 1

#Налаштування  стилю для столбця з номером стола
def BronNum(i,text,Vkladki):
    while i <= 5:
        text[i] = tk.Label(
            Vkladki[2],
            text=f'№{text[i]}',
            font=('Consolas', 20),
            fg='black',
            bg='#c0fcee',
        )
        i += 1

#Налаштування місця для столбця з номером стола
def BronNumPlace(i,Bron1,x1,y1):
    while i <= 5:
        Bron1[i].place(x=x1, y=y1)
        y1 += 45
        i += 1

