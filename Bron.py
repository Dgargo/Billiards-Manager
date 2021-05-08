from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image

def BronMas(Bron):
    for i in range(10, 24):
        Bron.append(i)

def Bronik(i,Bron,Vkladki):
    while i <= 13:
        Bron[i] = tk.Label(
            Vkladki[2],
            text=f'{Bron[i]}',
            font=('Consolas', 25),
            bg='#3de060',
        )
        i += 1

def BronPlace(i,Bron1,x1,y1):
    while i <= 13:
        Bron1[i].place(x=x1, y=y1)
        x1 += 44
        i += 1

def BronNum(i,text,Vkladki):
    while i <= 5:
        text[i] = tk.Label(
            Vkladki[2],
            text=f'№{text[i]}',
            font=('Consolas', 25),
            fg='black',
            bg='#f7fffd',
        )
        i += 1
def BronNumPlace(i,Bron1,x1,y1):
    while i <= 5:
        Bron1[i].place(x=x1, y=y1)
        y1 += 80
        i += 1