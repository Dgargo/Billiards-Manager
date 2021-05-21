
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk

def M_Text(i,Name,Vkladki,Fsize,text):
    Name[i] = tk.Label(
        Vkladki[3],
        bg = '#086e02',
        font=('Arial Black', Fsize),
        text = text,
        )



