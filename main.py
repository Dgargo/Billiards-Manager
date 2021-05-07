
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image



#Налоштування головного вікна
window = Tk()
window.title('Billiards manager V1')
window.geometry('800x800')
window.configure(bg='#f7fffd')
#Налаштування вкладок
nb = ttk.Notebook(window,height=800)
nb.pack(pady=10,fill='both')
Vkladki =['Golovna','Zakaz','Bronik','Menu','Quest']
i= 0
while i<=4:
    Vkladki[i] = ttk.Frame(window)
    i +=1

nb.add(Vkladki[0],text='Головна')
nb.add(Vkladki[1],text='Новий заказ')
nb.add(Vkladki[2],text='Заброньовані')
nb.add(Vkladki[3],text='Меню')
nb.add(Vkladki[4],text='?')

#Імпорт картинок
table_img_one ="image/table.png"
img = ImageTk.PhotoImage(Image.open(table_img_one))
panel = tk.Label(Vkladki[0], image=img)
stan_null_img="image/Gray.png"
gray = ImageTk.PhotoImage(Image.open(stan_null_img))
stan_gray =tk.Label(Vkladki[0], image= gray)

#Налаштування  стилю фону вкладок
fon = [1,2,3,4,5]
i=0
while i<=4:
    fon[i] = tk.Label(
        Vkladki[i],
        bg='#f7fffd',
        height=1000,
        width=800,
    )
    i +=1

#Налаштування стилю столів
table = [1, 2, 3, 4, 5, 6]
i = 0
while i <= 5:
    table[i] = tk.Label(
        Vkladki[0],
        bg='#f7fffd',
        image=img
    )
    i += 1

#Налаштування стилю номера стола
text = [1, 2, 3, 4, 5, 6]
n = [1, 2, 3, 4, 5, 6]
i = 0
while i <= 5:

    text[i] =tk.Label(
        Vkladki[0],
        text=f'№{n[i]}',
        font=('Consolas',14),
        fg='black',
        bg='#f7fffd',
        )
    i += 1

#Налаштування стилю стану стола
stan = [1, 2, 3, 4, 5, 6]
i = 0
while i <= 5:
    stan[i] = tk.Label(
        Vkladki[0],
        bg='#f7fffd',
        image=gray
    )
    i += 1

#Налаштування стилю часу стола
time = [1, 2, 3, 4, 5, 6]
i = 0
while i<=5 :
    time[i] = tk.Label(
        Vkladki[0],
        text='00:00:00',
        font=('Consolas', 14),
        fg='black',
        bg='#f7fffd',
    )
    i += 1
#Налаштування вкладки Заказ
Zakaz_N_T  = tk.Label(
        Vkladki[1],
        text='Номер Стола:',
        font=('Consolas', 14),
        fg='black',
        bg='#f7fffd',
)
Zakaz_N_C = ttk.Combobox(
    Vkladki[1],
    font=('Consolas', 14),
    width=1,
)
Zakaz_N_C['values'] =tuple(range(1,7))

Zakaz_T_Z =tk.Label(
        Vkladki[1],
        text='Час, з:          до:     ',
        font=('Consolas', 14),
        fg='black',
        bg='#f7fffd',
)

Zakaz_T_H = ttk.Combobox(
    Vkladki[1],
    font=('Consolas', 14),
    width =2,
)
Zakaz_T_H['values'] = tuple(range(10,24))

Zakaz_T_M = ttk.Combobox(
    Vkladki[1],
    font=('Consolas', 14),
    width =2,
)
Zakaz_T_M['values'] = tuple(range(0, 60))

Zakaz_T_H_D = ttk.Combobox(
    Vkladki[1],
    font=('Consolas', 14),
    width =2,
)
Zakaz_T_H_D['values'] = tuple(range(11,25))

Zakaz_T_M_D = ttk.Combobox(
    Vkladki[1],
    font=('Consolas', 14),
    width =2,
)
Zakaz_T_M_D['values'] = tuple(range(0, 60))

Zakaz_B = tk.Button(
    Vkladki[1],
    text ='Відправити',
    font=('Consolas', 14),
    width=15,
    height=1,
    bg='#8cffa7'
)
Bron = []
for i in range(10,24):
    Bron.append(i)
i = 0
while i <= 13:

    Bron[i] =tk.Label(
        Vkladki[2],
        text=f'{Bron[i]}',
        font=('Consolas',16),
        bg='#3de060',
        )
    i += 1

Menu = tk.Label(
    Vkladki[3],
    text='''В даній вкладці можна настроїти скільки коштує година гри,
подивитися статистику за різні періоди''',
    font=('Consolas', 14),
    fg='black',
    bg='#f7fffd',
)

Quest = tk.Label(
    Vkladki[4],
    text='''В даній вкладці описано як користуватися програмою''',
    font=('Consolas', 14),
    fg='black',
    bg='#f7fffd',
)

#Налаштування розміщення  елементів
i=0
while i<=4:
    fon[i].pack()
    i +=1
table[0].place(x=20, y=50)
table[1].place(x=470, y=50)
table[2].place(x=20, y=300)
table[3].place(x=470, y=300)
table[4].place(x=20, y=550)
table[5].place(x=470, y=550)

text[0].place(x=100, y=20)
text[1].place(x=550, y=20)
text[2].place(x=100, y=270)
text[3].place(x=550, y=270)
text[4].place(x=100, y=520)
text[5].place(x=550, y=520)

stan[0].place(x=40, y=165)
stan[1].place(x=490, y=165)
stan[2].place(x=40, y=415)
stan[3].place(x=490, y=415)
stan[4].place(x=40, y=665)
stan[5].place(x=490, y=665)

time[0].place(x=100, y=180)
time[1].place(x=550, y=180)
time[2].place(x=100, y=430)
time[3].place(x=550, y=430)
time[4].place(x=100, y=680)
time[5].place(x=550, y=680)

Zakaz_N_T.place(x=30, y=25)
Zakaz_N_C.place(x=155, y=25)
Zakaz_T_Z.place(x=30, y=80)
Zakaz_T_H.place(x=105, y=80)
Zakaz_T_M.place(x=151, y=80)
Zakaz_T_H_D.place(x=233, y=80)
Zakaz_T_M_D.place(x=280, y=80)
Zakaz_B.place(x=30, y=130)
i =0
x1 = 50
y1 = 20
while i <=13:
    Bron[i].place(x=x1, y =y1)
    x1 +=31
    i  +=1

Menu.place(x=30, y=10)
Quest.place(x=30, y=10)
window.mainloop()