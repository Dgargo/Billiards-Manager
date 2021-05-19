
import tkinter as tk
from PIL import ImageTk, Image

#Налаштування  стилю фону вкладок
def Fon(i,fon,Vkladki):
    while i <= 4:
        fon[i] = tk.Label(
            Vkladki[i],
            bg='#f7fffd',
            height=1000,
            width=800,
        )
        i += 1

#функція для імпортування картинки стола і стану стола
def Stolic(i,table,Vkladki,img):
    while i <= 5:
        table[i] = tk.Label(
            Vkladki[0],
            bg='#f7fffd',
            image=img
        )
        i += 1

#Налаштування стилю номера стола
def Stolic_Text(i,text,Vkladki):
    while i <= 5:
        text[i] = tk.Label(
            Vkladki[0],
            text=f'№{text[i]}',
            font=('Consolas', 14),
            fg='black',
            bg='#f7fffd',
        )
        i += 1

#Налаштування стилю часу стола
def Stolic_time(i,time,Vkladki):
    while i <= 5:
        time[i] = tk.Label(
            Vkladki[0],
            text='00:00:00',
            font=('Consolas', 14),
            fg='black',
            bg='#f7fffd',
        )
        i += 1
#Налаштування стилю кнопки скидання
def Reset(i,res,Vkladki,img):
    while i<=5:
        res[i]=tk.Button(
            Vkladki[0],
            bg = '#fc2803',
            image=img
        )
        i += 1


