
import tkinter as tk

#Налаштування стилю тексту в вкладці меню
def M_Text(i,Name,Vkladki,Fsize,text):
    Name[i] = tk.Label(
        Vkladki[3],
        bg = '#086e02',
        font=('Arial Black', Fsize),
        text = text,
        )



