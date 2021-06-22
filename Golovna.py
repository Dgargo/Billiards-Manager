
import tkinter as tk
from PIL import ImageTk, Image

#Налаштування  стилю фону вкладок
def Fon(i,fon,Vkladki):
    while i <= 4:
        fon[i] = tk.Label(
            Vkladki[i],
            bg='#086e02',
            height=1000,
            width=800,
        )
        i += 1

#функція для імпортування картинки стола і стану стола
def Stolic(i,table,Vkladki,img):
        table[i] = tk.Label(
            Vkladki[0],
            bg = '#086e02',
            image=img
        )

#Налаштування стилю номера стола
def Stolic_Text(i,text,Vkladki):
    while i <= 5:
        text[i] = tk.Label(
            Vkladki[0],
            text=f'№{text[i]}',
            font=('Arial Black', 16),
            fg='black',
            bg='#086e02',
        )
        i += 1

#Налаштування стилю часу стола
def Stolic_time(i,time,Vkladki):
    time[i] = tk.Label(
        Vkladki[0],
        text='00:00:00',
        font=('Arial Black', 12),
        bg='#086e02',
            )

#Налаштування стилю кнопки скидання
def Reset(i,res,Vkladki,img):
    while i<=5:
        res[i]=tk.Button(
            Vkladki[0],
            bg = '#e82528',
            image=img,

        )
        i += 1


def Timer_Menu(i,Name,Vkladki,img):
    Name[i] = tk.Label(
        Vkladki[0],
        bg='#086e02',
        image=img,
         )


