from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image

def NameZakaz(i,Name,Vkladki,text):
    Name[i] = tk.Label(
        Vkladki[1],
        text=text,
        font=('Arial Black', 18),
        bg='#086e02'
        )

def OthderTextZakaz(i,Name,Vkladki,text):
    Name[i] = tk.Label(
        Vkladki[1],
        text=text,
        font=('Arial Black', 14),
        bg='#086e02'
    )

def ButtonZakaz(i,Buton,Vkladki,funct):
    Buton[i]=tk.Button(
        Vkladki[1],
        text='Відправити',
        font=('Arial Black', 16),
        width=15,
        height=1,
        bg='#8cffa7',
        relief=RIDGE,
        command = funct
    )

def NumTable(i,NumB,Vkladki):
    NumB[i]= ttk.Combobox(
        Vkladki[1],
        font=('Arial Black', 12),
        width=1,
        values=list(range(1, 7))
    )

def HourZakaz(i,Hour,Vkladki,a,b):
    Hour[i] = ttk.Combobox(
        Vkladki[1],
        font=('Consolas', 12),
        width=2,
        values=list(range(a, b))

    )