from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image

#Стиль  назви заказів
def NameZakaz(i,Zakaz_Name,Vkladki,text):
    Zakaz_Name[i] =tk.Label(
        Vkladki[1],
        text = text,
        font=('Arial Black', 18),
        bg='#086e02'

    )
#Стиль кнопок заказів
def Button_Z(i,Zakaz_B,Vkladki):
    while i<=1:
        Zakaz_B[i] = tk.Button(
            Vkladki[1],
            text='Відправити',
            font=('Arial Black', 14),
            width=15,
            height=1,
            bg='#8cffa7',
            relief =RIDGE
        )
        i +=1
#Стиль  тексту "Номер стола"
def Number_Tap_text(i,Num_Tab,Vkladki):
    while i<=1:
        Num_Tab[i] = tk.Label(
            Vkladki[1],
            text='Номер Стола:',
            font=('Arial Black', 12),
            fg='black',
            bg='#086e02',
        )
        i +=1